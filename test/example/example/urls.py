from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # comment app
    path('comment/', include('comment.urls')),
    # API urls
    path('api/', include('post.api.urls')),
    path('api/', include('accounts.api.urls')),
    path('api/', include('comment.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('post.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
