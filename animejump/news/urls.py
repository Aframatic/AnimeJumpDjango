from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='news-index'),
    path('<int:pk>', views.NewsDetail.as_view(), name='news_detail'),
    path('staff/add_news/', views.add_news, name='add_news'),
    path('staff/news_not_publish/', views.news_not_published, name='news_not_published'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
