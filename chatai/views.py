import time

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from langchain_core.messages import HumanMessage, AIMessage

from .ai_model import get_chat
from .models import User, Chat
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_page(request):
    return render(request, 'index.html')


def signup_page(request):
    error_message = None
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')

        if User.objects.filter(username=username).exists():
            error_message = "Nickname already exists. Please choose a different nickname."
            return render(request, 'signup.html', {'error_message': error_message})

        if password == password2:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                name=name,
                surname=surname,
            )

            user.date_of_birth = date_of_birth
            user.gender = gender
            user.save()

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                error_message = "No User Found !"
        else:
            error_message = "Passwords doesn't match"

    return render(request, 'signup.html', {'error_message': error_message})


def login_page(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            error_message = "Invalid Nickname or Password."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def main_page(request):
    return render(request, 'main-page.html')


@login_required
def chat_page(request):
    messages = Chat.objects.filter(user=request.user)
    return render(request, 'chat-page.html', {'messages': messages})

@login_required
@csrf_exempt
def chat_query(request):
    query = request.POST.get('query')
    messages = Chat.objects.filter(user=request.user).order_by('id')
    history = []
    for message in messages:
        history.append(HumanMessage(
                content=message.user_message
            )
        )
        history.append(
            AIMessage(content=message.ai_message)
        )
    response = get_chat(query, request.user.id, history)
    Chat.objects.create(user=request.user, user_message=query, ai_message=response.content)
    return JsonResponse({"messages": response.content}, status=200)