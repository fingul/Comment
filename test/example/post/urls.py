from django.urls import path, re_path
from post.views import (
        PostListView,
        createpost_view,
        PostDetailView,
        # PostUpdateView,
        )


app_name = 'post'

urlpatterns = [
    path('', PostListView.as_view(), name='postlist'),
    path('createpost/', createpost_view, name='createpost'),
    re_path(r'(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='postdetail'),
]