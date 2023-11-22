from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path
    ip_user = request.META['REMOTE_ADDR']

    return HttpResponse(f'''
        <p>Хост сервера: {host}</p>
        <p>Информация о браузере клиента: {user_agent}</p>
        <p>IP пользователя: {ip_user}''')

def error(request):
    status_code = 400
    error_message = 'К сожалению произошла ошибка'
    return HttpResponse(error_message, status=status_code)

def user(request, login='Unknown', floder='unknown_floder', post_number=0):
    return HttpResponse(f'''<h2>Логин: {login}</h2>
                            <h2>Имя папки: {floder}</h2>
                            <h2>Номер поста: {post_number}</h2>''')