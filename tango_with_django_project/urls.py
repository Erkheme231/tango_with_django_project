from django.contrib import admin
from django.urls import path, include
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('rango/', include('rango.urls')),
    path('login/', views.user_login, name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
