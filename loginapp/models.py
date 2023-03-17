from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.


class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=200)
    date = models.DateField(("Date"), default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.text
