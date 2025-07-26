# tests/test_core.py

import re
from monitor.utils import extract_matching_lines

def test_core_matching_patterns():
    # Simulate sample log content
    log_data = [
        "INFO: Everything is working",
        "WARNING: Low memory",
        "CRITICAL: Disk failure detected",
        "ERROR: FAILED login from IP 192.168.1.10",
        "Notice: User login success",
        "Unauthorized access attempt from IP 10.0.0.3"
    ]

    error_patterns = ["CRITICAL", "FAILED", "unauthorized access"]
    compiled_patterns = [re.compile(p, re.IGNORECASE) for p in error_patterns]

    result = extract_matching_lines(log_data, compiled_patterns)

    assert len(result) == 3
    assert any("CRITICAL" in r for r in result)
    assert any("FAILED" in r for r in result)
    assert any("unauthorized access" in r.lower() for r in result)
