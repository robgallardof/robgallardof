"""Build the profile's SVG widgets (light/dark, EN/ES) into assets/widgets/.

- ide-<lang>.svg            : VS Code-style window with the Developer record (static).
- timeline-<lang>-<theme>.svg: work + education timeline (static).
- overview-<lang>-<theme>.svg: live GitHub overview from the REST API (repos, stars, followers,
                               languages, latest projects). Uses GITHUB_TOKEN when present.

Standard library only, so the workflow needs nothing but Python.
Run: python scripts/widgets.py
"""

from __future__ import annotations

import json
import os
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path

USER = "robgallardof"
# Deprecated or meta repositories that should not appear as "latest projects".
HIDDEN = {"robgallardof", "no-ai-couathor"}
OUT = Path(__file__).resolve().parent.parent / "assets" / "widgets"
FONT = '"Segoe UI", -apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif'
MONO = '"Cascadia Code", "JetBrains Mono", Consolas, Menlo, "DejaVu Sans Mono", monospace'
BRAND = '<linearGradient id="brand" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8b5cf6"/><stop offset="1" stop-color="#0ea5e9"/></linearGradient>'

THEMES = {
    "dark": {"bg": "#0d1117", "card": "#121829", "border": "#25304a", "ink": "#e6edf3", "muted": "#8b949e",
             "chip": "rgba(148,163,184,0.12)", "track": "#21283b"},
    "light": {"bg": "#ffffff", "card": "#ffffff", "border": "#d8dee8", "ink": "#0f172a", "muted": "#57606a",
              "chip": "rgba(15,23,42,0.05)", "track": "#eef1f6"},
}

LANG_COLORS = {"TypeScript": "#3178c6", "Python": "#3776ab", "JavaScript": "#f1e05a", "C#": "#9b4f96",
               "Rust": "#dea584", "HTML": "#e34c26", "Shell": "#89e051", "CSS": "#663399", "Kotlin": "#a97bff"}


def frame(width: int, height: int, theme: dict, label: str, body: str, defs: str = "") -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(label)}">
  <defs>{BRAND}{defs}<style>text{{font-family:{FONT};}} .mono{{font-family:{MONO};}}</style></defs>
  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="18" fill="{theme["card"]}" stroke="{theme["border"]}"/>
  <rect x="24" y="0.5" width="96" height="3" rx="1.5" fill="url(#brand)"/>
{body}
</svg>
'''


# ---------------------------------------------------------------- IDE window

IDE_CODE = {
    "en": [
        [("kw", "public sealed record "), ("ty", "Developer")],
        [("p", "{")],
        [("p", "    "), ("kw", "public string "), ("id", "Name"), ("p", "     => "), ("st", '"Roberto Gallardo"'), ("p", ";")],
        [("p", "    "), ("kw", "public string "), ("id", "Role"), ("p", "     => "), ("st", '"Software Architect · Full Stack .NET"'), ("p", ";")],
        [("p", "    "), ("kw", "public string "), ("id", "Location"), ("p", " => "), ("st", '"Guadalajara, Jalisco"'), ("p", ";")],
        [("p", "    "), ("kw", "public string "), ("id", "DotNet"), ("p", "   => "), ("st", '".NET Framework 2.0 → .NET 10 / 11"'), ("p", ";")],
        [("p", "    "), ("kw", "public string"), ("p", "[] "), ("id", "Stack"), ("p", "  => ["), ("st", '"C#"'), ("p", ", "), ("st", '"Rust"'), ("p", ", "), ("st", '"Python"'), ("p", ", "), ("st", '"Vue"'), ("p", ", "), ("st", '"Next.js"'), ("p", "];")],
        [("p", "    "), ("kw", "public string"), ("p", "[] "), ("id", "Loves"), ("p", "  => ["), ("st", '"Clean Architecture"'), ("p", ", "), ("st", '"CI/CD"'), ("p", ", "), ("st", '"AI agents & MCP"'), ("p", "];")],
        [("p", "    "), ("kw", "public int "), ("id", "YearsWithAI"), ("p", " => "), ("nu", "4"), ("p", ";")],
        [("p", "    "), ("cm", "// Code that works is the minimum. Code that's clear is the goal.")],
        [("p", "}")],
    ],
    "es": [
        [("kw", "public sealed record "), ("ty", "Developer")],
        [("p", "{")],
        [("p", "    "), ("kw", "public string "), ("id", "Name"), ("p", "     => "), ("st", '"Roberto Gallardo"'), ("p", ";")],
        [("p", "    "), ("kw", "public string "), ("id", "Role"), ("p", "     => "), ("st", '"Arquitecto de Software · Full Stack .NET"'), ("p", ";")],
        [("p", "    "), ("kw", "public string "), ("id", "Location"), ("p", " => "), ("st", '"Guadalajara, Jalisco"'), ("p", ";")],
        [("p", "    "), ("kw", "public string "), ("id", "DotNet"), ("p", "   => "), ("st", '".NET Framework 2.0 → .NET 10 / 11"'), ("p", ";")],
        [("p", "    "), ("kw", "public string"), ("p", "[] "), ("id", "Stack"), ("p", "  => ["), ("st", '"C#"'), ("p", ", "), ("st", '"Rust"'), ("p", ", "), ("st", '"Python"'), ("p", ", "), ("st", '"Vue"'), ("p", ", "), ("st", '"Next.js"'), ("p", "];")],
        [("p", "    "), ("kw", "public string"), ("p", "[] "), ("id", "Loves"), ("p", "  => ["), ("st", '"Clean Architecture"'), ("p", ", "), ("st", '"CI/CD"'), ("p", ", "), ("st", '"Agentes de IA y MCP"'), ("p", "];")],
        [("p", "    "), ("kw", "public int "), ("id", "YearsWithAI"), ("p", " => "), ("nu", "4"), ("p", ";")],
        [("p", "    "), ("cm", "// Que funcione es lo mínimo. Que se entienda es la meta.")],
        [("p", "}")],
    ],
}

SYNTAX = {"kw": "#569cd6", "ty": "#4ec9b0", "id": "#9cdcfe", "st": "#ce9178", "nu": "#b5cea8", "cm": "#6a9955", "p": "#d4d4d4"}


def ide(lang: str) -> str:
    lines = IDE_CODE[lang]
    w, top, lh = 860, 86, 25
    h = top + lh * len(lines) - 4
    rows = []
    for i, tokens in enumerate(lines):
        y = top + i * lh
        spans = "".join(f'<tspan fill="{SYNTAX[k]}">{escape(t)}</tspan>' for k, t in tokens)
        rows.append(f'<text x="34" y="{y}" text-anchor="end" class="mono" style="font-size:13px" fill="#5a6274">{i + 1}</text>'
                    f'<text x="52" y="{y}" class="mono" style="font-size:14px;white-space:pre" xml:space="preserve">{spans}</text>')
    body = f'''  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="18" fill="#1e1e1e" stroke="#30363d"/>
  <path d="M0.5 18.5a18 18 0 0 1 18-18h{w - 37}a18 18 0 0 1 18 18V44H0.5z" fill="#252526"/>
  <circle cx="24" cy="22" r="6" fill="#ff5f57"/><circle cx="44" cy="22" r="6" fill="#febc2e"/><circle cx="64" cy="22" r="6" fill="#28c840"/>
  <rect x="92" y="10" width="138" height="34" rx="6" fill="#1e1e1e"/>
  <rect x="92" y="10" width="138" height="2" fill="url(#brand)"/>
  <text x="108" y="32" style="font-size:12.5px" fill="#4ec9b0">C#</text>
  <text x="132" y="32" style="font-size:12.5px" fill="#e6edf3">Developer.cs</text>
  <text x="{w - 20}" y="32" text-anchor="end" style="font-size:12px" fill="#8b949e">.NET 11 · UTF-8</text>
  {"".join(rows)}'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Developer.cs">
  <defs>{BRAND}<style>text{{font-family:{FONT};}} .mono{{font-family:{MONO};}}</style></defs>
{body}
</svg>
'''


# ------------------------------------------------------------------- timeline

TIMELINE = {
    "en": {
        "work_title": "Experience", "edu_title": "Education",
        "work": [
            ("2023 — now", "Full Stack .NET Developer", "Global logistics", [".NET 8", "Clean Architecture", "CQRS", "Docker/K8s", "Azure DevOps", "Vue", "MongoDB"]),
            ("2022", ".NET Developer", "Banking", [".NET Framework → .NET 5", "Biometrics", "GCM → FCM", "Kotlin"]),
            ("2019 — 2022", "Developer", "Telecom", ["VB.NET", "C#", "Java", "SQL Server", "SSRS", "Mulesoft"]),
        ],
        "edu": [
            ("2024 — 2025", "Master's Degree in Software Architecture", "Università degli Studi Guglielmo Marconi", ["Taken at AICAD Business School"]),
            ("2015 — 2019", "Bachelor's in Administrative Computer Systems", "Universidad Veracruzana", []),
        ],
    },
    "es": {
        "work_title": "Experiencia", "edu_title": "Formación",
        "work": [
            ("2023 — hoy", "Desarrollador Full Stack .NET", "Logística global", [".NET 8", "Clean Architecture", "CQRS", "Docker/K8s", "Azure DevOps", "Vue", "MongoDB"]),
            ("2022", "Desarrollador .NET", "Banca", [".NET Framework → .NET 5", "Biometría", "GCM → FCM", "Kotlin"]),
            ("2019 — 2022", "Desarrollador", "Telecomunicaciones", ["VB.NET", "C#", "Java", "SQL Server", "SSRS", "Mulesoft"]),
        ],
        "edu": [
            ("2024 — 2025", "Maestría en Arquitectura de Software", "Università degli Studi Guglielmo Marconi", ["Cursada en AICAD Business School"]),
            ("2015 — 2019", "Lic. en Sistemas Computacionales Administrativos", "Universidad Veracruzana", []),
        ],
    },
}


def chip_row(x: float, y: float, labels: list[str], theme: dict, max_x: float) -> tuple[str, float]:
    out, cx, cy = [], x, y
    for label in labels:
        w = 14 + len(label) * 6.7
        if cx + w > max_x:
            cx, cy = x, cy + 26
        out.append(f'<rect x="{cx:.1f}" y="{cy}" width="{w:.1f}" height="20" rx="10" fill="{theme["chip"]}" stroke="{theme["border"]}"/>'
                   f'<text x="{cx + w / 2:.1f}" y="{cy + 14}" text-anchor="middle" style="font-size:11.5px;font-weight:600" fill="{theme["ink"]}">{escape(label)}</text>')
        cx += w + 6
    return "".join(out), cy + 20


def column(x: float, width: float, title: str, items, theme: dict) -> tuple[str, float]:
    out = [f'<text x="{x}" y="58" style="font-size:20px;font-weight:800" fill="url(#brand)">{escape(title)}</text>']
    y = 92
    line_x = x + 8
    start_y = y
    for period, role, org, chips in items:
        out.append(f'<circle cx="{line_x}" cy="{y + 6}" r="7" fill="url(#brand)"/><circle cx="{line_x}" cy="{y + 6}" r="3" fill="{theme["card"]}"/>')
        tx = x + 30
        out.append(f'<text x="{tx}" y="{y + 11}" style="font-size:12.5px;font-weight:700;letter-spacing:0.4px" fill="#8b5cf6">{escape(period)}</text>')
        out.append(f'<text x="{tx}" y="{y + 34}" style="font-size:16.5px;font-weight:700" fill="{theme["ink"]}">{escape(role)}</text>')
        out.append(f'<text x="{tx}" y="{y + 55}" style="font-size:13.5px" fill="{theme["muted"]}">{escape(org)}</text>')
        bottom = y + 62
        if chips:
            svg, bottom = chip_row(tx, y + 66, chips, theme, x + width)
            out.append(svg)
        y = bottom + 26
    out.insert(1, f'<rect x="{line_x - 1}" y="{start_y + 6}" width="2" height="{max(0, y - start_y - 40)}" rx="1" fill="{theme["border"]}"/>')
    return "".join(out), y


def timeline(lang: str, theme_name: str) -> str:
    t, theme = TIMELINE[lang], THEMES[theme_name]
    w = 1200
    left, ly = column(36, 560, t["work_title"], t["work"], theme)
    right, ry = column(636, 530, t["edu_title"], t["edu"], theme)
    h = int(max(ly, ry)) + 4
    body = f'  <rect x="610" y="34" width="1" height="{h - 68}" fill="{theme["border"]}"/>\n  {left}\n  {right}'
    return frame(w, h, theme, f'{t["work_title"]} · {t["edu_title"]}', body)


# ------------------------------------------------------------------- overview

OVERVIEW = {
    "en": {"title": "GitHub overview", "repos": "public repos", "years": "years on GitHub", "languages": "languages",
           "langs": "Languages across my repositories", "latest": "Latest projects", "updated": "updated daily by GitHub Actions"},
    "es": {"title": "Resumen de GitHub", "repos": "repos públicos", "years": "años en GitHub", "languages": "lenguajes",
           "langs": "Lenguajes en mis repositorios", "latest": "Proyectos más recientes", "updated": "se actualiza a diario con GitHub Actions"},
}


def api(path: str):
    req = urllib.request.Request(f"https://api.github.com{path}", headers={"Accept": "application/vnd.github+json", "User-Agent": USER})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch() -> dict:
    user = api(f"/users/{USER}")
    repos = [r for r in api(f"/users/{USER}/repos?per_page=100&type=owner") if not r["fork"] and not r["archived"]]
    langs = Counter(r["language"] for r in repos if r["language"])
    latest = sorted((r for r in repos if r["name"] not in HIDDEN), key=lambda r: r["created_at"], reverse=True)[:4]
    years = datetime.now(timezone.utc).year - int(user["created_at"][:4])
    return {
        "repos": user["public_repos"],
        "years": years,
        "languages": len(langs),
        "langs": langs.most_common(6),
        "latest": [(r["name"], r["language"] or "—") for r in latest],
    }


def overview(data: dict, lang: str, theme_name: str) -> str:
    t, theme = OVERVIEW[lang], THEMES[theme_name]
    w, h = 1200, 300
    parts = [f'<text x="36" y="56" style="font-size:20px;font-weight:800" fill="url(#brand)">{escape(t["title"])}</text>',
             f'<text x="{w - 36}" y="56" text-anchor="end" style="font-size:12px" fill="{theme["muted"]}">{escape(t["updated"])}</text>']
    # KPI tiles
    for i, (value, label) in enumerate([(data["repos"], t["repos"]), (data["years"], t["years"]), (data["languages"], t["languages"])]):
        x = 36 + i * 128
        parts.append(f'<rect x="{x}" y="80" width="116" height="92" rx="14" fill="{theme["chip"]}" stroke="{theme["border"]}"/>'
                     f'<text x="{x + 16}" y="128" style="font-size:32px;font-weight:800" fill="url(#brand)">{value}</text>'
                     f'<text x="{x + 16}" y="154" style="font-size:12.5px" fill="{theme["muted"]}">{escape(label)}</text>')
    # Language bar
    total = sum(n for _, n in data["langs"]) or 1
    bx, by, bw = 36, 214, 356
    parts.append(f'<text x="{bx}" y="{by - 12}" style="font-size:13px;font-weight:700" fill="{theme["ink"]}">{escape(t["langs"])}</text>')
    parts.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="10" rx="5" fill="{theme["track"]}"/>')
    cx = bx
    legend = []
    for i, (name, n) in enumerate(data["langs"]):
        seg = bw * n / total
        color = LANG_COLORS.get(name, "#8b5cf6")
        parts.append(f'<rect x="{cx:.1f}" y="{by}" width="{max(seg - 2, 2):.1f}" height="10" rx="3" fill="{color}"/>')
        cx += seg
        lx, ly = bx + (i % 3) * 122, by + 36 + (i // 3) * 22
        legend.append(f'<circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{color}"/>'
                      f'<text x="{lx + 16}" y="{ly}" style="font-size:12.5px" fill="{theme["ink"]}">{escape(name)} <tspan fill="{theme["muted"]}">{round(100 * n / total)}%</tspan></text>')
    parts += legend
    # Latest projects
    px = 450
    parts.append(f'<rect x="{px - 18}" y="80" width="1" height="190" fill="{theme["border"]}"/>')
    parts.append(f'<text x="{px}" y="100" style="font-size:13px;font-weight:700" fill="{theme["ink"]}">{escape(t["latest"])}</text>')
    for i, (name, language) in enumerate(data["latest"]):
        y = 122 + i * 40
        color = LANG_COLORS.get(language, "#8b5cf6")
        parts.append(f'<rect x="{px}" y="{y}" width="714" height="32" rx="10" fill="{theme["chip"]}" stroke="{theme["border"]}"/>'
                     f'<circle cx="{px + 18}" cy="{y + 16}" r="5" fill="{color}"/>'
                     f'<text x="{px + 32}" y="{y + 21}" style="font-size:14px;font-weight:600" fill="{theme["ink"]}">{escape(name)}</text>'
                     f'<text x="{px + 700}" y="{y + 21}" text-anchor="end" style="font-size:12.5px" fill="{theme["muted"]}">{escape(language)}</text>')
    return frame(w, h, theme, t["title"], "  " + "\n  ".join(parts))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    data = fetch()
    for lang in ("en", "es"):
        (OUT / f"ide-{lang}.svg").write_text(ide(lang), encoding="utf-8")
        for theme in THEMES:
            (OUT / f"timeline-{lang}-{theme}.svg").write_text(timeline(lang, theme), encoding="utf-8")
            (OUT / f"overview-{lang}-{theme}.svg").write_text(overview(data, lang, theme), encoding="utf-8")
    print(f"widgets written to {OUT} · repos={data['repos']} years={data['years']} langs={data['langs']}")


if __name__ == "__main__":
    main()
