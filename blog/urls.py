
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(
        '',
        views.PostListView.as_view(),
        name='post_list'
    ),

    path(
        'post/<int:pk>/',
        views.PostDetailView.as_view(),
        name='post_detail'
    ),

    path(
        'post/novo/',
        views.PostCreateView.as_view(),
        name='post_create'
    ),

    path(
        'post/<int:pk>/editar/',
        views.PostUpdateView.as_view(),
        name='post_update'
    ),

    path(
        'post/<int:pk>/excluir/',
        views.PostDeleteView.as_view(),
        name='post_delete'
    ),
]
