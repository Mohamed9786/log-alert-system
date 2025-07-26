import datetime
import re


def extract_matching_lines(log_lines: list, patterns: list) -> list:
    """
    Extracts lines that match any of the given compiled regex patterns.
    """
    matching_lines = []
    for line in log_lines:
        for pattern in patterns:
            if pattern.search(line):
                matching_lines.append(line)
                break
    return matching_lines



def filter_recent_lines(lines, minutes=60):
    """
    Placeholder: In future, filter log lines within the last `minutes`.
    """
    return lines  # Not filtering for now (useful for syslogs with timestamps)

def extract_summary(matches):
    """
    Returns a count of matched error types for a readable alert summary.
    """
    summary = {}
    for line in matches:
        for key in ["CRITICAL", "FAILED", "segfault", "unauthorized access"]:
            if re.search(key, line, re.IGNORECASE):
                summary[key] = summary.get(key, 0) + 1
    return summary

def format_summary(summary):
    lines = [f"{k}: {v}" for k, v in summary.items()]
    return "\n".join(lines)
