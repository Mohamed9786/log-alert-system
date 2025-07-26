import sys
import os
import re
import streamlit as st
from streamlit_autorefresh import st_autorefresh

# Add parent directory to sys.path to enable monitor package imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from monitor.config import Config
from monitor.core import load_log_file
from monitor.utils import extract_matching_lines, extract_summary, format_summary
from monitor.email import send_email_alert  # ⬅️ Import auto-emailing

# ------------------------
# 🔁 Auto-refresh (10 sec)
# ------------------------
st_autorefresh(interval=10_000, limit=None, key="auto-refresh")

# ------------------------
# ⚙️ Load Config
# ------------------------
config = Config()
default_log_path = config.get("log_path", "sample_logs/sample.log")
error_patterns = config.get("error_patterns", ["CRITICAL", "FAILED", "unauthorized access"])
compiled_patterns = [re.compile(p, re.IGNORECASE) for p in error_patterns]
threshold = config.get("threshold", 1)
email_to = config.get("email_to")
email_from = config.email_from
email_pass = config.email_pass

# ------------------------
# 🎨 UI Setup
# ------------------------
st.set_page_config(page_title="Log Analyzer", layout="wide")
st.title("Log Analyzer Dashboard")
st.markdown("Monitor log files and auto-extract alerts using regex patterns.")

# ------------------------
# 📤 Upload Log File (Optional)
# ------------------------
uploaded_file = st.file_uploader("Upload Log File (optional)", type=["log", "txt"])

# ------------------------
# 🔁 Load Log & Match
# ------------------------
if uploaded_file:
    try:
        log_lines = uploaded_file.read().decode("utf-8", errors="ignore").splitlines()
        matches = extract_matching_lines(log_lines, compiled_patterns)
        summary = extract_summary(matches)
        summary_text = format_summary(summary)
    except Exception as e:
        st.error(f"Failed to read uploaded file: {e}")
        log_lines, matches, summary_text = [], [], ""
else:
    refresh = st.button("Manual Refresh Log")
    if refresh or 'log_lines' not in st.session_state:
        try:
            log_lines = load_log_file(default_log_path)
            matches = extract_matching_lines(log_lines, compiled_patterns)
            summary = extract_summary(matches)
            summary_text = format_summary(summary)

            st.session_state["log_lines"] = log_lines
            st.session_state["matches"] = matches
            st.session_state["summary_text"] = summary_text

            st.success("Log loaded successfully!")
        except Exception as e:
            st.error(f"Error loading log: {e}")
            log_lines, matches, summary_text = [], [], ""
    else:
        log_lines = st.session_state.get("log_lines", [])
        matches = st.session_state.get("matches", [])
        summary_text = st.session_state.get("summary_text", "")

    # ------------------------
    # 📧 Auto Email Alert
    # ------------------------
    if len(matches) >= threshold:
        if not st.session_state.get("email_sent", False):
            try:
                send_email_alert(
                    subject="Log Analyzer Alert",
                    summary=summary_text,
                    full_log="\n".join(matches),
                    sender=email_from,
                    password=email_pass,
                    recipient=email_to
                )
                st.session_state["email_sent"] = True
                st.success("Alert email sent!")
            except Exception as e:
                st.error(f"Failed to send email: {e}")
    else:
        st.session_state["email_sent"] = False  # reset flag

# ------------------------
# 🔍 Filter Log Entries
# ------------------------
filter_keyword = st.text_input("Filter logs by keyword / IP / type")

if filter_keyword:
    matches = [line for line in matches if filter_keyword.lower() in line.lower()]

# ------------------------
# 📝 Summary of Alerts
# ------------------------
st.subheader("Summary of Alerts")
if summary_text:
    st.code(summary_text)
else:
    st.info("No matching patterns found.")

# ------------------------
# 📋 Matched Entries
# ------------------------
st.subheader("Matching Log Entries")
if matches:
    for line in matches[-50:]:
        st.text(line)

    st.download_button(
        label="Download Matched Logs",
        data="\n".join(matches),
        file_name="matched_logs.txt",
        mime="text/plain"
    )
else:
    st.info("No matching log entries found.")

# ------------------------
# 📂 Full Log Viewer
# ------------------------
with st.expander("View Full Log File (Last 50 lines)"):
    if log_lines:
        for line in log_lines[-50:]:
            st.text(line)
    else:
        st.warning("No log file content to display.")
