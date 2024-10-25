# your_app/templatetags/custom_filters.py
from django import template
from khayyam import JalaliDate

register = template.Library()

@register.filter
def to_jalali(date):
    if date:
        return JalaliDate(date).strftime('%d %B %Y')
    return ''
