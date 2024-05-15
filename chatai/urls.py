from django.contrib import admin
from django.urls import path
from .views import home_page, login_page, signup_page, logout_view, main_page, chat_page, chat_query

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('main-page/', main_page, name='main'),
    path('chat-ai/', chat_page, name='chat'),
    path('chat-ai/query/', chat_query, name='query'),
]
