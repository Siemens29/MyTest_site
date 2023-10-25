from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField("Name", max_length=20)
    desc = models.TextField("Description", max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups list"

    def get_absolute_url(selfs):
        return "/groups/"


class User(models.Model):
    username = models.CharField("User Name", max_length=50)
    date_created = models.DateTimeField("Date create", auto_now=True)
    groups = models.ForeignKey(Group, on_delete=models.PROTECT)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users list"

    def get_absolute_url(selfs):
        return "/users/"