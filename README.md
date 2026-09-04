# Hi, I'm Shobhit 👋

I'm an AI/ML engineer based in India. I build things at the intersection of LLM internals, reinforcement learning, and agent systems — usually from scratch, because that's the only way I actually learn how they work.

---

## Things I've Built

### 🌍 [dreamer4-coinrun](https://github.com/shobhitagnihotri69/dreamer4-coinrun)
Trained the full Dreamer 4 architecture on 9.6M frames of CoinRun I generated myself. A 1.57B-parameter action-conditioned transformer trained with flow matching + shortcut forcing on one H200. PSNR 40.41 — beats GenieRedux baseline. Cost: ~$150.

The original Open Dreamer codebase had 5 bugs that prevented it from running on CoinRun at all. I found and fixed all of them. The debugging notes are in the repo.

### 🤖 [swe-in-prod](https://github.com/shobhitagnihotri69/swe-in-prod)
Implemented GRPO (Group Relative Policy Optimization) from scratch — the same RL algorithm DeepSeek-R1 uses for reasoning. Applied it to fine-tune Qwen 2.5 Coder 0.5B on real SWE-bench bugs using a mock shell environment. No critic, no value network. Just sampling N rollouts, scoring them, and updating the policy.

### 🔬 [llm-lite](https://github.com/shobhitagnihotri69/llm-lite)
Complete LLM stack from scratch in PyTorch. 8 stages: tokenizer → NumPy autograd → custom AdamW → RoPE + Multi-Head Attention + KV-Cache → pre-training → SFT → LoRA + DPO + PPO → INT4 quantization. Every component has unit tests. No HuggingFace in the core.

### 📊 [nano-gpt-oss](https://github.com/shobhitagnihotri69/nano-gpt-oss)
A transformer that beats GPT-2 baseline across 18 ablations (varied heads, layers, hidden dim). Architecture additions: MoE with gated routing, SwiGLU FFN, Grouped Query Attention + RoPE, Sliding Window Attention, Sink Slots, RMSNorm.

### 🧠 [world-model-from-scratch](https://github.com/shobhitagnihotri69/world-model-from-scratch)
Implementation of Ha & Schmidhuber 2018 "World Models" on MiniPong. Two tiny networks (V + M, ~167k params) learn the physics of Pong from pixels alone, then simulate the game with the actual game engine turned off.

### 💬 [Slack-ClawdBot](https://github.com/shobhitagnihotri69/Slack-ClawdBot)
Production TypeScript Slack bot with three integrated systems: RAG (semantic search over indexed Slack history), long-term memory with mem0.ai, and MCP integration for GitHub and Notion. 59 tools. Docker-deployed.

---

## Stack

**Core:** Python · PyTorch · NumPy  
**LLMs & Agents:** LangGraph · CrewAI · Smolagents · LlamaIndex · LangChain  
**Infra:** Modal · Vercel · Docker · Hugging Face  
**Backend:** FastAPI · TypeScript · Node.js  
**Other:** MCP (Model Context Protocol) · PEFT · LoRA · GRPO · PPO · DPO

---

## Currently

Looking for a **remote AI engineering internship** ($500/month). I can contribute 20–25 hours/week, work async, and take real engineering tasks off your backlog.

If you're building something interesting in AI infrastructure, agents, or LLM fine-tuning — reach out.

📧 Open to GitHub issues, PRs, and LinkedIn.

