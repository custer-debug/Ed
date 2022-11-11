from django import template
from education_app.models import *


register = template.Library()


@register.simple_tag()
def get_teachers():
    return Teachers.objects.all()

@register.simple_tag()
def get_areas():
    return StudyField.objects.all()

@register.simple_tag()
def get_menu():
    menu = [
        {'title':'Обзор программ','url_name':'ed'},
        {'title':'Преподаватели','url_name':'teachers'}
    ]
    return menu
