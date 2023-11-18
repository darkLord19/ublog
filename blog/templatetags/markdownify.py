from django import template
import mistune

register = template.Library()


@register.filter
def markdown(value):
    markdown = mistune.create_markdown()
    return markdown(value)
