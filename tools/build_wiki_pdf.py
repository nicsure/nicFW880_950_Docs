#!/usr/bin/env python3
"""Build a portable PDF edition of the RMS880/950 Markdown wiki.

This intentionally uses only the Python standard library so that the checked-in
PDF can be regenerated in a minimal checkout without requiring a browser,
Pandoc, or a TeX installation.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path


PAGE_WIDTH, PAGE_HEIGHT = 595, 842  # A4, in PDF points
LEFT, RIGHT, TOP, BOTTOM = 48, 48, 54, 46
LINE_HEIGHT = 13
WIKI_URL = "https://github.com/nicsure/RMS880/wiki"


def pdf_text(value: str) -> str:
    """Return text that is safe for the built-in PDF Type 1 fonts."""
    replacements = {"→": " -> ", "–": "-", "—": "-", "⚠": "Warning:"}
    for source, target in replacements.items():
        value = value.replace(source, target)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "replace").decode()
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def plain_text(value: str) -> str:
    """Remove the Markdown markup while retaining the readable link label."""
    value = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = re.sub(r"(\*\*|__|\*|_)", "", value)
    value = re.sub(r"<[^>]+>", "", value)
    return re.sub(r"\s+", " ", value).strip()


def wrap(value: str, size: int, available: int) -> list[str]:
    """Wrap approximately: Helvetica averages about 0.52 em per character."""
    maximum = max(12, int(available / (size * 0.52)))
    words = value.split()
    lines: list[str] = []
    line = ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if len(candidate) <= maximum or not line:
            line = candidate
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines or [""]


@dataclass
class Page:
    commands: list[str] = field(default_factory=list)
    y: float = PAGE_HEIGHT - TOP
    chapter: str = ""


class Document:
    def __init__(self) -> None:
        self.pages = [Page()]

    @property
    def page(self) -> Page:
        return self.pages[-1]

    def new_page(self, chapter: str = "") -> None:
        self.pages.append(Page(chapter=chapter))

    def ensure(self, height: float, chapter: str) -> None:
        if self.page.y - height < BOTTOM:
            self.new_page(chapter)

    def line(self, text: str, size: int = 10, indent: int = 0, font: str = "F1", chapter: str = "") -> None:
        self.ensure(LINE_HEIGHT * (size / 10) + 2, chapter)
        x = LEFT + indent
        self.page.commands.append(f"BT /{font} {size} Tf {x:.1f} {self.page.y:.1f} Td ({pdf_text(text)}) Tj ET")
        self.page.y -= LINE_HEIGHT * (size / 10)

    def paragraph(self, text: str, size: int = 10, indent: int = 0, font: str = "F1", chapter: str = "") -> None:
        for line in wrap(text, size, PAGE_WIDTH - LEFT - RIGHT - indent):
            self.line(line, size, indent, font, chapter)
        self.page.y -= 3

    def heading(self, text: str, level: int, chapter: str) -> None:
        size = {1: 20, 2: 16, 3: 13, 4: 11}.get(level, 10)
        self.ensure(size * 1.8, chapter)
        self.page.y -= 4
        self.paragraph(text, size, 0, "F2", chapter)
        self.page.y -= 3

    def rule(self, chapter: str) -> None:
        self.ensure(12, chapter)
        y = self.page.y
        self.page.commands.append(f"0.55 w {LEFT} {y:.1f} m {PAGE_WIDTH - RIGHT} {y:.1f} l S")
        self.page.y -= 10

    def table(self, rows: list[list[str]], chapter: str) -> None:
        if not rows:
            return
        columns = max(len(row) for row in rows)
        width = (PAGE_WIDTH - LEFT - RIGHT) / columns
        for row_index, row in enumerate(rows):
            cells = [plain_text(cell) for cell in row] + [""] * (columns - len(row))
            cell_lines = [wrap(cell, 8, int(width - 8)) for cell in cells]
            height = max(len(lines) for lines in cell_lines) * 10 + 7
            self.ensure(height, chapter)
            y_top = self.page.y
            for column, lines in enumerate(cell_lines):
                x = LEFT + column * width + 4
                for index, line in enumerate(lines):
                    font = "F2" if row_index == 0 else "F1"
                    self.page.commands.append(f"BT /{font} 8 Tf {x:.1f} {y_top - 10 - index * 10:.1f} Td ({pdf_text(line)}) Tj ET")
            self.page.commands.append(f"0.3 w {LEFT} {y_top:.1f} m {PAGE_WIDTH - RIGHT} {y_top:.1f} l S")
            for column in range(columns + 1):
                x = LEFT + column * width
                self.page.commands.append(f"{x:.1f} {y_top:.1f} m {x:.1f} {y_top - height:.1f} l S")
            self.page.y -= height
        self.page.commands.append(f"0.3 w {LEFT} {self.page.y:.1f} m {PAGE_WIDTH - RIGHT} {self.page.y:.1f} l S")
        self.page.y -= 7


def parse_table(lines: list[str]) -> list[list[str]]:
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows


def render_page(document: Document, path: Path) -> None:
    chapter = path.stem.replace("-", " ")
    lines = path.read_text(encoding="utf-8").splitlines()
    document.new_page(chapter)
    index = 0
    paragraph_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph_lines
        if paragraph_lines:
            document.paragraph(plain_text(" ".join(paragraph_lines)), chapter=chapter)
            paragraph_lines = []

    while index < len(lines):
        line = lines[index]
        if line.startswith("|") and "|" in line[1:]:
            flush_paragraph()
            table_lines = []
            while index < len(lines) and lines[index].startswith("|"):
                table_lines.append(lines[index])
                index += 1
            document.table(parse_table(table_lines), chapter)
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            document.heading(plain_text(heading.group(2)), len(heading.group(1)), chapter)
        elif re.fullmatch(r"\s*(-{3,}|\*{3,}|_{3,})\s*", line):
            flush_paragraph()
            document.rule(chapter)
        elif not line.strip():
            flush_paragraph()
        elif re.match(r"^\s*>\s?", line):
            flush_paragraph()
            document.paragraph(plain_text(re.sub(r"^\s*>\s?", "", line)), 9, 14, "F3", chapter)
        elif match := re.match(r"^(\s*)([-*+] |\d+\. )(.*)$", line):
            flush_paragraph()
            indent = 12 + len(match.group(1))
            marker = "- " if not match.group(2)[0].isdigit() else match.group(2)
            document.paragraph(marker + plain_text(match.group(3)), 10, indent, "F1", chapter)
        else:
            paragraph_lines.append(line.rstrip(" "))
        index += 1

    flush_paragraph()


def source_pages(wiki: Path) -> list[Path]:
    """Use the Home page's navigation order, then include any remaining pages."""
    home = wiki / "Home.md"
    named = {path.stem: path for path in wiki.glob("*.md") if path.name != "_Sidebar.md"}
    ordered = [home]
    for target in re.findall(r"/wiki/([^#)]+)", home.read_text(encoding="utf-8")):
        if target in named and named[target] not in ordered:
            ordered.append(named[target])
    return ordered + sorted((path for path in named.values() if path not in ordered), key=lambda path: path.name)


def write_pdf(document: Document, destination: Path) -> None:
    for number, page in enumerate(document.pages, start=1):
        if page.chapter:
            page.commands.insert(0, f"BT /F1 8 Tf {LEFT} {PAGE_HEIGHT - 30} Td ({pdf_text(page.chapter)}) Tj ET")
        page.commands.append(f"BT /F1 8 Tf {PAGE_WIDTH / 2 - 12:.1f} 28 Td (Page {number}) Tj ET")

    objects = [b"<< /Type /Catalog /Pages 2 0 R /PageMode /UseOutlines >>", None, None, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>", b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>", b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>"]
    page_refs = []
    for page in document.pages:
        content_ref = len(objects) + 1
        content = ("q\n" + "\n".join(page.commands) + "\nQ\n").encode("ascii")
        objects.append(f"<< /Length {len(content)} >>\nstream\n".encode() + content + b"endstream")
        page_ref = len(objects) + 1
        objects.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_WIDTH} {PAGE_HEIGHT}] /Resources << /Font << /F1 4 0 R /F2 5 0 R /F3 6 0 R >> >> /Contents {content_ref} 0 R >>".encode())
        page_refs.append(page_ref)
    objects[1] = ("<< /Type /Pages /Kids [" + " ".join(f"{ref} 0 R" for ref in page_refs) + f"] /Count {len(page_refs)} >>").encode()
    objects[2] = b"<< /Title (RMS880/950 Documentation) /Author (nicFW880 documentation wiki) /Subject (Offline PDF edition) >>"

    output = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for number, obj in enumerate(objects, start=1):
        offsets.append(len(output))
        output.extend(f"{number} 0 obj\n".encode())
        output.extend(obj)
        output.extend(b"\nendobj\n")
    startxref = len(output)
    output.extend(f"xref\n0 {len(objects) + 1}\n0000000000 65535 f\n".encode())
    output.extend(b"".join(f"{offset:010d} 00000 n\n".encode() for offset in offsets[1:]))
    output.extend(f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R /Info 3 0 R >>\nstartxref\n{startxref}\n%%EOF\n".encode())
    destination.write_bytes(output)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wiki", type=Path, default=Path("RMS880.wiki"))
    parser.add_argument("--output", type=Path, default=Path("RMS880_950_Documentation.pdf"))
    args = parser.parse_args()

    document = Document()
    document.heading("RMS880/950 Documentation", 1, "")
    document.paragraph("Offline PDF edition of the nicFW880/950 documentation wiki.", 12)
    document.paragraph(f"Source wiki: {WIKI_URL}", 9)
    document.rule("")
    document.heading("Contents", 2, "")
    pages = source_pages(args.wiki)
    for path in pages:
        title = next((plain_text(line[2:]) for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("# ")), path.stem.replace("-", " "))
        document.paragraph(title, 9, 10)
    for path in pages:
        render_page(document, path)
    write_pdf(document, args.output)
    print(f"Wrote {args.output} with {len(pages)} wiki pages across {len(document.pages)} PDF pages.")


if __name__ == "__main__":
    main()
