from django.conf.urls import url
from app1 import views

urlpatterns = [
  url('',views.index,name='index'),
]


urlpatterns = [
url('',views.help,name='help'),
]
