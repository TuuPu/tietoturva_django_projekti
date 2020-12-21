
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from polls.views import IndexView

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', IndexView.as_view(), name='home'),
    #path('', TemplateView.as_view(template_name='index.html'), name='home'),
    #path('polls/', TemplateView.as_view(template_name='polls/index.html'), name='home'),
]
