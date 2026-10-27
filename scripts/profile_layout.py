"""Generate the profile's local vector layout widgets; no network or dependencies."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
PATHS = {
 "code": "m8 7-5 5 5 5m8-10 5 5-5 5m-3-14-2 18",
 "layers": "m12 3 10 5-10 5L2 8Zm-10 10 10 5 10-5M2 12l10 5 10-5",
 "network": "M9 9h6v6H9zM12 2v7m0 6v7M2 12h7m6 0h7M5 5l4 4m6 6 4 4M5 19l4-4m6-6 4-4",
 "layout": "M3 4h18v16H3zM3 9h18M9 9v11",
 "clock": "M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0M12 6v6l4 2",
 "arrow": "M4 12h16m-6-6 6 6-6 6",
}


def main():
    folder = ROOT / "assets/icons"
    folder.mkdir(exist_ok=True)
    for name, path in PATHS.items():
        (folder / f"{name}.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path d="{path}" fill="none" stroke="#8b5cf6" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>\n',encoding="utf-8")
    for lang in ("en", "es"):
        title = "One ecosystem. From intent to delivery." if lang == "en" else "Un ecosistema. De la idea a la entrega."
        subtitle = "Local tools / explicit controls / reproducible checks" if lang == "en" else "Herramientas locales / control explicito / pruebas reproducibles"
        names = [("01", "Rekora", "Context + memory" if lang=="en" else "Contexto + memoria"),
                 ("02", "RepoRinse", "Git + tool policies" if lang=="en" else "Git + politicas"),
                 ("03", "Resolve Forge", "Edit + review" if lang=="en" else "Edicion + revision"),
                 ("04", "Social Forge", "Plan + publish" if lang=="en" else "Planear + publicar"),
                 ("05", "Declara MX", "Documents + calculations" if lang=="en" else "Documentos + calculos"),
                 ("06", "readme-builder", "Design + generate" if lang=="en" else "Disenar + generar")]
        for theme in ("dark", "light"):
            bg, ink, muted, border = ("#0d1117", "#e6edf3", "#9caac0", "#27344c") if theme=="dark" else ("#ffffff", "#172033", "#59677b", "#dce3ee")
            parts=[f'<rect x=".5" y=".5" width="979" height="337" rx="20" fill="{bg}" stroke="{border}"/>',f'<text x="490" y="42" text-anchor="middle" font-size="23" font-weight="700" fill="{ink}">{escape(title)}</text>',f'<text x="490" y="67" text-anchor="middle" font-size="13" fill="{muted}">{escape(subtitle)}</text>']
            for i,(number,name,desc) in enumerate(names):
                x,y=24+(i%3)*318,92+(i//3)*112
                parts += [f'<rect x="{x}" y="{y}" width="296" height="92" rx="13" fill="{bg}" stroke="{border}"/>',f'<text x="{x+16}" y="{y+27}" font-size="11" fill="#8b5cf6" font-weight="700">{number} / BUILDING BLOCK</text>',f'<text x="{x+16}" y="{y+51}" font-size="19" fill="{ink}" font-weight="650">{name}</text>',f'<text x="{x+16}" y="{y+74}" font-size="13" fill="{muted}">{escape(desc)}</text>']
            (ROOT / f"assets/widgets/ecosystem-{lang}-{theme}.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 338" width="980" height="338" role="img" aria-label="'+escape(title)+'"><style>text{font-family:Segoe UI,Arial,sans-serif}</style>'+''.join(parts)+'</svg>\n',encoding="utf-8")
            stages = ["PLAN", "BUILD", "VERIFY", "SHIP"] if lang=="en" else ["PLANEAR", "CONSTRUIR", "VERIFICAR", "ENTREGAR"]
            parts=[f'<rect x=".5" y=".5" width="979" height="119" rx="18" fill="{bg}" stroke="{border}"/>']
            for i,stage in enumerate(stages):
                x=122+i*245
                parts += [f'<circle cx="{x}" cy="38" r="15" fill="{bg}" stroke="#8b5cf6"/>',f'<text x="{x}" y="43" text-anchor="middle" font-size="12" fill="#8b5cf6">0{i+1}</text>',f'<text x="{x}" y="83" text-anchor="middle" font-size="15" font-weight="700" fill="{ink}">{stage}</text>']
                if i<3:parts.append(f'<path d="M{x+28} 38h188" stroke="{border}" stroke-dasharray="4 5"/>')
            (ROOT / f"assets/widgets/workflow-{lang}-{theme}.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 120" width="980" height="120"><style>text{font-family:Segoe UI,Arial,sans-serif}</style>'+''.join(parts)+'</svg>\n',encoding="utf-8")


if __name__ == "__main__":
    main()
