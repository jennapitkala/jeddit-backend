from django.views import generic
from comments.models import CommentModel
from .models import PostModel



class CommentSectionView(generic.ListView):
    model = CommentModel
    template_name = 'posts/detail.html'
    context_object_name = 'comment_list'
    
    def get_queryset(self):
        # Retrieve the values from the URL
        comments_slug = self.kwargs['comments_slug']
        # later you have to filter better. What if two different users have the same post title in the same subjeddit?
        queryset = CommentModel.objects.filter(post__slug=comments_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_slug = self.kwargs['comments_slug']
        post = PostModel.objects.get(slug=post_slug)
        context['post'] = post
        return context