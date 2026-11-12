
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse, reverse_lazy

from .models import Post
from .forms import PostForm


# READ - Listagem de posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


# READ - Detalhes de um post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# CREATE - Criar post
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse(
            'blog:post_detail',
            kwargs={'pk': self.object.pk}
        )


# UPDATE - Editar post
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse(
            'blog:post_detail',
            kwargs={'pk': self.object.pk}
        )


# DELETE - Excluir post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:post_list')
