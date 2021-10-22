from django.urls import path
from .feeds import LatestPostsFeed
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        views.post_detail, 
        name='post_detail'),
    path('<int:post_id>/share/',
         views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', 
         views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
