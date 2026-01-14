from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('filter/', views.index, name='filter'),
    path('anime/tag/<str:tag>', views.index, name='anime_tag'),
    path('order_by/<str:type>', views.index, name='order_by'),
    path('<int:pk>', views.AnimeDetailView.as_view(), name='anime_detail'),
    path('staff/add_anime/', views.add_anime, name='add_anime'),
    path('staff/add_tags/', views.add_tags, name='add_tags'),
    path('staff/delete_tag/', views.delete_tag, name='delete_tag'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
