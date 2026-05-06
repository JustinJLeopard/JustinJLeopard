# Justin Leopard

Software engineer building agent infrastructure: orchestration layers, safe local execution, typed memory, routing policy, evaluation, and the operator surfaces that make autonomous runs accountable.

I care about the unglamorous parts of agent systems: the queue, trace, sandbox, review gate, memory record, cost ledger, and handoff. If those pieces are weak, the model looks impressive right up until it repeats the same expensive mistake.

## Current Focus

| Surface | What it proves |
| --- | --- |
| [JustAi](https://github.com/JustinJLeopard/JustAi) | Control plane for multi-agent engineering work: intent, plan, execute, review, synthesize. |
| [JustAi demo](https://justai-demo.vercel.app) | Browser-visible mission control for task state, memory, trajectories, agents, cost, latency, and review quality. |
| [safe-mini](https://github.com/JustinJLeopard/safe-mini) | Safe-by-construction local execution for mini-swe-agent-style bash-action loops. |
| [route-mini](https://github.com/JustinJLeopard/route-mini) | Multi-provider LLM routing with fallback, budget, latency targets, and decision logging. |
| [memory-mini](https://github.com/JustinJLeopard/memory-mini) | Durable namespaced memory with upsert-first semantics, soft delete, cleanup, and optional embeddings. |
| [lab-mini](https://github.com/JustinJLeopard/lab-mini) | Repeatable data-science lab loop: load, profile, analyze, claim, report. |

## Operating Thesis

Agents get useful when the system around them is engineered like production infrastructure.

- **Sandbox the boundary, not the capability.** Give the agent room to solve the task inside a scoped worktree, scrubbed environment, guarded path, and recorded trajectory.
- **Trajectories beat vibes.** Every action should leave a replayable trace that can teach the next run.
- **Routing is policy.** Stronger models are an escalation decision, not a default reflex.
- **Memory has lifecycle.** Durable context needs namespacing, upsert, retention, and cleanup rather than chat-history luck.
- **Evaluation should change behavior.** A score that does not route, block, or teach the next run is mostly decoration.

## Public Proof Path

- Portfolio and writing: [delegateandorchestrate.com](https://www.delegateandorchestrate.com)
- Live demo: [justai-demo.vercel.app](https://justai-demo.vercel.app)
- Flagship repo: [JustAi](https://github.com/JustinJLeopard/JustAi)
- Substrate repos: [safe-mini](https://github.com/JustinJLeopard/safe-mini), [route-mini](https://github.com/JustinJLeopard/route-mini), [memory-mini](https://github.com/JustinJLeopard/memory-mini), [lab-mini](https://github.com/JustinJLeopard/lab-mini)

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
