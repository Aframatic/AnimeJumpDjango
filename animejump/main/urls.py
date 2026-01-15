from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('anime/search/', views.SearchResultsView.as_view(), name='search_results'),
    path('anime/filter/', views.index, name='filter'),
    path('anime/tag/<str:tag>', views.index, name='anime_tag'),
    path('anime/order_by/<str:type>', views.index, name='order_by'),
    path('anime/<int:pk>', views.AnimeDetailView.as_view(), name='anime_detail'),
    path('anime/staff/add_anime/', views.add_anime, name='add_anime'),
    path('anime/staff/add_tags/', views.add_tags, name='add_tags'),
    path('anime/staff/delete_tag/', views.delete_tag, name='delete_tag'),
    path('anime/staff/anime_not_published/', views.anime_not_published, name='anime_not_published'),
    path('anime/staff/anime_edit/<int:pk>', views.anime_edit, name='anime_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
