from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Anime
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator
from taggit.models import Tag
from .forms import AddAnime, TagForm, AnimeNotPublished, UsersPublish
from django.utils.timezone import now
from django.shortcuts import redirect


def index(request, type=None, tag=None):
    anime = Anime.objects.all().order_by('title').filter(published=True)
    filters = request.GET.getlist("tags")
    if tag:
        anime = Anime.objects.filter(tags__name=tag).filter(published=True)
    if filters:
        tags = Tag.objects.filter(name__in=filters)
        id = tags.values_list('id')
        anime = Anime.objects.filter(tags__pk__in=id).distinct().filter(published=True)
    if type:
        if type == 'date':
            anime = Anime.objects.all().order_by('-date_time').filter(published=True)
        if type == 'date_out':
            anime = Anime.objects.all().order_by('-date_out').filter(published=True)
    tags = Tag.objects.all()
    paginator = Paginator(anime, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/index.html', {'anime': page_obj, 'tags': tags})


class SearchResultsView(ListView):
    model = Anime
    template_name = 'main/index.html'
    context_object_name = 'anime'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            anime_result = Anime.objects.filter(title__iregex=query, published=True)
            anime = anime_result
        else:
            anime = None
        return anime


class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'main/anime_detail.html'
    context_object_name = 'anime'

    def get_queryset(self):
        published = Anime.objects.filter(published=True)
        return published


def add_anime(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        filters = request.POST.getlist("tags")
        form = AddAnime(request.POST, request.FILES)
        if form.is_valid():
            anime = Anime.objects.create(title=form.cleaned_data['title'],
                                         description=form.cleaned_data['description'],
                                         episode=form.cleaned_data['episode'],
                                         image=form.cleaned_data['image'], )
            for filter in filters:
                anime.tags.add(filter)
    form = AddAnime()
    return render(request, 'main/staff/anime/add_anime.html', {'tags': tags, 'form': form})


def add_tags(request):
    tags = Tag.objects.all()
    form = TagForm(request.POST)
    if form.is_valid():
        if request.method == 'POST':
            Tag.objects.create(name=form.cleaned_data['tag'])
            return render(request, 'main/staff/add_tags.html', {'tags': tags})
    return render(request, 'main/staff/add_tags.html', {'tags': tags})


def delete_tag(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        id = request.POST.get("tag", False)
        Tag.objects.filter(pk=id).delete()
    return render(request, 'main/staff/add_tags.html', {'tags': tags})


def anime_not_published(request):
    anime = Anime.objects.all().order_by('title').filter(published=False)
    filters = request.GET.getlist("tags")
    if filters:
        tags = Tag.objects.filter(name__in=filters)
        id = tags.values_list('id')
        anime = Anime.objects.filter(tags__pk__in=id).distinct().filter(published=False)
    tags = Tag.objects.all()
    paginator = Paginator(anime, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/staff/anime/anime_not_published.html', {'anime': page_obj, 'tags': tags})


def anime_edit(request, pk=None):
    anime = Anime.objects.get(pk=pk)
    tags = anime.tags.all()
    all_tags = Tag.objects.all()
    anime_tags = []
    no_anime_tags = []
    checked_tags = request.POST.getlist("checked_tags")
    for tag in tags:
        anime_tags.append(tag.name)
    for all_tag in all_tags:
        if all_tag.name in anime_tags:
            continue
        else:
            no_anime_tags.append(all_tag.name)
    if request.method == "POST":
        form = AnimeNotPublished(request.POST, request.FILES, instance=anime)
        if form.is_valid():
            anime = form.save(commit=False)
            anime.author = request.user
            anime.date_time = now()
            anime.save()
            anime.tags.clear()
            for check_tag in checked_tags:
                anime.tags.add(check_tag)
            return redirect('anime_not_published')
    else:
        form = AnimeNotPublished(instance=anime)
    return render(request, 'main/staff/anime/anime_edit.html',
                  {
                      'form': form,
                      'tags': tags,
                      'no_anime_tags': no_anime_tags,
                      'id': anime.id
                  })

# class AnimeListView(ListView):
#     model = Anime
#     template_name = 'main/index.html'
#     context_object_name = 'anime'
#     ordering = 'title'
#     paginate_by = 3
#
#     def get_queryset(self):
#         published = Anime.objects.filter(published=True)
#         return published
#
#
# class OrderBy(ListView):
#     model = Anime
#     template_name = 'main/index.html'
#     context_object_name = 'anime'
#     paginate_by = 3
#
#     def get_queryset(self, **kwargs):
#         anime = Anime.objects.filter(published=True)
#         type = self.kwargs['type']
#         if type:
#             if type == 'date':
#                 anime = Anime.objects.all().order_by('-date_time').filter(published=True)
#             if type == 'date_out':
#                 anime = Anime.objects.all().order_by('-date_out').filter(published=True)
#         return anime
#
#
# class TagsView(ListView):
#     model = Anime
#     template_name = 'main/index.html'
#     context_object_name = 'anime'
#     paginate_by = 3
#
#     def get_queryset(self, **kwargs):
#         anime = Anime.objects.filter(published=True)
#         tag = self.kwargs['tag']
#         if tag:
#             anime = Anime.objects.filter(tags__name=tag)
#         return anime
#
# class FiltersView(ListView):
#     model = Anime
#     template_name = 'main/index.html'
#     context_object_name = 'anime'
#     paginate_by = 3
#
#     def get_queryset(self, **kwargs):
#         anime = Anime.objects.filter(published=True)
#         filters = self.kwargs['filter']
#         if filters:
#             tags = Tag.objects.filter(name__in=filters)
#             id = tags.values_list('id')
#             anime = Anime.objects.filter(tags__pk__in=id).distinct()
#         return anime
