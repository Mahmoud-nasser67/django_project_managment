from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
class num_task(models.IntegerChoices):
    PANDING=1,'panding'
    COMPLETE=2,'complete'
    POSTPONED=3,'postponed'
    CANCEL=4,'cancel'

class Progect(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    statues = models.IntegerField(choices=num_task.choices,default=num_task.PANDING)
    create_at=models.DateTimeField(auto_now_add=True)
    updata_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(category,on_delete=models.PROTECT)
    user=models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class task(models.Model):

    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    project = models.ForeignKey(Progect,on_delete=models.CASCADE)

    def __str__(self):
        return self.description




