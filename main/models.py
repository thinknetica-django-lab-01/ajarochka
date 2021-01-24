from django.db import models
import datetime

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
    email = models.EmailField()

class Post(models.Model):
    post_id = models.IntegerField()
    post_date = models.DateField()
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # def posted_today(self):
    #     return self.post_date.date() == datetime.date.today()

class Vacancies(models.Model):
    vacancies_author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='vacancies')
    vacancy_title = models.CharField(max_length=128)
    vacancy_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class Resumes(models.Model):
    resume_author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='resumes')
    resume_text = models.CharField(max_length=128)
    resume_id = models.ForeignKey(Post, on_delete=models.CASCADE)

