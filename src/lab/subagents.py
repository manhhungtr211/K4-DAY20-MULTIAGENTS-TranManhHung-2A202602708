"""GUIDE Phần 1 - Định nghĩa subagent (tác tử con).   >>> SINH VIÊN CÀI ĐẶT <<<

Pseudo-code: guides/pseudocode/02_subagents.md
Kiểm tra:    pytest tests/test_02_agent.py
"""


def get_subagents() -> list[dict]:
    """Trả về danh sách subagent (ít nhất 2, tên khác nhau).

    Mỗi phần tử là một dict có các khóa bắt buộc:
      "name":          tên duy nhất (chữ thường, có thể có dấu gạch ngang)
      "description":   khi nào tác tử chính nên giao việc cho subagent này (viết như một hướng dẫn hành động)
      "system_prompt": chỉ dẫn cho subagent
    Gợi ý vai trò: explorer (đọc và báo cáo), implementer (thực hiện), reviewer (kiểm tra độc lập).
    """
    return [
        {
            "name": "explorer",
            "description": (
                "Use this agent to explore files, inspect logs, read docstrings, and understand "
                "data formats or code structure before making changes. Returns a detailed findings report."
            ),
            "system_prompt": (
                "You are an exploration subagent. Your role is to examine files, search code, "
                "inspect logs, and understand requirements. Report facts and findings clearly. "
                "Do not modify or delete files."
            ),
        },
        {
            "name": "implementer",
            "description": (
                "Use this agent to implement fixes, write or edit code, clean data files, "
                "and run scripts or tests. Returns a summary of changes and test results."
            ),
            "system_prompt": (
                "You are an implementation subagent. Your role is to make changes, write scripts, "
                "clean datasets, parse logs, and execute tests. Verify each change before finishing."
            ),
        },
        {
            "name": "reviewer",
            "description": (
                "Use this agent to independently inspect output files, verify schema adherence, "
                "check edge cases, and run regression tests. Returns verification status."
            ),
            "system_prompt": (
                "You are a reviewer subagent. Your role is to verify the solution against requirements. "
                "Check created files, run tests, and validate formatting. Do not make edits; report status."
            ),
        },
    ]
