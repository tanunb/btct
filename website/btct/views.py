# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic import View
from django.template import loader
from .models import Article

# Create your views here.
def index(request):
	all_article = Article.objects.all()
	template = loader.get_template('btct/index.html')
	context = {
		'all_article': all_article,
	}
	return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
	template_name = 'btct/base.html'
	context_object_name = 'all_article'

	def get_queryset(self):
		return Article.objects.all()

class ArticleCreate(CreateView):
	model = Article
	fields = ['topic', 'date', 'content']

class ArticleUpdate(UpdateView):
    model = Article
    fields = ['topic', 'date', 'content']   

# class ArticleDelete(DeleteView):
# 	model = Article
# 	success_url = reverse_lazy('btct:index')    