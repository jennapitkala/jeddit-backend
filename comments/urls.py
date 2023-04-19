from django.urls import include, path


urlpatterns = [
    path('j/', include('subjeddits.urls')),
]
