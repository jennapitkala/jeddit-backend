"""from django.views.generic.list import ListView
from django.views import generic
from .models import Post

  

class PostsIndexView(generic.ListView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'comments_list'
    def get_queryset(self):
        return Post.objects.filter(Post.subjeddit.title == self.slug).order_by('-creation_date')"""
        
        
from django.http import HttpResponse


def PostsIndexView(request, slug, comments_slug):
    return HttpResponse("Hello, world. You're at the posts index / comment section.")



# made some chagnes to make better post commebnts upvoting 