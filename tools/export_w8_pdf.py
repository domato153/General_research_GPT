#!/usr/bin/env python3
"""Render approved W8 Markdown and 26 local SVGs to a faithful Korean A4 PDF.
Use only on the authorized research branch; never mutate FINAL_REPORT.md or main.
"""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import fitz
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "FINAL_REPORT.md"
STYLE = ROOT / "final_pdf_report_style.css"
INSTRUCTIONS = ROOT / "final_pdf_html_formatting_instruction_final.md"
OUT = ROOT / "exports" / "Trump_2026_Midterms_Full_Report_20261012.pdf"
HTML_PATH = ROOT / "exports" / "_pdf_build" / "report.html"
CSS_PATH = HTML_PATH.parent / "report_style.css"
GITHUB_BASE = (
    "https://github.com/domato153/General_research_GPT/blob/"
    "research/20261011-trump-midterms-opinion/"
)


def inner(container, el):
    while el.contents:
        container.append(el.contents[0].extract())


def main():
    for f in (SOURCE, STYLE, INSTRUCTIONS):
        assert f.exists() and f.stat().st_size > 1000, f"Missing source: {f}"
    src = SOURCE.read_text(encoding="utf-8")
    match = re.match(r"^# (.+)$", src, re.M)
    assert match, "Actual report title missing"
    title = match.group(1)
    assert "W8" in src and "A~F" in src
    assert re.search(r"^## 14\. ", src, re.M)
    assert len(src) > 40000, "This is not the full source report"

    renderer = MarkdownIt("default", {"html": False, "linkify": False, "breaks": False})
    soup = BeautifulSoup(renderer.render(src), "html.parser")
    h1 = soup.find("h1")
    assert h1 and h1.get_text(" ", strip=True) == title
    h1.decompose()

    chapter_nodes = [x for x in soup.find_all("h2") if re.match(r"^\d+\.\s", x.get_text(" ", strip=True))]
    chapter_titles = [x.get_text(" ", strip=True) for x in chapter_nodes]
    assert len(chapter_titles) == 14 and all(
        chapter_titles[i].startswith(f"{i+1}. ") for i in range(14)
    ), chapter_titles

    # Preserve source text, lists, tables and literal claims. The embedded
    # Markdown TOC is replaced by a page-linked TOC of the same 14 chapters.
    toc_head = next((x for x in soup.find_all("h2") if x.get_text(" ", strip=True) == "목차"), None)
    if toc_head:
        nxt = toc_head.next_sibling
        while nxt and getattr(nxt, "name", None) in ("ol", "ul", "p"):
            following = nxt.next_sibling
            nxt.extract()
            nxt = following
        toc_head.extract()

    # Replace figure paragraph+following italic caption with one figure without
    # changing image or caption contents.
    md_figs = []
    for img in list(soup.find_all("img")):
        assert img.get("src", "").startswith("assets/"), img
        path = ROOT / img["src"]
        assert path.is_file() and path.suffix.lower() == ".svg", path
        figure = soup.new_tag("figure", attrs={"class": "report-figure"})
        img["loading"] = "eager"
        img.parent.replace_with(figure)
        figure.append(img)
        nexttag = figure.find_next_sibling()
        if nexttag and nexttag.name == "p" and nexttag.find("em"):
            cap = soup.new_tag("figcaption")
            inner(cap, nexttag)
            nexttag.extract()
            figure.append(cap)
        md_figs.append((path, figure))
    assert len(md_figs) == 26, f"Expected 26 original research figures, got {len(md_figs)}"
    assert len(set(p.as_posix() for p, _ in md_figs)) == 26

    # Transform relative source and CSV hyperlinks into persistent GitHub links.
    # SVG sources themselves remain local original assets for vector rendering.
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not href.startswith(("http://", "https://", "#", "mailto:")):
            a["href"] = GITHUB_BASE + href

    for tbl in list(soup.find_all("table")):
        wrap = soup.new_tag("div", attrs={"class": "table-wrap"})
        tbl.wrap(wrap)

    # Transform leading "소결" paragraphs to the template's compact conclusion.
    for p in list(soup.find_all("p")):
        if p.get_text(" ", strip=True).startswith(("소결.", "소결:")) or (
            p.find("strong") and p.find("strong").get_text(" ", strip=True).startswith("소결")
        ):
            p["class"] = list(dict.fromkeys(p.get("class", []) + ["conclusion-box"]))

    # Build semantic sections from the original parsed Markdown DOM, preserving
    # exact order of all claims and subheadings.
    fragment = soup.new_tag("main", attrs={"class": "report-body"})
    sec = None
    for el in list(soup.contents):
        if not getattr(el, "name", None):
            continue
        if el.name == "h2":
            title_txt = el.get_text(" ", strip=True)
            sec = soup.new_tag("section", attrs={"class": "report-section"})
            if title_txt.startswith("14. "):
                sec["class"].extend(["appendix", "appendix-break"])
            m = re.match(r"^(\d+)\.", title_txt)
            if m:
                el["id"] = f"chapter-{int(m.group(1))}"
            elif title_txt.startswith("요약"):
                sec["class"].append("executive")
            else:
                el["id"] = re.sub(r"[^a-z0-9]+", "-", title_txt.lower()).strip("-") or "preface"
            fragment.append(sec)
        if sec is None:
            sec = soup.new_tag("section", attrs={"class": "report-section", "data-intro": "true"})
            fragment.append(sec)
        sec.append(el.extract())

    subtitle = "경제·외교·유권자 연합·의회 경쟁구조 | 2026.10.12 기준"
    cover = f"""
    <section class="cover">
      <div class="cover-edge"></div><div class="cover-orbit cover-orbit-a"></div>
      <div class="cover-orbit cover-orbit-b"></div>
      <div class="cover-top"><div class="cover-brand">GENERAL / RESEARCH</div>
        <div class="cover-top-right">DEEP RESEARCH REPORT<br>2026.10.12</div></div>
      <div class="cover-index">POLITICS &amp; ELECTORAL ANALYSIS</div>
      <div class="cover-middle"><div class="cover-code">W8 / FINAL REPORT <span class="cover-code-rule"></span></div>
        <h1 class="cover-title"><span class="title-ko">{title}</span></h1>
        <div class="cover-subtitle">{subtitle}</div></div>
      <div class="cover-bottom"><div class="cover-bottom-left">W1–W7 + APPROVED A–F
         <span class="accent-pipe">/</span> EXPANDED</div><div>2026 · KOREAN EDITION</div></div>
      <div class="cover-bottom-rule"></div>
    </section>"""
    toc_html = """<section class="toc"><div class="toc-kicker">REPORT NAVIGATION</div>
      <div class="toc-header"><div class="toc-small-num">14</div><div>
      <h2>목차</h2><p class="toc-en">TABLE OF CONTENTS</p></div></div>
      <div class="toc-note"><div class="toc-note-label">REPORT SCOPE</div>
      2026년 10월 12일까지의 조사·검증 자료. 2026년 11월 3일 실제 선거 결과는 미포함.</div>
      <nav class="toc-list">"""
    for i, heading in enumerate(chapter_titles, 1):
        text_name = heading.split(". ", 1)[1]
        toc_html += (
            f'<a class="toc-row" href="#chapter-{i}">'
            f'<span class="toc-num">{i:02d}</span>'
            f'<span class="toc-name">{text_name}</span></a>'
        )
    toc_html += "</nav></section>"

    HTML_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(STYLE, CSS_PATH)
    css = CSS_PATH.read_text(encoding="utf-8")
    css += """
    /* Report-specific editorial metadata; approved baseline CSS remains intact. */
    @page report {
      @top-right { content: "TRUMP 2026  /  MIDTERMS";
        font-family:"Noto Sans CJK KR",sans-serif; font-size:7pt;
        letter-spacing:.065em; color:#677888; padding-top:7mm; }
      @bottom-left { content: "2026.10.12  ·  RESEARCH REPORT";
        font-family:"Noto Sans CJK KR",sans-serif; font-size:7pt;
        color:#677888; padding-bottom:7mm; }
    }
    .cover-title .title-ko { font-size:25pt; line-height:1.32;
      letter-spacing:-.055em; overflow-wrap:break-word; }
    .cover-middle:after { top:124mm; }
    .report-body .report-figure img { max-height: 170mm; width: 100%; object-fit:contain; }
    .report-body .report-figure figcaption { break-before:avoid; }
    .report-section .table-wrap { break-inside:auto; }
    .report-section .table-wrap tr { break-inside:avoid; }
    """
    CSS_PATH.write_text(css, encoding="utf-8")
    # The PDF's base_url is the repository root so original assets resolve.
    # Keep an identical local report_style.css there for the HTML link.
    shutil.copyfile(CSS_PATH, ROOT / "report_style.css")
    document = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8">
      <title>{title}</title>
      <link rel="stylesheet" href="report_style.css"></head><body>
      {cover}{toc_html}{str(fragment)}</body></html>"""
    HTML_PATH.write_text(document, encoding="utf-8")

    # Semantic preflight: every original figure and 14 chapter heading preserved.
    html_soup = BeautifulSoup(document, "html.parser")
    assert len(html_soup.select("main.report-body figure.report-figure")) == 26
    assert len(html_soup.select("main.report-body h2[id^=chapter-]")) == 14
    assert len(html_soup.select("section.toc a.toc-row")) == 14
    images = [im["src"] for im in html_soup.select("main img")]
    assert len(images) == len(set(images)) == 26
    html_tables = len(html_soup.select("main table"))
    raw_tables = len(BeautifulSoup(renderer.render(src), "html.parser").find_all("table"))
    assert html_tables == raw_tables, (html_tables, raw_tables)

    HTML(filename=str(HTML_PATH), base_url=str(ROOT)).write_pdf(str(OUT))

    pdf = fitz.open(OUT)
    text = "\n".join(page.get_text() for page in pdf)
    page_count = len(pdf)
    assert page_count >= 20, page_count
    for heading in chapter_titles:
        assert heading in text or heading.split(". ", 1)[1] in text, f"Missing PDF heading {heading}"
    for idx in range(1, 27):
        assert f"그림 {idx}." in text, f"Missing PDF figure caption {idx}"
    phrases = [
        "민주당 44%", "36%", "2026", "CBO",
        "데이터센터", "재획정", "Siena", "NATO", "ICE",
        "53.4%", "48.1%", "트럼프",
    ]
    absent = [word for word in phrases if word not in text]
    assert not absent, f"Missing key content: {absent}"
    blanks = [
        i+1 for i, page in enumerate(pdf)
        if len(page.get_text().strip()) < 15
    ]
    assert not blanks, f"Blank PDF pages: {blanks}"
    assert len(pdf[0].get_text()) > 60, "Cover title missing"
    assert len(pdf[1].get_text()) > 100, "TOC missing"
    page_texts = [len(p.get_text().strip()) for p in pdf]
    short_pages = [i + 1 for i, n in enumerate(page_texts) if n < 120]
    print(json.dumps({
        "source_bytes": SOURCE.stat().st_size,
        "source_chars": len(src),
        "pdf_bytes": OUT.stat().st_size,
        "pages": page_count,
        "headings": len(chapter_titles),
        "embedded_svg_figure_links": len(md_figs),
        "tables": html_tables,
        "captions_in_pdf": 26,
        "pdf_short_text_pages": short_pages,
        "pdf_path": str(OUT),
        "fonts": sorted({font[3] for p in pdf for font in p.get_fonts(full=True)}),
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
