from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to="static/img/")
    repository = models.URLField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name  # 👈 So the admin panel or templates can show project names clearly
