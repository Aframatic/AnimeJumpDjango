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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
