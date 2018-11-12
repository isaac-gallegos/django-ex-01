from django.db import models


class Recruit(models.Model):
	fname = models.CharField(max_length=128)
	age = models.IntegerField()

class Job(models.Model):
	title = models.CharField(max_length=45)
	salary = models.IntegerField()

class RecruitJob(models.Model):
	"""An association between recruit and job objects"""
	recruit = models.ForeignKey(Recruit, models.CASCADE)
	job = models.ForeignKey(Job, models.CASCADE)
	preference = models.IntegerField()