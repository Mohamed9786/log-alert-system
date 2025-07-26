import re
import logging
from monitor.constants import DEFAULT_PATTERNS, DEFAULT_THRESHOLD, DEFAULT_LOG_PATH
from monitor.alert import send_email_alert
from monitor.utils import extract_summary, format_summary, filter_recent_lines

def load_log_file(log_path: str) -> list:
    """
    Reads a log file and returns its contents as a list of lines.
    """
    with open(log_path, "r") as f:
        return f.readlines()


def monitor_logs(config):
    log_path = config.get("log_path", DEFAULT_LOG_PATH)
    patterns = config.get("error_patterns", DEFAULT_PATTERNS)
    threshold = config.get("threshold", DEFAULT_THRESHOLD)
    email_to = config.get("email_to")

    try:
        with open(log_path, "r", errors="ignore") as f:
            lines = f.readlines()
    except FileNotFoundError:
        logging.error(f"Log file not found: {log_path}")
        return

    # Apply time filter if needed
    filtered_lines = filter_recent_lines(lines)

    matches = []
    for line in filtered_lines:
        for pattern in patterns:
            if re.search(pattern, line, re.IGNORECASE):
                matches.append(line.strip())
                break  # avoid double-counting same line

    match_count = len(matches)
    logging.info(f"{match_count} matching log entries found.")

    if match_count >= threshold:
        summary_data = extract_summary(matches)
        summary_text = format_summary(summary_data)
        full_log = "\n".join(matches[:50])

        send_email_alert(
            subject=f"[ALERT] {match_count} Issues Found in Logs",
            summary=summary_text,
            full_log=full_log,
            sender=config.email_from,
            password=config.email_pass,
            recipient=email_to
        )
    else:
        logging.info(f"No alert sent. Match count ({match_count}) below threshold ({threshold}).")
