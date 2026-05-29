# Monico Agent

**Hierarchical Autonomous AI Agent Platform** with **Safe** and **Uncensored** editions.

## Editions

### Monico Safe (Default / Free)
- Sandboxed Docker execution (zero blast radius)
- Moderated models

### Monico Uncensored (Paid)
- Non-sandboxed, full power
- Hugging Face uncensored models
- Set `MONICO_TIER=paid` in environment

## Quick Start (No Stripe needed)

1. Set env var: `MONICO_TIER=paid` (or leave as free)
2. `pip install -r requirements.txt`
3. `uvicorn backend.main:app --reload`

## API

**POST /run**
```json
{
  "input": "Hello, research something for me",
  "user_id": "test_user"
}
```

