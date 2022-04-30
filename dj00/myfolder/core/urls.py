from django.urls import path
from .views import Homepage
from . import views
urlpatterns = [ 
    path('',Homepage.as_view(), name='index'),
    path('course/',views.GetAllCourseAPIView.as_view()),
    path('example/', views.Example.as_view()),
    path('list/', views.list.as_view(), name='list'),
    path('create/', views.create.as_view(), name='create'),
    path('mycreate/', views.mycreate, name='mycreate'), 
]