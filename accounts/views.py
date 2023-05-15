from django.shortcuts import render,redirect
from .models import User, Lecture
from .loginfunc import *

idCheckTemp = ''#아이디체크용 전역변수 

#마이 페이지에서 사용할 함수 

def AddLect(request):
    if request.method == 'POST':
        professor = request.POST['professor']
        lect_name = request.POST['lect_name']
        user_id = request.user.user_id
        user = User.objects.get(user_id=user_id)
        lecture = Lecture(professor=professor, lectName=lect_name)
        lecture.save()
        user.lecture_set.add(lecture)
        return redirect('MyPage')
    else:
        return render(request, 'AddLect.html')
        # 강의 추가 기능(?) AddLect.html 템플릿에 추가 필요

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
    if request.method == 'POST':
        userInfo = User()
        userInfo.age = request.POST['age']
        userInfo.name = request.POST['name']
        userInfo.user_id = request.POST['user_id']
        userInfo.email = request.POST['email']
        userInfo.user_pw = request.POST['user_pw']
        tmp = Encryption(userInfo.user_pw)
        userInfo.user_pw = tmp + (15 - len(tmp))*'0'
        userInfo.save()
        return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/SignUp.html') 

#로그인 부분에서 사용할 함수들 

def Login(request):
    if request.method == 'POST':
        tmp_id = request.POST['myid']
        tmp_pw = request.POST['mypw']
        checkObj = User.objects.filter(user_id = tmp_id)
        if not len(checkObj):
            return render(request, 'accounts/login.html')
        elif checkObj[0].user_pw != Encryption(tmp_pw):
            return render(request, 'accounts/login.html')
        else:
            return render(request, '../main/index.html')
    else:
        return render(request, 'accounts/login.html')# 안전하게 통과했으므로 home화면으로 넘어감 


def Home(request):
    return render(request, 'accounts/home.html')

# 마이페이지 함수
def MyPage(request):
    if request.method == 'POST': # 회원 정보 수정
        user_id = request.POST['user_id'] # user_id 값을 가져옴
        user = User.objects.get(user_id=user_id) 
        user.name = request.POST['name']
        user.age = request.POST['age']
        user.email = request.POST['email'] # User 모델에서 user_id값에 해당하는 사용자 정보를 가져옴
        user.save() # 사용자 정보를 사용자가 입력한 값으로 갱신
        return redirect('MyPage') # 변경된 사용자 정보를 저장 후 MyPage로 리디렉션
    else: # 메서드가 POST가 아닐 경우
        user_id = request.user.user_id # 현재 로그인된 사용자의 user_id 값을 가져옴
        user = User.objects.get(user_id=user_id)
        lectures = user.lecture_set.all()
        context = {'user': user, 'lectures' : lectures}
        return render(request, 'MyPage.html', context)
    # 사용자 정보를 MyPage.html 템플릿에 전달
    
def Forget(request):
    return render(request, 'accounts/ps_change.html')


