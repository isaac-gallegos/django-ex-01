from django.db import models


class Recruit(models.Model):
	fname = models.CharField(max_length=128)
	age = models.IntegerField()

class Job(models.Model):
	title = models.CharField(max_length=45)
	salary = models.IntegerField()