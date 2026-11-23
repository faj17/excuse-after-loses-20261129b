import os

TEXT = """I am pleased to report the loss was entirely my fault, which is the first thing I have ever gotten completely right.
"""


def validate_text(text):
    """Validate the entry text before writing.

    Rules: 1-200 characters, UTF-8-encodable, and a single line
    (no newline characters except the trailing one).
    """
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry text must be 1-200 chars, got {len(text)}")
    text.encode("utf-8")
    body = text[:-1] if text.endswith("\n") else text
    if "\n" in body or "\r" in body:
        raise ValueError("entry text must be a single line")


validate_text(TEXT)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
