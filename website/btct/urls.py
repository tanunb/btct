from django.conf.urls import url
from . import views

app_name = 'btct'

urlpatterns = [
    # /btct/
    url(r'^$', views.index, name = 'index'),
]