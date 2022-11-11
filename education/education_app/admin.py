from django.contrib import admin
from .models import Teachers,StudyField
from .parse import parse_excel_std_fb,parse_headhunter

class TeachersAdmin(admin.ModelAdmin):
    list_display = ('id','name','post','rating')
    list_display_links = ('name','rating')
    search_fields = ('name','rating')
    prepopulated_fields = {'slug':('name',)}


class StudyFieldAdmin(admin.ModelAdmin):
    fields = ('title','slug','code')
    list_display = ('id','title','code')
    list_display_links = ('title','code')
    search_fields = ('title','code')
    prepopulated_fields = {'slug':('title',)}


    def save_model(self, request, obj, form, change) -> None:
        data = parse_excel_std_fb(obj.title)
        obj.ct_complexity_hard = data['Complexity']['Тяжко идёт']
        obj.ct_complexity_easy = data['Complexity']['Легко']
        obj.ct_mark_3 = data['Rating'][3]
        obj.ct_mark_4 = data['Rating'][4]
        obj.ct_mark_5 = data['Rating'][5]
        obj.ct_practical_yes = data['Practical']['Да']
        obj.ct_practical_no = data['Practical']['Нет']
        obj.ct_jobs_yes = data['Job']['Да']
        obj.ct_jobs_no = data['Job']['Нет']
        obj.ct_students = data['Count']
        data = parse_headhunter(obj.title)
        obj.ct_vacancy = data['count_vacancy']
        obj.min_salary = data['min_salary']
        obj.max_salary = data['max_salary']
        obj.save()



admin.site.register(Teachers,TeachersAdmin)
admin.site.register(StudyField,StudyFieldAdmin)
