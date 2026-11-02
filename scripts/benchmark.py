"""Time the shipped `sorting.sort` and write an HTML report to site/index.html.

This report is what CI deploys to GitHub Pages.
"""

import os
import random
import time
from datetime import UTC, datetime
from pathlib import Path

from sorting import sort

SIZES = [100, 1_000, 2_000, 5_000]
OUT = Path("site/index.html")


def main():
    rows = []
    for n in SIZES:
        data = [random.randint(0, n) for _ in range(n)]
        start = time.perf_counter()
        result = sort(data)
        elapsed_ms = (time.perf_counter() - start) * 1000
        status = "✅" if result == sorted(data) else "❌"
        cells = [f"{n:,}", f"{elapsed_ms:.1f} ms", status]
        rows.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
        print(f"n={n:>6,}  {elapsed_ms:8.1f} ms  {status}")

    commit = os.environ.get("GITHUB_SHA", "local")[:7]
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sorting Benchmarks</title>
<style>
body {{ font-family: system-ui, sans-serif; max-width: 640px;
        margin: 2rem auto; padding: 0 1rem; }}
table {{ border-collapse: collapse; width: 100%; }}
td, th {{ border: 1px solid #ccc; padding: .4rem .6rem; text-align: left; }}
</style></head><body>
<h1>Sorting Benchmarks</h1>
<p>Shipped implementation: <code>{sort.__name__}</code><br>
Commit <code>{commit}</code> · built {datetime.now(UTC):%Y-%m-%d %H:%M} UTC</p>
<table><tr><th>n</th><th>time</th><th>correct</th></tr>
{"".join(rows)}
</table></body></html>
"""
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
