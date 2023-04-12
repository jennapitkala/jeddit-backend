from django.urls import path
from .views import SubjedditsIndexView
from posts.views import PostsIndexView

app_name = 'j'
urlpatterns = [
    path('<slug:slug>/', SubjedditsIndexView.as_view(), name='index'),
    path('<slug:slug>/comments/<slug:comments_slug>/', PostsIndexView, name='comments')
    #HOW TO MAKE IT LOOK LIKE j/thelastofus/comments/<post.title>????????
]
