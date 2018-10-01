from django import template

register = template.Library()

@register.filter(name='get_months_for_year')
def get_months_for_year(dictionary, key):
    return dictionary.get(key)