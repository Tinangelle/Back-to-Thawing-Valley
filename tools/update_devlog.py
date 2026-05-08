#!/usr/bin/env python3
import argparse
import html
import re
from pathlib import Path


DATE_RE = re.compile(r"^###\s+\*\*(\d{4}-\d{2}-\d{2})\*\*\s*$")
LANG_MARK = re.compile(r"^@(zh|en|fr)\s*$")

TITLE_RES = {
    "zh": re.compile(r"^####\s+\*\*标题：(.+)\*\*\s*$"),
    "en": re.compile(r"^####\s+\*\*Title:\s*(.+)\*\*\s*$"),
    "fr": re.compile(r"^####\s+\*\*Titre\s*:\s*(.+)\*\*\s*$"),
}

SECTION_RES = {
    "zh": {
        "content": re.compile(r"^\*\s+\*\*内容\*\*：\s*$"),
        "files": re.compile(r"^\*\s+\*\*相关文件\*\*：\s*$"),
    },
    "en": {
        "content": re.compile(r"^\*\s+\*\*Content:\*\*\s*$"),
        "files": re.compile(r"^\*\s+\*\*Related files:\*\*\s*$"),
    },
    "fr": {
        "content": re.compile(r"^\*\s+\*\*Contenu\s*:\*\*\s*$"),
        "files": re.compile(r"^\*\s+\*\*Fichiers\s*:\*\*\s*$"),
    },
}

NOTE_RES = {
    "zh": re.compile(r"^\*\s+\*\*备注\*\*：\s*(.*)$"),
    "en": re.compile(r"^\*\s+\*\*Note:\*\*\s*(.*)$"),
    "fr": re.compile(r"^\*\s+\*\*Remarque\s*:\*\*\s*(.*)$"),
}

CHILD_BULLET_RE = re.compile(r"^\s{2}\*\s+(.*)$")

LABELS = {
    "zh": {"content": "内容", "files": "相关文件", "note": "备注"},
    "en": {"content": "Content", "files": "Related files", "note": "Note"},
    "fr": {"content": "Contenu", "files": "Fichiers", "note": "Remarque"},
}

# Typographic colon after field labels (FR uses a space before colon).
LABEL_SEP = {"zh": "：", "en": ":", "fr": " : "}


def clean_text(text: str) -> str:
    value = text.strip().replace("\\+", "+").replace("\\->", "->").replace("\\_", "_")
    value = value.replace("\\-", "-")
    return value


def inline_format(text: str) -> str:
    escaped = html.escape(clean_text(text))
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    # Markdown-style *phrase* italics after bold pass
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)
    return escaped


def empty_locale():
    return {"title": "", "content": [], "files": [], "note": ""}


def parse_entries(markdown_text: str):
    lines = markdown_text.splitlines()
    entries = []
    current = None
    current_lang = "zh"
    current_section = None

    for raw_line in lines:
        line = raw_line.rstrip()
        date_match = DATE_RE.match(line)
        if date_match:
            if current:
                entries.append(current)
            current = {
                "date": date_match.group(1),
                "locales": {"zh": empty_locale(), "en": empty_locale(), "fr": empty_locale()},
            }
            current_lang = "zh"
            current_section = None
            continue

        lm = LANG_MARK.match(line)
        if current and lm:
            current_lang = lm.group(1)
            current_section = None
            continue

        if not current:
            continue

        loc = current["locales"][current_lang]

        title_res = TITLE_RES.get(current_lang)
        if title_res:
            tm = title_res.match(line)
            if tm:
                loc["title"] = clean_text(tm.group(1))
                continue

        sec_map = SECTION_RES[current_lang]
        matched_sec = False
        for key, rex in sec_map.items():
            if rex.match(line):
                current_section = key
                matched_sec = True
                break
        if matched_sec:
            continue

        note_rx = NOTE_RES[current_lang]
        nm = note_rx.match(line)
        if nm:
            loc["note"] = clean_text(nm.group(1))
            current_section = None
            continue

        child_match = CHILD_BULLET_RE.match(line)
        if child_match and current_section in ("content", "files"):
            loc[current_section].append(clean_text(child_match.group(1)))

    if current:
        entries.append(current)

    entries = [e for e in entries if e["date"] and e["locales"]["zh"]["title"]]
    entries.sort(key=lambda e: e["date"], reverse=True)
    return entries


def build_timeline(entries):
    """Sidebar: one link per year-month (newest post in that month), label YYYY-MM."""
    lines = ["        <ul>"]
    seen_months = set()
    for entry in entries:
        date = entry["date"]
        ym = date[:7]
        if ym in seen_months:
            continue
        seen_months.add(ym)
        lines.append(f'          <li><a href="#post-{date}">{ym}</a></li>')
    lines.append("        </ul>")
    return "\n".join(lines)


def locale_body_html(lang_code: str, loc: dict):
    lbl = LABELS[lang_code]
    lines = []

    if loc["title"]:
        lines.append(f"          <h2>{html.escape(loc['title'])}</h2>")

    if loc["content"]:
        sep = LABEL_SEP[lang_code]
        lines.append(f"          <p><strong>{html.escape(lbl['content'])}{sep}</strong></p>")
        lines.append("          <ul>")
        for item in loc["content"]:
            lines.append(f"            <li>{inline_format(item)}</li>")
        lines.append("          </ul>")

    if loc["files"]:
        sep = LABEL_SEP[lang_code]
        lines.append(f"          <p><strong>{html.escape(lbl['files'])}{sep}</strong></p>")
        lines.append("          <ul>")
        for item in loc["files"]:
            lines.append(f"            <li>{inline_format(item)}</li>")
        lines.append("          </ul>")

    if loc["note"]:
        sep = LABEL_SEP[lang_code]
        lines.append(f"          <p><strong>{html.escape(lbl['note'])}{sep}</strong> {inline_format(loc['note'])}</p>")

    return "\n".join(lines)


def locale_is_populated(loc: dict) -> bool:
    return bool(loc["title"] or loc["content"] or loc["files"] or loc["note"])


def build_post(entry):
    lines = [
        f'        <article class="blog-post" id="post-{entry["date"]}">',
        f'          <time datetime="{entry["date"]}">{entry["date"]}</time>',
    ]
    for code in ("zh", "en", "fr"):
        loc = entry["locales"][code]
        if not locale_is_populated(loc):
            continue
        inner = locale_body_html(code, loc)
        if not inner.strip():
            continue
        lines.append(f'          <div class="devlog-lang" data-devlog-lang="{code}">')
        lines.append(inner)
        lines.append("          </div>")
    lines.append("        </article>")
    return "\n".join(lines)


def build_section(entries):
    timeline_html = build_timeline(entries)
    posts_html = "\n\n".join(build_post(entry) for entry in entries)
    return (
        '    <section class="blog-timeline-layout">\n'
        '      <aside class="blog-timeline">\n'
        '        <h2 data-i18n="timelineTitle">Timeline</h2>\n'
        f"{timeline_html}\n"
        "      </aside>\n\n"
        '      <div class="blog-list">\n'
        f"{posts_html}\n"
        "      </div>\n"
        "    </section>"
    )


def first_preview_line(loc: dict):
    if loc["content"]:
        plain = re.sub(r"\*\*(.+?)\*\*", r"\1", loc["content"][0])
        plain = re.sub(r"\*([^*]+)\*", r"\1", plain)
        return clean_text(plain)
    if loc["note"]:
        return loc["note"]
    return ""


def build_home_preview(entries, limit=3):
    lines = ['      <div class="devlog-preview-list">']
    for entry in entries[:limit]:
        date = entry["date"]
        lines.append('        <article class="devlog-preview-card">')
        lines.append(f'          <p class="devlog-preview-date">{date}</p>')
        for code in ("zh", "en", "fr"):
            loc = entry["locales"][code]
            if not loc["title"] and not first_preview_line(loc):
                continue
            title = html.escape(loc["title"] or "")
            preview = html.escape(first_preview_line(loc))
            lines.append(f'          <div class="devlog-lang" data-devlog-lang="{code}">')
            if title:
                lines.append(f"            <h3>{title}</h3>")
            if preview:
                lines.append(f"            <p>{preview}</p>")
            lines.append("          </div>")
        lines.append(f'          <a href="devlog.html#post-{date}" data-i18n="viewDetails">View details</a>')
        lines.append("        </article>")
    lines.append("      </div>")
    return "\n".join(lines)


def update_devlog_html(devlog_html: str, new_section_html: str):
    section_re = re.compile(
        r'<section class="blog-timeline-layout">.*?</section>',
        re.DOTALL,
    )
    updated, count = section_re.subn(new_section_html.strip(), devlog_html, count=1)
    if count != 1:
        raise RuntimeError("未找到可替换的 blog timeline 区块。")
    return updated


def update_index_html(index_html: str, preview_html: str):
    """Replace the homepage preview list outer div; inner `.devlog-lang` divs must not end the match."""
    start_token = '<div class="devlog-preview-list">'
    anchor_before_more = '<a class="devlog-more-link"'
    si = index_html.find(start_token)
    if si == -1:
        raise RuntimeError("未找到可替换的首页开发日志预览区块（起始标记缺失）。")
    ai = index_html.find(anchor_before_more, si)
    if ai == -1:
        raise RuntimeError("未找到首页 devlog-more-link 锚点。")
    close_pos = index_html.rfind("</div>", si, ai)
    if close_pos == -1:
        raise RuntimeError("未找到 devlog-preview-list 闭合标签。")
    close_end = close_pos + len("</div>")
    updated = index_html[:si] + preview_html.strip() + index_html[close_end:]
    return updated


def main():
    parser = argparse.ArgumentParser(description="从 Markdown 日志生成 devlog.html 文章区块。")
    parser.add_argument("--source", default="devlog-source.md", help="Markdown 日志源文件路径。")
    parser.add_argument("--target", default="devlog.html", help="目标 devlog.html 路径。")
    parser.add_argument("--index", default="index.html", help="首页 index.html 路径（用于更新日志预览）。")
    args = parser.parse_args()

    source_path = Path(args.source)
    target_path = Path(args.target)
    index_path = Path(args.index)

    markdown_text = source_path.read_text(encoding="utf-8")
    target_html = target_path.read_text(encoding="utf-8")
    index_html = index_path.read_text(encoding="utf-8")

    entries = parse_entries(markdown_text)
    if not entries:
        raise RuntimeError("未解析到有效日志，请检查 Markdown 标题格式。")

    section_html = build_section(entries)
    updated_html = update_devlog_html(target_html, section_html)
    preview_html = build_home_preview(entries)
    updated_index_html = update_index_html(index_html, preview_html)
    target_path.write_text(updated_html, encoding="utf-8")
    index_path.write_text(updated_index_html, encoding="utf-8")

    print(f"已更新 {target_path} 与 {index_path}，共写入 {len(entries)} 条日志。")


if __name__ == "__main__":
    main()
