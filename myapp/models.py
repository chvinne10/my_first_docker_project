from django.db import models

# Create your models here.
class Student(models.Model):
    studentname = models.CharField(max_length=150)
    rollnumber = models.IntegerField(unique=True,primary_key=True)
    password=models.CharField(max_length=200,null=False)
    def __str__(self):
        return f"{self.studentname},{self.rollnumber}"