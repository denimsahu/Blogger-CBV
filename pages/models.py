from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + " " + self.title
