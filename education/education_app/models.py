from django.urls import reverse
from django.db import models



class Teachers(models.Model):
    name = models.CharField(max_length = 255,verbose_name = 'ФИО')
    slug = models.SlugField(max_length =255,unique=True,db_index=True,verbose_name='URL')
    post = models.CharField(max_length = 255,verbose_name = 'Должность')
    photo = models.ImageField(upload_to = 'photos/',verbose_name='Фото')
    rating = models.FloatField(blank=False,verbose_name = 'Рейтинг')
    university = models.CharField(max_length = 255,verbose_name = 'Университет')
    expirience = models.PositiveSmallIntegerField(blank=False,verbose_name = 'Опыт преподавания')
    disciplines = models.TextField(blank=False,verbose_name = 'Преподаваемые дисциплины')
    education = models.TextField(blank=False,verbose_name = 'Образование')
    # awards = models.TextField(blank=False)


    def __str__(self) -> str:
        return self.name


    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug})


    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'







class StudyField(models.Model):
    title = models.CharField(max_length=255,verbose_name = 'Направление')
    slug = models.SlugField(max_length =255,unique=True,db_index=True,verbose_name='URL')
    code = models.CharField(max_length=10,verbose_name = 'Код направления')
    # rating = models.FloatField(blank=False,verbose_name = 'Рейтинг')
    ct_complexity_hard = models.FloatField()
    ct_complexity_easy = models.FloatField()
    ct_mark_3 = models.FloatField()
    ct_mark_4 = models.FloatField()
    ct_mark_5 = models.FloatField()
    ct_practical_yes = models.FloatField()
    ct_practical_no = models.FloatField()
    ct_jobs_yes = models.FloatField()
    ct_jobs_no = models.FloatField()
    ct_students = models.IntegerField()
    ct_vacancy = models.IntegerField()
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()


    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('education',kwargs={'ed_slug':self.slug})

    class Meta:
        verbose_name = 'Государтсвенный стандарт'
        verbose_name_plural = 'Государтсвенные стандарты'
