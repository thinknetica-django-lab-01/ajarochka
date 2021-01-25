from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

TAGS = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
    ('Online', 'Online'),
    ('35-44', '35-44'),
    ('45-54', '45-54'),
    ('55-64', '55-64'),
    ('65+', '65+'),
)
class Author(models.Model):
    user = models.CharField(max_length=128)

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