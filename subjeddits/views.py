#from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import generic
from .models import Subjeddit

from posts.models import Post



class SubjedditsIndexView(generic.ListView):
    model = Post
    template_name = 'subjeddits/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Post.objects.filter(subjeddit__title=slug).order_by('-creation_date')
