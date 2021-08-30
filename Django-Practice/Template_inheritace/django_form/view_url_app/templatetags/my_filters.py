from django import template


register = template.Library()

def my_filters(value):
    return value + "This is custom filter"

register.filter('custom_filter', my_filters)
