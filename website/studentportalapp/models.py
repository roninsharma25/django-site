from django.db import models

class Student(models.Model):
    studentName = models.CharField(max_length = 50)
    studentAge = models.IntegerField(default = 0)

    # Other fields
    # Availability
    # Instructor
    # Tutoring subject

    def __str__(self):
        return self.studentName + " is age " + str(self.studentAge)

    def getName(self):
        return self.studentName
    
    def getAge(self):
        return self.studentAge

