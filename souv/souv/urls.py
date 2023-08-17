from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', views.index_map),
    # path('<str:country_name>/', views.country_detail, name='country_detail'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')), 
]
