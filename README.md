# Monico Agent

⚠️ The old Omni site is broken (404).

Live at: [https://monico-agent.vercel.app](https://monico-agent.vercel.app)

## 📥 Download & Installation

### Termux (Android)

```bash
# Update and install dependencies
pkg update && pkg upgrade -y
pkg install python git clang libffi openssl tur-repo -y
pkg install python-pip

# Clone or download the repo (if not in Termux)
git clone https://github.com/jaykk99/monico-agent.git
cd monico-agent

# Install Python packages
pip install --upgrade pip
pip install -r requirements.txt

# Run the app
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

**Tips for Termux:** 
- Use `termux-wake-lock` for background running.
- Install additional pkgs if errors occur (e.g., `pkg install libjpeg-turbo` for image libs).
- Access via browser at http://localhost:8000 or use ngrok for external.

### Mac / Linux / Windows
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Integrations
- **Telegram**: `python agent.py --telegram`
- **Slack**: `python agent.py --slack`
- **SMS**: `python agent.py --sms`

## Website
Visit the live site for more: https://monico-agent.vercel.app

Run the agent locally with the commands above.