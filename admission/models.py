from django.db import models

from main.models import BaseModel
from academics.models import Course
import uuid
from student.models import Student


def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)



class StudentAdmission(BaseModel):
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	admission_date = models.DateTimeField(auto_now_add=True)
	course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
	description = models.CharField(max_length=120)
	#image = models.ImageField("Uploaded image", upload_to=scramble_uploaded_filename)
	