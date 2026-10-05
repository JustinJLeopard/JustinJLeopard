"""Run the actual publisher shell against a local GitHub CLI stub; no network."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import textwrap
import unittest

ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / '.github/workflows/exact-head-acceptance.yml'
SHA = '1' * 40
OTHER_SHA = '2' * 40
BASE = 'main'


class PublisherContract(unittest.TestCase):
    def run_publisher(self, *, environment=None, pr=None, response=None, api_fails=False, rewrite=None):
        source = WORKFLOW.read_text()
        script = textwrap.dedent(source.split('        run: |\n', 1)[1])
        if rewrite is not None:
            old, new = rewrite
            self.assertIn(old, script)
            script = script.replace(old, new)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'publisher.sh').write_text(script)
            subprocess.run(['bash', '-n', str(root / 'publisher.sh')], check=True)
            stub = root / 'gh'
            stub.write_text('''#!/usr/bin/env python3
import json, os, pathlib, sys
root = pathlib.Path(os.environ['STUB_ROOT'])
expected_pr = ['pr', 'view', os.environ['PR_NUMBER'], '--repo',
               os.environ['GITHUB_REPOSITORY'], '--json',
               'state,isDraft,baseRefName,headRefOid,isCrossRepository']
expected_api = ['api', '-X', 'POST', '-H', 'Accept: application/vnd.github+json',
                'repos/' + os.environ['GITHUB_REPOSITORY'] + '/check-runs',
                '--input', '-']
if sys.argv[1:] == expected_pr:
    print(os.environ['STUB_PR'])
elif sys.argv[1:] == expected_api:
    payload = json.load(sys.stdin)
    (root / 'published.json').write_text(json.dumps(payload))
    if os.environ['STUB_API_FAILS'] == '1':
        sys.exit(1)
    payload.update(json.loads(os.environ['STUB_RESPONSE']))
    print(json.dumps(payload))
else:
    sys.exit('Unexpected gh command: ' + repr(sys.argv))
''')
            stub.chmod(0o755)
            live_pr = dict(state='OPEN', isDraft=False, baseRefName=BASE,
                           headRefOid=SHA, isCrossRepository=False)
            live_pr.update(pr or {})
            env = dict(os.environ, PATH=tmp + os.pathsep + os.environ['PATH'],
                       STUB_ROOT=tmp, STUB_PR=json.dumps(live_pr),
                       STUB_RESPONSE=json.dumps(response or {}),
                       STUB_API_FAILS=str(int(api_fails)), PR_NUMBER='7',
                       SUPPLIED_SHA=SHA, DISPATCH_REF='refs/heads/' + BASE,
                       DISPATCH_ACTOR='JustinJLeopard', TRIGGERING_ACTOR='JustinJLeopard',
                       TRUSTED_ACCEPTORS='JustinJLeopard', CHECK_NAME='Exact-head acceptance',
                       GITHUB_REPOSITORY='example/repo', DETAILS_URL='https://example.invalid/run/1',
                       GITHUB_STEP_SUMMARY=str(root / 'summary'))
            env.update(environment or {})
            result = subprocess.run(['bash', str(root / 'publisher.sh')], env=env,
                                    capture_output=True, text=True)
            published = root / 'published.json'
            return result, json.loads(published.read_text()) if published.exists() else None

    def test_current_head_publishes_exact_identity(self):
        result, payload = self.run_publisher()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(payload['head_sha'], SHA)
        self.assertEqual(payload['external_id'], 'pr:7:' + SHA)
        self.assertEqual(payload['name'], 'Exact-head acceptance')
        self.assertEqual(payload['conclusion'], 'success')

    def test_invalid_dispatch_never_publishes(self):
        for field, value in [('DISPATCH_ACTOR', 'other'), ('TRIGGERING_ACTOR', 'other'),
                             ('DISPATCH_REF', 'refs/heads/untrusted'), ('PR_NUMBER', '0'),
                             ('PR_NUMBER', '7; echo injected'), ('SUPPLIED_SHA', 'short')]:
            with self.subTest(field=field, value=value):
                result, payload = self.run_publisher(environment={field: value})
                self.assertNotEqual(result.returncode, 0)
                self.assertIsNone(payload)

    def test_ineligible_or_new_head_never_publishes(self):
        for field, value in [('state', 'CLOSED'), ('isDraft', True),
                             ('baseRefName', 'other'), ('isCrossRepository', True),
                             ('headRefOid', OTHER_SHA)]:
            with self.subTest(field=field):
                result, payload = self.run_publisher(pr={field: value})
                self.assertNotEqual(result.returncode, 0)
                self.assertIsNone(payload)

    def test_bad_api_readback_fails(self):
        for field, value in [('name', 'wrong'), ('head_sha', OTHER_SHA),
                             ('external_id', 'wrong'), ('status', 'queued'),
                             ('conclusion', 'failure')]:
            with self.subTest(field=field):
                result, _ = self.run_publisher(response={field: value})
                self.assertNotEqual(result.returncode, 0)

    def test_wrong_transport_arguments_fail(self):
        for old, new in [
            ('--repo "$GITHUB_REPOSITORY"', '--repo "wrong/repo"'),
            ('view "$PR_NUMBER"', 'view "999"'),
            ('state,isDraft,baseRefName,headRefOid,isCrossRepository', 'state'),
            ('-X POST', '-X GET'),
            ('repos/$GITHUB_REPOSITORY/check-runs', 'repos/wrong/repo/check-runs'),
            ('--input -', '--input missing.json'),
        ]:
            with self.subTest(argument=old):
                result, payload = self.run_publisher(rewrite=(old, new))
                self.assertNotEqual(result.returncode, 0)
                self.assertIsNone(payload)

    def test_api_failure_fails(self):
        result, _ = self.run_publisher(api_fails=True)
        self.assertNotEqual(result.returncode, 0)


if __name__ == '__main__':
    unittest.main()
