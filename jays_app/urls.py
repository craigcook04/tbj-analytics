from django.urls import path

from . import views

app_name = 'jays_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.teams, name='teams'),
    path('roster/', views.search, name='search'),
    path('players/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('players/<str:playerId>/', views.players, name='players'),
    path('roster/<str:teamId>/', views.roster, name='roster'),
    path('report/<str:playerId>/', views.generateReport, name='generateReport')

]