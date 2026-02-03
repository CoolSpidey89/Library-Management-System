from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.user:
            user = User.objects.create_user(
                username=self.email,
                password=self.roll_number
            )
            self.user = user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    published_date = models.DateField()
    is_issued = models.BooleanField(default=False)

    issued_to = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    issue_date = models.DateField(null=True, blank=True)

    return_date = models.DateField(null=True, blank=True)
    fine = models.IntegerField(default=0)



    def __str__(self):
        return self.title


