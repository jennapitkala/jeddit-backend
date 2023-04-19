from django.views.generic.list import ListView
from django.views import generic

from posts.models import PostModel



class SubjedditsIndexView(generic.ListView):
    model = PostModel
    template_name = 'subjeddits/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return PostModel.objects.filter(subjeddit__title=slug).order_by('-creation_date')
