# Monico Agent

**Hierarchical Autonomous AI Agent Platform** with **Safe** and **Uncensored** editions.

## Editions

### 1. Monico Safe (Free/Default)
- Sandboxed execution
- Moderated models (Groq, OpenAI, etc.)
- Zero blast radius

### 2. Monico Uncensored (Paid)
- Non-sandboxed high-power mode
- Hugging Face uncensored models
- Full system access (user responsibility)

## Core Architecture
- Master-Worker pattern
- Observe → Think → Act → Evaluate cycle
- LiteLLM model registry

## Quick Start
```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

## API
POST /run

```json
{
  "input": "Your request here",
  "user_id": "user123"
}
```

