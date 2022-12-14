from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogs.urls')),
    path('accounts/', include('allauth.urls')),
    path('c/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),

    
]