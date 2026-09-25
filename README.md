### Shobhit Agnihotri

I make  LLM architectures from scratch, post-training RL systems, and autonomous agent infrastructure from first principles. Graduating from  IIT Madras.

Experience:
- Independent Systems & ML Researcher. September 2024 – Present.
  Implementing frontier model architectures, test-time search, and RL alignment algorithms from scratch (World Models, GRPO, MoE, custom autograd, LoRA/DPO).
- AI Engineer at [LOQO.AI](https://loqo.ai). January 2024 – August 2024.
  Architected multi-modal video intelligence and automated narrative generation pipelines using Whisper, LangChain, and diffusion models. Reduced manual production turnaround by ~90%.

Education:
- [Indian Institute of Technology, Madras](https://www.iitm.ac.in) (IIT Madras). 2023 – 2026 (Expected).

World Models:
- [dreamer4-coinrun](https://github.com/shobhitagnihotri69/dreamer4-coinrun) : Trained a 1.57B-parameter action-conditioned world model with flow matching + shortcut forcing on 9.6M self-generated CoinRun frames on an H200 (PSNR 40.41, beating GenieRedux baselines). Debugged and fixed 5 upstream bugs in the original codebase that prevented environment rollouts.
- [world-model-from-scratch](https://github.com/shobhitagnihotri69/world-model-from-scratch) : Implementation of Ha & Schmidhuber (2018) World Models. Trains a VAE visual compressor and MDN-RNN memory network (~167k parameters) to learn environment dynamics from raw pixels and simulate game rollouts entirely within hallucinated latent dreams.

LLMs from Scratch:
- [llm-lite](https://github.com/shobhitagnihotri69/llm-lite) : Complete, zero-dependency transformer stack in pure PyTorch/NumPy. 8 stages built from scratch: custom BPE tokenizer, autograd engine, AdamW optimizer, RoPE + Multi-Head Attention + KV-Cache, pre-training, SFT, LoRA, and INT4 quantization with comprehensive test coverage.
- [nano-gpt-oss](https://github.com/shobhitagnihotri69/nano-gpt-oss) : Transformer framework outperforming the GPT-2 baseline across 18 ablation configurations. Features gated Mixture-of-Experts (MoE) routing, SwiGLU activations, Grouped-Query Attention (GQA), and Sliding Window Attention with sink tokens.
- [DeepSeek-From-Scratch](https://github.com/shobhitagnihotri69/DeepSeek-From-Scratch) : Ground-up PyTorch implementation of DeepSeek architecture innovations, including Multi-Head Latent Attention (MLA) with decoupled RoPE compression and DeepSeekMoE fine-grained sparse expert routing.

Post-Training & RL:
- [mercor-grpo-agent](https://github.com/shobhitagnihotri69/mercor-grpo-agent) : Empirical reproduction and critique of Mercor's RL post-training setup vs. standard DeepSeek GRPO on SWE-bench. Investigated length hacking, token entropy regularization, and dynamic DPPO prefix-masking with an interactive benchmark runner.
- [swe-in-prod](https://github.com/shobhitagnihotri69/swe-in-prod) : From-scratch implementation of Group Relative Policy Optimization (GRPO, DeepSeek-R1) for agentic reasoning and code synthesis. Built the actor-environment-reward loop, advantage normalization without a critic network, and LoRA policy optimization on real SWE-bench tasks.
- [Reasoning-for-LLMs](https://github.com/shobhitagnihotri69/Reasoning-for-LLMs) : Test-time compute scaling, Chain-of-Thought (CoT) search algorithms, and Process Reward Models (PRM) with guided beam search across multi-step mathematical and algorithmic reasoning benchmarks.

Agents in Production:
- [Slack-ClawdBot](https://github.com/shobhitagnihotri69/Slack-ClawdBot) : Production TypeScript agent infrastructure integrating semantic RAG over historical chat threads, persistent memory using mem0, Model Context Protocol (MCP) clients for GitHub & Notion, and 59 custom tool executions. Docker-deployed.
- [Vizuara-Agents-10Day-Bootcamp](https://github.com/shobhitagnihotri69/agents-bootcamp-beginner) : Multi-agent orchestration architectures spanning LangGraph, CrewAI, and Smolagents for automated code review desks, CI log triage, and deterministic tool-calling workflows.

Open Source Contributions & Merged Pull Requests:
<!-- START_MERGED_PRS -->
<!-- Do not edit this section manually. It is automatically updated by GitHub Actions. -->
> **Total Merged Pull Requests: 22** across frontier AI agent runtimes, robotics foundation data pipelines, and developer tooling.

| Repository | PR | Description | Merged Date |
| :--- | :---: | :--- | :---: |
| [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow) | [#625](https://github.com/Hebbian-Robotics/hflow/pull/625) | `fix(importers/lerobot): refuse unsupported storage_format (#624)` | Sep 25, 2026 |
| [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow) | [#621](https://github.com/Hebbian-Robotics/hflow/pull/621) | `fix(doctor): report missing channels in chunk indexes instead of crashing (#620)` | Sep 24, 2026 |
| [ColinGPT9/clips-studio](https://github.com/ColinGPT9/clips-studio) | [#104](https://github.com/ColinGPT9/clips-studio/pull/104) | `fix(pipeline): persist recovered metadata to db on cached downloads a…` | Sep 24, 2026 |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | [#1330](https://github.com/orbi-build/orbi/pull/1330) | `fix(#1320): stagger runner timer instances with deterministic offsets` | Sep 24, 2026 |
| [agentclientprotocol/claude-agent-acp](https://github.com/agentclientprotocol/claude-agent-acp) | [#1173](https://github.com/agentclientprotocol/claude-agent-acp/pull/1173) | `fix: announce resumed subagent generations when they start` | Sep 24, 2026 |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | [#1327](https://github.com/orbi-build/orbi/pull/1327) | `fix(runner): serialize issue claim and slot delivery identity with cl…` | Sep 24, 2026 |
| [agentconnect-md/agentconnect](https://github.com/agentconnect-md/agentconnect) | [#2381](https://github.com/agentconnect-md/agentconnect/pull/2381) | `fix(daemon): apply configured agent model to memory dream extraction …` | Sep 24, 2026 |
| [preloop/preloop](https://github.com/preloop/preloop) | [#880](https://github.com/preloop/preloop/pull/880) | `fix(flows): preserve full command result payload on terminal mark` | Sep 24, 2026 |
| [truera/trulens](https://github.com/truera/trulens) | [#2809](https://github.com/truera/trulens/pull/2809) | `fix(core): make delete_singleton match the stored key and disable OTEL exporters` | Sep 23, 2026 |
| [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow) | [#614](https://github.com/Hebbian-Robotics/hflow/pull/614) | `fix(prefetch): handle concurrent aclose, error recovery, and director…` | Sep 23, 2026 |
| [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow) | [#606](https://github.com/Hebbian-Robotics/hflow/pull/606) | `feat(cache): use platformdirs as single owner of user cache paths (#585)` | Sep 23, 2026 |
| [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow) | [#592](https://github.com/Hebbian-Robotics/hflow/pull/592) | `feat(examples/egocentric): add WebDataset tar converter with metadata…` | Sep 22, 2026 |
| [huggingface/Repo2RLEnv](https://github.com/huggingface/Repo2RLEnv) | [#137](https://github.com/huggingface/Repo2RLEnv/pull/137) | `fix(reward): ignore git extended headers and mode lines in diff norma…` | Sep 22, 2026 |
| [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow) | [#589](https://github.com/Hebbian-Robotics/hflow/pull/589) | `fix(storage): expose object-store mirror refresh activity with bounde…` | Sep 22, 2026 |
| [trycua/cua](https://github.com/trycua/cua) | [#4019](https://github.com/trycua/cua/pull/4019) | `fix(cua-driver): report daemon_running accurately from socket liveness` | Sep 22, 2026 |
| [AssemblyAI/assemblyai-node-sdk](https://github.com/AssemblyAI/assemblyai-node-sdk) | [#186](https://github.com/AssemblyAI/assemblyai-node-sdk/pull/186) | `fix(realtime): reject connect() promise when WebSocket errors before …` | Sep 21, 2026 |
| [preloop/preloop](https://github.com/preloop/preloop) | [#820](https://github.com/preloop/preloop/pull/820) | `fix(mcp): recover database failures and sanitize tool errors` | Sep 19, 2026 |
| [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow) | [#572](https://github.com/Hebbian-Robotics/hflow/pull/572) | `feat(build-ai): migrate evaluation CLI from argparse to Typer (#566)` | Sep 19, 2026 |
| [preloop/preloop](https://github.com/preloop/preloop) | [#808](https://github.com/preloop/preloop/pull/808) | `fix(cli): one OAuth lineage per Codex CLI enrollment (#799)` | Sep 19, 2026 |
| [preloop/preloop](https://github.com/preloop/preloop) | [#796](https://github.com/preloop/preloop/pull/796) | `fix(ask_user): drop unsupported item keys and validate schema item re…` | Sep 18, 2026 |
| [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow) | [#559](https://github.com/Hebbian-Robotics/hflow/pull/559) | `fix(lerobot): refuse task_index referencing unpublished tasks before …` | Sep 18, 2026 |
| [uselemma/lemma](https://github.com/uselemma/lemma) | [#81](https://github.com/uselemma/lemma/pull/81) | `fix(tracing): detect success: false and status: error tool failure pa…` | Sep 15, 2026 |
<!-- END_MERGED_PRS -->

Technical Focus:
- PyTorch, NumPy, CUDA, Custom Autograd, Flow Matching, World Models
- GRPO, PPO, DPO, Process Reward Models (PRM), LoRA / PEFT, Test-Time Search
- Model Context Protocol (MCP), TypeScript, LangGraph, RAG, Modal GPU Infra, Docker

Contact:
- Email: shobhitagnihotri416@gmail.com
- Portfolio: [shobhitagnihotri69.github.io](https://shobhitagnihotri69.github.io)
- GitHub: [shobhitagnihotri69](https://github.com/shobhitagnihotri69)
