from django.urls import path
from .views import signup_view, login_view, home_view, demo_request_view, speak_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    path('demo/', demo_request_view, name='demo'),
    path('home/speak/', speak_view, name='speak'), 
]
