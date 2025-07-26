# 🔍 Log Analyzer + Auto Alert System

A real-time, regex-based log monitoring and alert system with:

- 📊 Streamlit Dashboard
- 📧 Auto Email Alerts
- 🔁 Live Log Monitoring
- ✅ Pytest Unit Testing

---

## 📦 Features

- Filter logs using regex patterns (e.g., CRITICAL, FAILED, etc.)
- Email alerts triggered when matches exceed threshold
- Web UI to visualize log alerts
- Download matched logs
- Upload your own log file for analysis
- Modular, testable, and extensible

---

## 🚀 How to Run

### 1. Clone and Install

```bash
git clone https://github.com/yourname/log-alert-system.git
cd log-alert-system
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
```

### 2. Configure

Set your `.env` file:

```env
EMAIL_FROM=youremail@gmail.com
EMAIL_PASS=yourapppassword
```

Edit `config.yaml`:

```yaml
log_path: system_errors.log
error_patterns:
  - "\\[Error\\]"
  - "\\[Warning\\]"
threshold: 1
email_to: targetemail@example.com
```

### 3. Run Streamlit UI

```bash
streamlit run streamlit_app/app.py
```

### 4. Run CLI Monitor (Optional)

```bash
python run.py
```

### 5. Run Tests

```bash
pytest
```

---

## 📁 Folder Structure

```
log-alert-system/
├── monitor/
│   ├── alert.py
│   ├── config.py
│   ├── constants.py
│   ├── core.py
│   ├── email.py
│   └── utils.py
│
├── streamlit_app/
│   └── app.py
│
├── test/
│   ├── test_config.py
│   ├── test_core.py
│   └── test_utils.py
│
├── logs/
│   └── app.log
├── sample_logs/
│   └── sample.log
├── config.yaml
├── run.py
├── pytest.ini
├── .gitignore
└── README.md
```

---

## 💡 Future Enhancements

- Export filtered logs by IP/date/type
- Real-time socket monitoring
- Integration with Slack or Telegram for alerts
- Admin panel to adjust thresholds/patterns

---

## 🛡️ License

This project is licensed under the MIT License.
