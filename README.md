# 🛡️ Log Analyzer + Auto Alert System

## 🎯 Overview
An industry-ready Python tool to monitor logs (e.g., `/var/log/syslog`) and trigger alerts when error patterns are detected.

## 🔧 Features
- 🔍 Regex-based log scanning
- 📬 Email alerting via Gmail SMTP
- ⚙️ Configurable via `config.yaml`
- 🧪 Sample log testing (`sample.log`)
- 🕰️ Schedule via cron or systemd

## 📁 Project Structure
log-alert-system/
├── monitor/
│   ├── __init__.py
│   ├── core.py         # Log scanning logic
│   ├── alert.py        # Email alerting
│   ├── config.py       # Loads config.yaml + .env
│   ├── utils.py        # Time filtering, formatting
│   └── constants.py    # Regex patterns, thresholds
├── config.yaml
├── .env
├── run.py              # CLI entry point
├── sample.log          # For testing
├── logs/
│   └── app.log         # System logs
├── requirements.txt
└── README.md


## 🚀 Getting Started

1. Clone repo & install dependencies:

2. Configure:
- `config.yaml` → patterns, threshold, email_to
- `.env` → your `EMAIL_FROM` and `EMAIL_PASS`

3. Test it:
python run.py


## 🛠️ Scheduling with Cron
Run every 10 minutes:
*/10 * * * * /usr/bin/python3 /path/to/run.py


## 🐳 Optional: Docker (future)
Can be containerized to run on EC2, ECS, or Lambda.

---

✅ Ready for Interviews:
- Clean modular design
- Secure config handling
- Extendable for SMS, Slack, CloudWatch
