import markdown2
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="markdown")
def render_markdown(value):
    """Renderiza texto Markdown em HTML.

    safe=True escapa HTML cru na fonte (a resposta vem de um LLM;
    jamais deve executar marcação estrangeira), mas a sintaxe
    Markdown (títulos, listas, código, tabelas) continua viva.
    """
    if not value:
        return ""
    html = markdown2.markdown(
        value,
        safe_mode="escape",
        extras=["fenced-code-blocks", "tables", "strike", "task_list"],
    )
    return mark_safe(html)
