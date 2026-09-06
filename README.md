### Shobhit Agnihotri

I build world models, LLM architectures from scratch, post-training RL systems, and autonomous agent infrastructure from first principles. B.S. in Data Science at IIT Madras.

Experience:
- Independent Systems & ML Researcher. September 2024 – Present.
  Implementing frontier model architectures, test-time search, and RL alignment algorithms from scratch (World Models, GRPO, MoE, custom autograd, LoRA/DPO).
- AI Engineer at [LOQO.AI](https://loqo.ai). January 2024 – August 2024.
  Architected multi-modal video intelligence and automated narrative generation pipelines using Whisper, LangChain, and diffusion models. Reduced manual production turnaround by ~90%.

Education:
- B.S. in Data Science & Applications, [Indian Institute of Technology, Madras](https://www.iitm.ac.in) (IIT Madras). 2022 – 2026 (Expected).

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

Technical Focus:
- PyTorch, NumPy, CUDA, Custom Autograd, Flow Matching, World Models
- GRPO, PPO, DPO, Process Reward Models (PRM), LoRA / PEFT, Test-Time Search
- Model Context Protocol (MCP), TypeScript, LangGraph, RAG, Modal GPU Infra, Docker

Contact:
- Email: shobhitagnihotri416 [at] gmail [dot] com
- Portfolio: [shobhitagnihotri69.github.io](https://shobhitagnihotri69.github.io)
- GitHub: [shobhitagnihotri69](https://github.com/shobhitagnihotri69)
