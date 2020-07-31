from django.db import models

class Members(models.Model):
    objects = models.Manager()
    memberNo = models.IntegerField(default=0, primary_key=True, auto_created=True)
    memberName = models.CharField(max_length=125)


class Projects(models.Model):
    objects = models.Manager()
    projectNo = models.IntegerField(default=0, primary_key=True, auto_created=True)
    projectName = models.CharField(max_length=125)


class Posts(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=1023)
    date = models.DateTimeField(auto_now=True)
    previous = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank = True)
    media =  models.FileField(upload_to="media", blank=True)
    brach = models.IntegerField(default=0)

    memberNo = models.ForeignKey(Members,on_delete=models.SET_NULL, null = True, blank = True)
    projectNo = models.ForeignKey(Projects,on_delete=models.SET_NULL, null = True, blank = True)