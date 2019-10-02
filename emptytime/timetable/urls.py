from django.urls import path

from . import views

app_name='timetable'

urlpatterns = [
    path('', views.index, name='index'),
    path('clearUser/', views.branchHome, name='branch'),
    path('account/', views.account, name='account'),
    path('account/add/', views.post, name='adduser'),
    path('account/result/', views.result, name='result'),
    path('account/error/', views.error, name='error'),
    path('account/delete/<str:username_text>/', views.delete, name='delete'),
]