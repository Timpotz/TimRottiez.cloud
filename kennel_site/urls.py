from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pups import views
from pups.views import home, contact_success


#router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact-success/', views.contact_success, name='contact_success'),
    #path('test-email/', test_email_view),
    path('gallery/', views.gallery_view, name='gallery'),
    path('test-404/', views.trigger_404),
]

handler404='pups.views.custom_404_view'
# Serve uploaded media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])