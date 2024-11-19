from django.db import models

# Create your models here.

class Student(models.Model):

    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    name = models.CharField(max_length=40)
    roll = models.IntegerField(unique=True, null=False)
    city = models.CharField(max_length=40)
    marks = models.IntegerField()
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)    
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name