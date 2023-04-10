from django.urls import path, include
from . import views

app_name = 'popmania'
urlpatterns = [
    path('', views.index, name='index'),
    path('login_user/', views.login_user,name='login_user'),
    path('authenticate_user/', views.authenticate_user,
    name='authenticate_user'),
    path('register/', views.register,name='register'),
    path('register_user/', views.register_user,
    name='register_user'),
    path('poll/',views.poll, name='poll'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('logout/',views.logout_user,name='logout'),
]
