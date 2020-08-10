from django.urls import path, re_path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    re_path(r'^quicksort/(?P<qs_input>([0-9]+))/$',views.get_qs),
    re_path(r'^permutations/(?P<perm_input>([A-Z]+|[a-z]+|[0-9]+)+)/$',views.get_permutation),
    re_path(r'^test3d/$',views.test_d3,name='test3d')
]