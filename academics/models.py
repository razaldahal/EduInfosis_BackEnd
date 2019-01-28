from django.db import models
from main.models import BaseModel

class Course(BaseModel):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    code = models.CharField(max_length=16)
    
    def __str__(self):
        return self.name

class Class(BaseModel):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(max_length=11)
    description = models.TextField()

    def __str__(self):
        return self.name

class Section(BaseModel):
    _class=models.ForeignKey(Class,on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    
    def __str__(self):
        return self.name
class SectionStudent(BaseModel):
    student = models.ForeignKey("student.student",on_delete=models.CASCADE)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    roll_no = models.IntegerField()
