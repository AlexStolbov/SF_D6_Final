from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post
from .resources import news as type_news


class PostsList(ListView):
    # model = Post
    # ordering = 'created'

    template_name = 'news_all.html'

    context_object_name = 'posts'

    queryset = Post.objects.filter(
        type=type_news
    ).order_by('created')


class NewsDetail(DetailView):
    model = Post

    template_name = 'news.html'

    context_object_name = 'post'

    # Определяет, как будем называть первичный ключ при определении url
    pk_url_kwarg = 'id'
