from django.shortcuts import render
from .models import News
from django.views.generic import DetailView
from django.core.paginator import Paginator


def index(request):
    news = News.objects.all().filter(published=True)
    paginator = Paginator(news, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/news_index.html', {'news': page_obj})


class NewsDetail(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

    def get_queryset(self):
        published = News.objects.filter(published=True)
        return published