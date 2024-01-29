from django import template
import locale

register = template.Library()

@register.filter
def format_currency(value):
    try:
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
        return locale.format_string("%.*f", (0, value), grouping=True)
    except (ValueError, TypeError):
        return value