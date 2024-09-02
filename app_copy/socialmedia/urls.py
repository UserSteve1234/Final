from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("publications/", publications_view, name='publications_view'),
    path("create_publication/", create_publication_view, name='create_publication_view'),
    path('publication/<int:pk>/update/', update_publication_view, name='update_publication_view'),
    path('publication/<int:pk>/delete/', delete_publication_view, name='delete_publication_view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
