from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    COURSE_CHOICES = [
        ('BS-CS', 'BS-CS'),
        ('BS-DS', 'BS-DS'),
        ('BS-IT', 'BS-IT'),
        ('BS-IS', 'BS-IS'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=5, choices=COURSE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
