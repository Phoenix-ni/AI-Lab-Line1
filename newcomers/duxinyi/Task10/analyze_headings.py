import markdown
from markdown.extensions.toc import TocExtension
from pathlib import Path
import html

def walk(tokens):
    for t in tokens:
        yield t
        yield from walk(t.get("children", []))

def analyze_headings(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    md = markdown.Markdown(extensions=[TocExtension()])
    md.convert(content)
    return [
        {"level": t["level"], "id": t["id"], "name": html.unescape(t["name"])}
        for t in walk(md.toc_tokens)
    ]