from django.urls import path

from user import views

urlpatterns = [
    path('add_user',views.add_user,name='add_user'),
    path('login_user',views.login_user,name='login_user'),
    path('logout_user',views.logout_user,name='logout_user')
]
