from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=128)

class Vacancies(Author):
    pass
    # post_title = models.CharField(max_length=128)
    # post_id = models.IntegerField()
    # post_author = models.ManyToManyField(Author, related_name='vacancies')
    # post_date = models.DateField()

class Resumes(Author):
    pass
    # resume_text = models.CharField(max_length=128)
    # resume_id = models.IntegerField()
    # resume_author = models.ManyToManyField(Author, related_name='resumes')
    # resume_date = models.DateField()