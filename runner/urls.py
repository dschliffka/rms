from django.conf.urls import url
from . import views

app_name = 'runner'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
