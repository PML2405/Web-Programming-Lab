from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    dob = models.DateField()

    def __str__(self):
        return self.name