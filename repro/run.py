"""mistletoe #279：深层嵌套有序列表触发 RecursionError。
运行：
    uv venv --python 3.12 && uv pip install -e . && .venv/bin/python repro/run.py
"""
import pathlib
import sys

import mistletoe as m

text = pathlib.Path(__file__).with_name("deep.md").read_text(encoding="utf-8")
print(f"py input lines={len(text.splitlines())} chars={len(text)}")
try:
    html = m.markdown(text)
except RecursionError as error:
    print("RecursionError  <-- 这就是要修的")
    sys.exit(1)
print(f"OK, html length {len(html)}")
