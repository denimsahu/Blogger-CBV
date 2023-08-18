from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=5000)
    username=models.CharField(max_length=40)
    date_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + " " + self.title
