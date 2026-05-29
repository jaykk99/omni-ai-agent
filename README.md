# Monico Agent

⚠️ **The old site (Omni bot / previous Vercel deployment) is broken** and returns 404.

✅ **Live site:** [https://monico-agent.vercel.app](https://monico-agent.vercel.app)

**Hierarchical Autonomous AI Agent Platform**

## Local Installation

### Mac
```bash
git clone https://github.com/jaykk99/monico-agent.git
cd monico-agent
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

### Linux
```bash
git clone https://github.com/jaykk99/monico-agent.git
cd monico-agent
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

### Windows
```bash
git clone https://github.com/jaykk99/monico-agent.git
cd monico-agent
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

## Integrations
- **Telegram**: `python -m monico --telegram`
- **Slack**: `python -m monico --slack`
- **SMS (Twilio)**: `python -m monico --sms`

## Quick Start
1. `pip install -r requirements.txt`
2. `uvicorn backend.main:app --reload`

## API
**POST /run**
```json
{
  "input": "Hello, research something for me",
  "user_id": "test_user"
}
```