from django import template

register = template.Library()


@register.filter
def format_time(minutes):
    if not minutes:
        return '-'
    if minutes < 59:
        return f"{minutes} мин."
    else:
        hours = minutes // 60
        remaining_minutes = minutes % 60
        if remaining_minutes == 0:
            return f"{hours} ч."
        else:
            return f"{hours} ч. {remaining_minutes} мин."
