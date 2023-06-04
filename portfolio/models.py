from django.db import models

class Introduce(models.Model):
    name = models.CharField(max_length=10, null=False)
    job = models.CharField(max_length=30, null=False)
    aboutMe = models.TextField(null=False)
    address = models.TextField(null=False)
    age = models.IntegerField(null=False)

class Experience(models.Model):
    EXPERIENCE_DIVS_CD = (
        ('E', 'Education'),
        ('P', 'Project'),
        ('S', 'Service')
    )

    strtDate = models.DateField(null=False)
    endDate = models.DateField(null=True)
    experinceDivsCd = models.CharField(max_length=1, choices=EXPERIENCE_DIVS_CD, null=False)
    title = models.CharField(max_length=30, null=False)
    subTitle = models.CharField(max_length=30, null=False)
    content = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=30, null=False)
    proficiency = models.IntegerField(null=False)