from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=1023)
    date = models.DateTimeField(auto_now=True)
    previous = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank = True)
    media =  models.FileField(upload_to="media", blank=True)
    def __str__(self):
        return self.title
