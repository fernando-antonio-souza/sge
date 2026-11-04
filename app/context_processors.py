from pathlib import Path

_CSS = Path(__file__).resolve().parent / "static" / "css" / "sge.css"


def static_versions(request):
    """Versão de statics pela data de modificação do arquivo: qualquer
    edição muda o ?v= e o navegador referca o CSS (cache-busting)."""
    try:
        version = int(_CSS.stat().st_mtime)
    except OSError:
        version = 1
    return {"sge_css_v": version}
