### Shobhit Agnihotri

I build world models, RL post-training systems (GRPO, DPO, PPO), and autonomous agent infrastructure from first principles. B.S. in Data Science at IIT Madras.

Experience:
- Independent Systems & ML Researcher. September 2024 – Present.
  Implementing frontier model architectures and alignment algorithms from scratch (World Models, GRPO, MoE, custom autograd, LoRA/DPO).
- AI Engineer at [LOQO.AI](https://loqo.ai). January 2024 – August 2024.
  Architected multi-modal video intelligence and story generation pipelines using Whisper, LangChain, and diffusion models. Reduced manual production time by ~90%.

Education:
- B.S. in Data Science & Applications, [Indian Institute of Technology, Madras](https://www.iitm.ac.in) (IIT Madras). 2022 – 2026 (Expected).

Projects:
- [dreamer4-coinrun](https://github.com/shobhitagnihotri69/dreamer4-coinrun) : Trained a 1.57B-parameter action-conditioned world model with flow matching + shortcut forcing on 9.6M self-generated CoinRun frames on an H200 (PSNR 40.41, beats GenieRedux baseline). Fixed 5 upstream bugs in the original codebase blocking environment rollouts.
- [mercor-grpo-agent](https://github.com/shobhitagnihotri69/mercor-grpo-agent) : Empirical reproduction and critique of Mercor's RL post-training setup vs. standard DeepSeek GRPO on SWE-bench. Evaluated length bias, token entropy regularization, and dynamic DPPO prefix-masking with an interactive benchmark runner.
- [swe-in-prod](https://github.com/shobhitagnihotri69/swe-in-prod) : From-scratch implementation of Group Relative Policy Optimization (GRPO, DeepSeek-R1) for agentic reasoning and code synthesis. Built the actor-environment loop, advantage normalization without a critic model, and LoRA policy updates on SWE-bench tasks.
- [llm-lite](https://github.com/shobhitagnihotri69/llm-lite) : Zero-dependency transformer and alignment stack in pure PyTorch/NumPy. Built custom autograd, BPE tokenizer, RoPE, KV-cache, SFT, LoRA, DPO, PPO, and INT4 weight-only quantization with full test suites.
- [nano-gpt-oss](https://github.com/shobhitagnihotri69/nano-gpt-oss) : Transformer architecture beating the GPT-2 baseline across 18 ablation configurations. Added gated Mixture-of-Experts (MoE) routing, SwiGLU activations, Grouped-Query Attention (GQA), and Sliding Window Attention with sink tokens.
- [Slack-ClawdBot](https://github.com/shobhitagnihotri69/Slack-ClawdBot) : Production TypeScript agent infrastructure with semantic RAG over historical chat threads, persistent memory via mem0, Model Context Protocol (MCP) clients for GitHub and Notion, and 59 custom tools.
- [world-model-from-scratch](https://github.com/shobhitagnihotri69/world-model-from-scratch) : Implementation of Ha & Schmidhuber (2018) World Models. Trains a VAE visual compressor and MDN-RNN memory network (~167k parameters) to simulate game rollouts entirely within hallucinated latent dreams.

Technical Focus:
- PyTorch, NumPy, CUDA, Transformers, Autograd, Flow Matching
- GRPO, PPO, DPO, Reward Modeling, Advantage Normalization, LoRA / PEFT
- Model Context Protocol (MCP), LangGraph, RAG, TypeScript, Modal GPU Infra, Docker

Contact:
- Email: shobhitagnihotri416 [at] gmail [dot] com
- Portfolio: [shobhitagnihotri69.github.io](https://shobhitagnihotri69.github.io)
- GitHub: [shobhitagnihotri69](https://github.com/shobhitagnihotri69)
