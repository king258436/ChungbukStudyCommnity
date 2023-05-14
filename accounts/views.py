from django.shortcuts import render,redirect
from .models import User, Lecture
from .loginfunc import *

idCheckTemp = ''#아이디체크용 전역변수 

#마이 페이지에서 사용할 함수 

def AddLect(request):
    if request.method == 'AddLect':
        pass

#회원가입 부분에서 사용할 함수들 

def CheckId(request):
    global idCheckTemp
    if request.method == 'CheckID':
        id = request.CheckID['userId']
        if CheckValidId(id):
            idCheckTemp = id
            #괜춘~
        else:
            pass
            #안괜춘~

def Register(request):
    global idCheckTemp
    if request.method == 'REGISTER':
        userInfo = User()
        userInfo.age = request.REGISTER['age']
        userInfo.name = request.REGISTER['name']
        userInfo.user_id = request.REGISTER['user_id']
        userInfo.email = request.REGISTER['email']
        userInfo.user_pw = request.REGISTER['user_pw']
        result = CheckValid(userInfo)
        if idCheckTemp != userInfo.user_id:
            return render(request, 'accounts/SignUp.html')
        elif result == 2:
            tmp = Encryption(userInfo.user_pw)
            userInfo.user_pw = tmp + (15 - len(tmp))*'0'
            userInfo.save()
            return render(request, '../main/index.html')
        elif result == 1:
            return render(request, 'accounts/SignUp.html')
        else:
            return render(request, 'accounts/SignUp.html')
    return render(request, 'accounts/SignUp.html') 

#로그인 부분에서 사용할 함수들 

def Login(request):
    if request.method == 'LOGIN':
        tmp_id = request.LOGIN['id']
        tmp_pw = request.LOGIN['pw']
        checkObj = User.objects.filter(user_id = tmp_id)
        if not len(checkObj):
            return render(request, '../main/index.html')
        elif checkObj[0].user_pw != Encryption(tmp_pw):
            return render(request, '../main/index.html')
        else:
            return render(request, '../main/index.html')
    
    return render(request, 'accounts/login.html')# 안전하게 통과했으므로 home화면으로 넘어감 

def Forget(request):
    return render(request, 'accounts/ps_change.html')

def MyPage(request):
    return render(request, '../main/index.html')
