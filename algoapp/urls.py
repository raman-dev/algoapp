from django.urls import path, re_path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    re_path(r'^test3d/$',views.test_d3,name='test3d')
]