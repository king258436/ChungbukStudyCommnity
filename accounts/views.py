from django.shortcuts import render,redirect
from .models import User
from .loginfunc import *

def Register(request):
    if request.method == 'POST':
        userInfo = User()
        userInfo.age = 0
        userInfo.name = request.POST['name']
        userInfo.user_id = request.POST['user_id']
        userInfo.email = request.POST['email']
        pw = request.POST['user_pw']
        result = CheckValid(pw)
        if result == 2:
            tmp = Encryption(pw)
            userInfo.user_pw = tmp + (15 - len(tmp))*'0'
            userInfo.save()
        elif result == 1:
            pass
        else:
            pass
    return render(request, 'accounts/Register.html')

def Login(request):
    if request.method == 'LOGIN':
        tmp_id = request.LOGIN['id']
        tmp_pw = request.LOGIN['pw']
        if not CheckValidID(tmp_id):
            #Checking that Id is in the DB
            pass
        elif not CheckValidPW(tmp_id,tmp_pw):
            #Checking that PW is wrong or PW is not match with id 
            pass
        else:
            #success
            pass
    return render(request, 'accounts/login.html')
