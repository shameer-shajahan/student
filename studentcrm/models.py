from django.db import models


# Create your models here.

class Student(models.Model):

    name=models.CharField(max_length=100)

    age=models.PositiveIntegerField()

    standard=models.CharField(max_length=50)

    gender_option=(
        ("male","male"),
        ( "female","female")
    )

    gender=models.CharField(max_length=50, choices=gender_option)


    address=models.TextField()

    mobile=models.CharField(max_length=12)

    email=models.EmailField()

    def __str__(self):
        return self.name

    picture=models.ImageField(upload_to="student_image",null=True)