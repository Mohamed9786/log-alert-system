# tests/test_utils.py

import re
from monitor.utils import extract_matching_lines

def test_extract_matching_lines():
    test_log_lines = [
        "INFO: Everything is fine",
        "CRITICAL: System overheating",
        "ERROR: FAILED to connect",
        "Segfault in memory",
        "Unauthorized access attempt",
    ]
    test_patterns = [re.compile(p, re.IGNORECASE) for p in ["CRITICAL", "FAILED", "segfault", "unauthorized access"]]

    matches = extract_matching_lines(test_log_lines, test_patterns)

    assert len(matches) == 4  # CRITICAL, FAILED, unauthorized access
    assert any("CRITICAL" in line for line in matches)
    assert any("FAILED" in line for line in matches)
    assert any("unauthorized access" in line.lower() for line in matches)
