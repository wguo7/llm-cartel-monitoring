"""Render report/report.md to report/report.pdf in the official Apart template's format (headless Chrome).

Matches template/template.docx: Letter, 1-inch margins, Old Standard TT (the template's embedded fonts, report/fonts/),
11pt body at 1.15 line spacing, 14pt bold section headings, 13pt bold subsections, and the header block (3pt rule,
centered 20pt bold title, thin rule, author, "With Apart Research", centered "Abstract", abstract block). Spacing matches
scripts/build_docx.py, which fills the template .docx itself.
Usage: python scripts/render_template.py
"""
import pathlib
import html as html_lib
import re
import subprocess

import markdown

ROOT = pathlib.Path(__file__).resolve().parents[1]
CSS = """
@font-face { font-family: 'OST'; src: url('fonts/OldStandardTT-regular.ttf'); }
@font-face { font-family: 'OST'; font-weight: bold; src: url('fonts/OldStandardTT-bold.ttf'); }
@font-face { font-family: 'OST'; font-style: italic; src: url('fonts/OldStandardTT-italic.ttf'); }
@page { size: Letter; margin: 1in; }
body { font-family: 'OST', serif; font-size: 11pt; line-height: 1.15; color: #000; margin: 0; }
.hdr { border-top: 3pt solid #000; margin-bottom: 6pt; }
.hdr .title { font-size: 20pt; font-weight: bold; text-align: center; line-height: 1.0; margin: 10pt 0 10pt; }
.hdr .rule { border-top: 1pt solid #000; }
.hdr .author { text-align: center; margin: 10pt 0 6pt; }
.hdr .with { text-align: center; margin: 0 0 10pt; }
.hdr .abshead { font-size: 14pt; font-weight: bold; text-align: center; margin: 0 0 8pt; }
.hdr .abstract { width: 4.93in; margin: 0 auto 6pt; text-align: justify; }
h2 { font-size: 14pt; font-weight: bold; margin: 12pt 0 4pt; line-height: 1.0; break-after: avoid; }
h3 { font-size: 12pt; font-weight: bold; margin: 8pt 0 4pt; line-height: 1.0; break-after: avoid; }
p { margin: 0 0 8pt; } li { margin: 0 0 3pt; } ul, ol { margin: 0 0 8pt; padding-left: 0.375in; }
img { width: 5.9in; display: block; margin: 4pt auto 2pt; }
p.cap { font-size: 9.5pt; font-style: italic; line-height: 1.1; }
table { border-collapse: collapse; font-size: 7pt; width: 6.5in; margin: 0 auto 4pt; line-height: 1.0; }
td, th { padding: 1.5pt 2pt; text-align: left; vertical-align: top; } td + td { white-space: nowrap; } th { font-weight: bold; border-bottom: 0.75pt solid #999; }
tr:last-child td { border-bottom: 0.75pt solid #999; }
table { break-inside: avoid; } tr { break-inside: avoid; }
caption { caption-side: top; text-align: left; font-size: 9.5pt; font-style: italic; line-height: 1.2; padding-top: 3pt; margin-bottom: 4pt; }  /* line-height 1.0 lets glyph tops paint onto the previous page */
ol.refs li { font-size: 10pt; margin-bottom: 2pt; }
.float { break-inside: avoid; page-break-inside: avoid; display: block; width: 100%; }
"""

md = (ROOT / "report/report.md").read_text()
title = re.search(r"^# (.+)$", md, re.M).group(1)
abstract = re.search(r"## Abstract\n\n(.+?)\n", md, re.S).group(1).strip()
rest = "## " + md.split("## Abstract", 1)[1].split("\n## ", 1)[1]
html = markdown.markdown(rest, extensions=["tables"])
html = re.sub(r"<p><em>((?:Figure|Table) [A-Z]?\d.*?)</em></p>", r"<p class='cap'>\1</p>", html, flags=re.S)
html = re.sub(r"(<p><img [^>]*></p>\s*<p class='cap'>.*?</p>)", r"<div class='float'>\1</div>", html, flags=re.S)
# table captions go inside the table: Chrome otherwise leaves a clipped sliver of a caption block it moves to the next page
html = re.sub(r"<p class='cap'>(Table.*?)</p>\s*<table>", r"<table><caption>\1</caption>", html, flags=re.S)
html = html.replace("<h2>References</h2>\n<ol>", "<h2>References</h2>\n<ol class='refs'>")
hdr = (f"<div class='hdr'><div class='title'>{title}</div><div class='rule'></div>"
       f"<div class='author'>William Guo<br>University of Chicago</div><div class='with'>With<br>Apart Research</div>"
       f"<div class='abshead'>Abstract</div><div class='abstract'>{markdown.markdown(abstract)[3:-4]}</div></div>")
doc = f"<!doctype html><html><head><meta charset='utf-8'><title>{html_lib.escape(title)}</title><style>{CSS}</style></head><body>{hdr}{html}</body></html>"
out = ROOT / "report/report.html"
out.write_text(doc)
chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files",
                f"--print-to-pdf={ROOT / 'report/report.pdf'}", out.as_uri()], check=True, capture_output=True)
print("wrote report/report.html and report/report.pdf")
