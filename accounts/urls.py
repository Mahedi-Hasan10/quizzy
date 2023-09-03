from django.urls import path
from accounts.views import signin,register,user_logout,profile
urlpatterns = [
    path('login/',signin,name='login'),
    path('logout/',user_logout,name='logout'),
    path('register/',register,name='register'),
    path('profile/',profile,name='profile'),
]
