from django import template

register = template.Library()


@register.filter(name='get_months_for_year')
def get_months_for_year(dictionary, key):
    return dictionary.get(key)


@register.filter(name='get_int_by_month')
def get_int_by_month(m):
    month = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12,
    }
    return month[m]
