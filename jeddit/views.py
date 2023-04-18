from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import generic

from subjeddits.models import SubjedditModel
from posts.models import PostModel


class IndexView(generic.ListView):
    template_name = 'jeddit/index.html'
    context_object_name = 'subjeddit_list'
    
    def get_queryset(self):
        return SubjedditModel.objects.all().order_by('-creation_date')
    
