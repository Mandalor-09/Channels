from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Chat(models.Model):
    content =  models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)