from django.urls import path
from .views import SubjedditsIndexView
from posts.views import CommentSectionView

app_name = 'j'
urlpatterns = [
    path('<slug:slug>/', SubjedditsIndexView.as_view(), name='index'),
    path('<slug:slug>/comments/<slug:comments_slug>/', CommentSectionView.as_view(), name='comments')
    # important to include as_view(), so that you don't have to deal with parameters in the view
    #HOW TO MAKE IT LOOK LIKE j/thelastofus/comments/<post.title>????????
]
