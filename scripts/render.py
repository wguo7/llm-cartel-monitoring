"""Render report/report.md to report/report.html and report/report.pdf (headless Chrome), 11pt, 1-inch margins.

Usage: python scripts/render.py
"""
import pathlib
import re
import subprocess

import markdown

ROOT = pathlib.Path(__file__).resolve().parents[1]
CSS = """
@page { size: Letter; margin: 1in; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 11pt; line-height: 1.35; color: #111; }
h1 { font-size: 17pt; margin: 0 0 6pt; } h2 { font-size: 13pt; margin: 14pt 0 4pt; } h3 { font-size: 11.5pt; margin: 10pt 0 3pt; }
p, li { margin: 0 0 6pt; } img { width: 86%; display: block; margin: 0 auto; } table { border-collapse: collapse; font-size: 7.5pt; width: 100%; }
th, td { border-bottom: 1px solid #ccc; padding: 2px 3px; text-align: left; } h2.refs { page-break-before: auto; }
.float { break-inside: avoid; page-break-inside: avoid; }
"""

md = (ROOT / "report/report.md").read_text()
html = markdown.markdown(md, extensions=["tables"])
# Keep each figure or table on the same page as its caption.
html = re.sub(r"(<p><img [^>]*></p>\s*<p><em>Figure.*?</p>)", r"<div class='float'>\1</div>", html, flags=re.S)
html = re.sub(r"(<p><em>Table.*?</p>\s*<table>.*?</table>)", r"<div class='float'>\1</div>", html, flags=re.S)
html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{html}</body></html>"
out = ROOT / "report/report.html"
out.write_text(html)
chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                f"--print-to-pdf={ROOT / 'report/report.pdf'}", out.as_uri()], check=True, capture_output=True)
print("wrote report/report.html and report/report.pdf")
