from django import template

register = template.Library()

@register.filter(name='is_reserved')
def is_reserved(selected_movie, seat):
    row, col = seat[0], seat[1:]
    try:
        col = int(col)
    except ValueError:
        return False
    return selected_movie.booked_seats.filter(row=row, col=col).exists()