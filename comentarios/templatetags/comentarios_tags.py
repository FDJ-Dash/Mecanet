from django import template
from ..views import show_preguntas

register = template.Library()


@register.inclusion_tag('comentarios/comentarios.html', takes_context=True)
def show_comentarios(context):
    return show_preguntas()