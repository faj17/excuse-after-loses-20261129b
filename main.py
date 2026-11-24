import os

TEXT = """I am pleased to report the loss was entirely my fault, which is the first thing I have ever gotten completely right.
"""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
