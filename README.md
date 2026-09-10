# Justin Leopard

Software engineer building agent infrastructure: orchestration layers, safe local execution, typed memory, routing policy, evaluation, and the operator surfaces that make autonomous runs accountable.

I care about the unglamorous parts of agent systems: the queue, trace, sandbox, review gate, memory record, cost ledger, and handoff. If those pieces are weak, the model looks impressive right up until it repeats the same expensive mistake.

## Current Focus

| Surface | Maturity | What to inspect |
| --- | --- | --- |
| [JustAi](https://github.com/JustinJLeopard/JustAi) | Prototype | Intent, planning, review, and checkpoint control plane. The public execution path is currently unwired and fails closed. |
| [JustAi demo](https://justai-demo.vercel.app) | Simulation | Deterministic, fixture-backed mission-control walkthrough. It has no backend or live agents. |
| [safe-mini](https://github.com/JustinJLeopard/safe-mini) | Alpha substrate | Policy-guarded local bash-action loop. Built-in executors run in the host process; isolation requires an injected executor boundary. |
| [route-mini](https://github.com/JustinJLeopard/route-mini) | Reference | Deterministic multi-provider routing policy with fallback, budget, latency targets, and decision records. |
| [memory-mini](https://github.com/JustinJLeopard/memory-mini) | Reference | Namespaced memory semantics: upsert, soft delete, cleanup, retrieval, and optional embeddings. |
| [lab-mini](https://github.com/JustinJLeopard/lab-mini) | Reference | Repeatable data-science lab loop: load, profile, analyze, claim, report. |

These labels describe the public artifacts as they work today, not the larger
architecture they are intended to become.

## Operating Thesis

Agents get useful when the system around them is engineered like production infrastructure.

- **Sandbox the boundary, not the capability.** Give the agent room to solve the task inside a scoped worktree, scrubbed environment, guarded path, and recorded trajectory.
- **Trajectories beat vibes.** Every action should leave a replayable trace that can teach the next run.
- **Routing is policy.** Stronger models are an escalation decision, not a default reflex.
- **Memory has lifecycle.** Durable context needs namespacing, upsert, retention, and cleanup rather than chat-history luck.
- **Evaluation should change behavior.** A score that does not route, block, or teach the next run is mostly decoration.

## Public Inspection Path

- Portfolio and writing: [delegateandorchestrate.com](https://www.delegateandorchestrate.com)
- Interactive simulation: [justai-demo.vercel.app](https://justai-demo.vercel.app)
- Control-plane prototype: [JustAi](https://github.com/JustinJLeopard/JustAi)
- Substrate and reference repos: [safe-mini](https://github.com/JustinJLeopard/safe-mini), [route-mini](https://github.com/JustinJLeopard/route-mini), [memory-mini](https://github.com/JustinJLeopard/memory-mini), [lab-mini](https://github.com/JustinJLeopard/lab-mini)

## Systems I Track Closely

I keep forks and notes around projects that shape the work:

- [mini-swe-agent](https://github.com/JustinJLeopard/mini-swe-agent) and [SWE-agent](https://github.com/JustinJLeopard/SWE-agent) for minimal bash-action agents and issue-solving loops.
- [MCP Python SDK](https://github.com/JustinJLeopard/python-sdk) and [MCP TypeScript SDK](https://github.com/JustinJLeopard/typescript-sdk) for tool protocol boundaries.
- [smolagents](https://github.com/JustinJLeopard/smolagents) and [Vercel AI SDK](https://github.com/JustinJLeopard/ai) for code-agent and TypeScript agent interface patterns.

The goal is not to collect logos; it is to keep the public graph close to the ideas I am building against.

## Background

- US Navy veteran, aircraft maintenance. The useful lesson was not ceremony; it was operational seriousness.
- Full-stack engineer across Python, TypeScript, React, Node, SQL, local Linux/WSL, and browser-visible product surfaces.
- Building Delegate & Orchestrate around practical agent systems that can be inspected, tested, and improved.

## Contact

- Site: [delegateandorchestrate.com](https://www.delegateandorchestrate.com)
- Email: [delegateandorchestrate@delegateandorchestrate.com](mailto:delegateandorchestrate@delegateandorchestrate.com)
- LinkedIn: [linkedin.com/in/justinjleopard](https://linkedin.com/in/justinjleopard)
