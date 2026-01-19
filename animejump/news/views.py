from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import News
from django.views.generic import DetailView
from django.core.paginator import Paginator
from .forms import AddNews, NewsNotPublished
from django.utils.timezone import now
from django.shortcuts import redirect


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


def add_news(request):
    if request.method == 'POST':
        form = AddNews(request.POST, request.FILES)
        if form.is_valid():
            News.objects.create(title=form.cleaned_data['title'],
                                description=form.cleaned_data['description'],
                                full_text=form.cleaned_data['full_text'],
                                image=form.cleaned_data['image'], )
    form = AddNews()
    return render(request, 'staff/news/add_news.html', {'form': form})


def news_not_published(request):
    news = News.objects.all().filter(published=False)
    paginator = Paginator(news, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'staff/news/news_not_published.html', {'news': page_obj})


def news_edit(request, pk=None):
    news = News.objects.get(pk=pk)
    if request.method == "POST":
        form = NewsNotPublished(request.POST, request.FILES, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.date_time = now()
            news.save()
            return redirect('news_not_published')
    else:
        form = NewsNotPublished(instance=news)
    return render(request, 'staff/news/news_edit.html',
                  {
                      'form': form,
                      'id': news.id
                  })
