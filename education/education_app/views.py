from django.shortcuts import get_object_or_404, render
from .models import StudyField, Teachers
from django.views.generic import ListView



class Standarts(ListView):
    model = StudyField
    template_name = 'list_of_areas.html'
    extra_context = {'title':'Направления'}


def teacher_post(request, post_slug):
    post = get_object_or_404(Teachers,slug=post_slug)
    context = {
        'title':'Профиль',
        'post': post
    }
    return render(request,'teacher.html',context=context)


def area_post(request, ed_slug):
    study = get_object_or_404(StudyField,slug=ed_slug)
    context = {
        'title':'Направление',
        'study': study
    }
    return render(request,'area.html',context=context)


def teachers(request):
    return render(request,'list_of_teachers.html', context={'title':'Преподаватели'})


# def standarts(request):
#     return render(request,'list_of_areas.html', context={'title':'Направления'})


def about(request):
    return render(request,'about.html',context={'title':'Информация',})
