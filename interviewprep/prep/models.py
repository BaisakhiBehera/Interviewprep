# prep/models.py
from django.db import models

class InterviewPrepLink(models.Model):
    TECHNOLOGY_CHOICES = [
        ('js', 'JavaScript'),
        ('python', 'Python'),
        ('java', 'Java'),
        ('react', 'React'),
        ('node', 'Node.js'),
        ('ruby', 'Ruby'),
        # You can add more technologies here
    ]

    EXPERIENCE_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    ]

    technology = models.CharField(max_length=20, choices=TECHNOLOGY_CHOICES)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    url = models.URLField()
