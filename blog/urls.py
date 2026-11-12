
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

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
    path(
    'post/<int:pk>/comentar/',
    views.CommentCreateView.as_view(),
    name='comment_create'
),
path(
    'login/',
    LoginView.as_view(
        template_name='registration/login.html'
    ),
    name='login'
),

path(
    'logout/',
    LogoutView.as_view(next_page='blog:post_list'),
    name='logout'
),
path(
    'categorias/',
    views.CategoryListView.as_view(),
    name='category_list'
),

path(
    'categorias/<int:pk>/',
    views.CategoryDetailView.as_view(),
    name='category_detail'
),
]
