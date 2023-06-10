from django.urls import path
from . import views
from .views import Search
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.listzadan, name='home'),
    path('bilet_1/', views.bilet_1, name='bilet_1'),
    path('search/', Search.as_view(), name='saerch'),
]



