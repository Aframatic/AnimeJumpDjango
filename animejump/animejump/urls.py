from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('authorization/', include('authorization.urls')),
                  path('', include('main.urls')),
                  path('news/', include('news.urls')),
                  path('random_anime/', include('random_anime.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
