"""Extract readable text and metadata from an EPUB using only the stdlib."""
from __future__ import annotations

import json
import re
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET


class TextExtractor(HTMLParser):
    BLOCKS = {"p", "div", "section", "article", "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr", "br"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.ignored = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in {"script", "style", "svg"}:
            self.ignored += 1
        elif tag in self.BLOCKS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "svg"} and self.ignored:
            self.ignored -= 1
        elif tag in self.BLOCKS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.ignored:
            self.parts.append(data)

    def text(self) -> str:
        raw = "".join(self.parts).replace("\u3000", " ")
        lines = [re.sub(r"[\t\r\f\v ]+", " ", line).strip() for line in raw.split("\n")]
        return re.sub(r"\n{3,}", "\n\n", "\n".join(line for line in lines if line)).strip()


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def read_xml(archive: zipfile.ZipFile, name: str) -> ET.Element:
    return ET.fromstring(archive.read(name))


def opf_path(archive: zipfile.ZipFile) -> str:
    root = read_xml(archive, "META-INF/container.xml")
    for node in root.iter():
        if local_name(node.tag) == "rootfile" and node.attrib.get("full-path"):
            return node.attrib["full-path"]
    raise ValueError("EPUB container has no OPF rootfile")


def extract(source: Path, output_dir: Path) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(source) as archive:
        opf_name = opf_path(archive)
        opf = read_xml(archive, opf_name)
        opf_dir = PurePosixPath(opf_name).parent

        metadata: dict[str, str | list[str]] = {}
        for node in opf.iter():
            if local_name(node.tag) == "metadata":
                for child in node:
                    key = local_name(child.tag)
                    if child.text and child.text.strip():
                        value = child.text.strip()
                        if key in metadata:
                            old = metadata[key]
                            metadata[key] = (old if isinstance(old, list) else [old]) + [value]
                        else:
                            metadata[key] = value
                break

        manifest: dict[str, str] = {}
        properties: dict[str, str] = {}
        for node in opf.iter():
            if local_name(node.tag) == "item":
                item_id = node.attrib.get("id")
                href = node.attrib.get("href")
                if item_id and href:
                    manifest[item_id] = href
                    properties[item_id] = node.attrib.get("properties", "")

        spine_ids: list[str] = []
        for node in opf.iter():
            if local_name(node.tag) == "itemref":
                idref = node.attrib.get("idref")
                if idref in manifest:
                    spine_ids.append(idref)
        if not spine_ids:
            spine_ids = [key for key, value in properties.items() if "nav" not in value]

        chapters = []
        text_parts = []
        for index, item_id in enumerate(spine_ids, 1):
            href = manifest[item_id]
            full_path = str(opf_dir / href) if str(opf_dir) != "." else href
            full_path = str(PurePosixPath(full_path))
            try:
                raw = archive.read(full_path)
            except KeyError:
                continue
            if not re.search(r"\.(?:x?html?|xml)$", full_path, re.I):
                continue
            parser = TextExtractor()
            parser.feed(raw.decode("utf-8", errors="replace"))
            text = parser.text()
            if not text:
                continue
            chapters.append({"index": len(chapters) + 1, "id": item_id, "href": full_path, "characters": len(text)})
            text_parts.append(f"\n\n===== EPUB_SPINE_{len(chapters):04d} | {full_path} =====\n\n{text}")

        combined = "".join(text_parts).strip() + "\n"
        (output_dir / "SOURCE.txt").write_text(combined, encoding="utf-8")
        result = {
            "source_file": str(source),
            "opf": opf_name,
            "metadata": metadata,
            "chapters": chapters,
            "characters": len(combined),
        }
        (output_dir / "MANIFEST.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        return result


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python extract_epub.py <input.epub> <output-directory>")
    result = extract(Path(sys.argv[1]), Path(sys.argv[2]))
    print(json.dumps({
        "metadata": result["metadata"],
        "chapters": len(result["chapters"]),
        "characters": result["characters"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
