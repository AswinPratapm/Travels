from . import views
from django.urls import path,include

urlpatterns = [

    path('',views.demo,name='demo'),
    # # path('',views.teamfn,name='deo'),
    # path('operations/', views.operations, name='operations'),

]
