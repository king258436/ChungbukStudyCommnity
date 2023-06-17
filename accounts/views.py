from django.contrib.auth import authenticate, login, models
from django.shortcuts import render,redirect
from .models import *
from .forms import *

def SignUp(request):
    if request.method == "POST":
        print("SIBAL")
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            myLect = LectList(username = request.POST.get('username'))
            myLect.save()
            return render(request, 'main/index.html')
        else:
            print(form)
    else:
        print("SIBAL")
        form = UserForm()
    return render(request, 'accounts/SignUp.html', {'form': form})
#마이 페이지에서 사용할 함수 

def Home(request):
    return render(request, 'accounts/index.html')

def MyPage(request):
    if not request.user.is_authenticated: #유효성검사
        return redirect("main:home")
    if request.method == 'POST':
        user = LectList.objects.get(username = request.user.username)
        myLect = user.myLects.all()
        for i in range(0,len(myLect)):
            checkbox = request.POST.get(f'sub{i}')
            if checkbox is not None:
                user.myLects.remove(myLect[i])
        user.save()
    error = 0
    userInfo = request.user
    myLect = []
    try:
        myLect = LectList.objects.get(username = request.user.username)
        myLect = myLect.myLects.all()
        if(len(myLect) == 0):
            error = 1
    except:
        error=1
    return render(request, 'accounts/mypage/MyPage.html', { 'MyLects' : myLect, 'userInfo' : userInfo, 'error' : error})

def InfoChange(request):
    if not request.user.is_authenticated: #유효성검사
        return redirect("main:home")
    error = 0
    warn = ''
    if request.method == "POST":
        user = request.user
        pwd = request.POST.get('user_pw')
        chPwd = request.POST.get('new_user_pw')
        confirmPwd = request.POST.get('new_user_pw_check')
        user = authenticate(username = user.username, password = pwd)
        if user is not None:
            if chPwd==confirmPwd:
                username = request.user.username
                user.set_password(chPwd)
                user.save()
                userdata = authenticate(request, username =username, password = chPwd)
                login(request, userdata)
                return redirect("accounts:MyPage")
            else:
                error=1
                warn = "변경할 비밀번호가 변경할 비밀번호 확인 부분과 일치하지 않습니다. "
        else:
            error=1
            warn = "현재 비밀번호가 일치하지 않습니다."
    return render(request, 'accounts/mypage/MyPageInfoChange.html', {'error' : error, 'warn' : warn})

def ManageSub(request):
    if not request.user.is_authenticated: #유효성검사
        return redirect("main:home")
    lectList = Lecture.objects.all()
    try:#현재 수강중인 강의가 있는가? 또는 처음 이 곳을 방문하는 것인가? 
        myLect = LectList.objects.get(username = request.user.username).myLects
    except:
        myLect = LectList(username = request.user.username)
        myLect.save()
    realLectList = []
    for i in lectList:
        try:
            myLect.get(lectName = i.lectName, professor = i.professor)
        except:
            realLectList.append(i)    
    if request.method == 'POST':
        if 'search_btn' in request.POST: # 검색버튼인경우
            realLectList = []
            search = request.POST.get('search_subject')
            lectList = Lecture.objects.filter(lectName__icontains = search)
            for i in lectList:
                try:
                    myLect.get(lectName = i.lectName, professor = i.professor)    
                except:
                    realLectList.append(i)
        elif 'add_btn' in request.POST:
            user = LectList.objects.get(username = request.user.username)
            for i in range(0,len(realLectList)):
                checkbox = request.POST.get(f'subject{i}')
                if checkbox == '':
                    user.myLects.add(realLectList[i])
            user.save()
            return redirect('accounts:MyPage')
    #추가하기 눌렀을 때 작동하는 파트 
    return render(request, 'accounts/mypage/ManageSub.html', {'lectList' : realLectList})

def Forget(request):
    warn = "일치하는 아이디가 존재하지 않습니다. 다시 입력해주세요."
    error = 0
    if request.method == "POST":
        userName = request.POST.get('username')
        try:
            user = User.objects.get(username = userName) #유효성검사
            url = '/accounts/PsChange/'+userName
            return redirect(url)
        except:
            error=1
    return render(request, 'accounts/Forget.html', {'warning' : warn, 'error' : error})


def PsChange(request,userName):
    user = User.objects.get(username = userName)
    error = 0
    if request.method == 'POST':
        pwd = request.POST.get('pwd')
        pwdConfirm = request.POST.get('pwdConfirm')
        if(pwd!=pwdConfirm):
            error=1
            return render(request, 'accounts/PsChange.html', {'username' : userName, 'error' : error})
        else:
            user.set_password(pwd)
            user.save()
            return render(request, 'accounts/login.html')
    return render(request, 'accounts/PsChange.html', {'username' : userName, 'error' : error})