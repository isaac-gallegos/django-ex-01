from django.shortcuts import render

# generic views - see more at https://docs.djangoproject.com/en/2.1/ref/class-based-views/
from django.views import generic

from .models import Recruit, Job, RecruitJob

class HomeView(generic.TemplateView):
	template_name = 'index.html'


class RecruitView(generic.DetailView):
	model = Recruit
	template_name = 'recruit.html'

class RecruitListView(generic.ListView):
	model = Recruit
	template_name = 'recruit_list.html'

class JobView(generic.DetailView):
	model = Job
	template_name = 'job.html'

class JobListView(generic.ListView):
	model = Job
	template_name = 'job_list.html'

class RecruitJobListView(generic.ListView):
	model = RecruitJob
	template_name = 'recruit_job_list.html'