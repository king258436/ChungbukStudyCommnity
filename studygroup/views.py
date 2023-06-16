from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator

def Main(request):
    studyList = list(study.objects.all())[::-1]
    paginator = Paginator(studyList, 5)
    pageNum = request.GET.get('page')
    pageObj = paginator.get_page(pageNum)
    context = {
        'studyList' : pageObj,
    }
    return render(request, "studygroup/main.html", context)

def Posting(request,studyName):
    isReady = 1
    stu = study.objects.get(title = studyName)
    if request.user.is_authenticated:
        if stu.author == request.user.username:
            myPost = 1
        else:
            myPost = 0
    else:
        myPost = 0
    if stu.tag == "모집 중":
        isReady=0
    else:
        isReady=1
    if request.method == "POST":
        if 'gotoList' in request.POST:
            return redirect('studyGroup:Main')
        elif 'delBtn' in request.POST:
            stu.delete()
            return redirect('studyGroup:Main')
        elif 'changeStat' in request.POST:
            if stu.tag == "모집 중":
                stu.tag = "모집 완료"
                isReady=1
            else:
                stu.tag = "모집 중"
                isReady=0
            stu.save()
    context = {
        'isReady':isReady,
        'studyName':studyName,
        'stu' : stu,
        'myPost' : myPost,
    }
    return render(request, 'studygroup/studypost.html', context)

def NewPosting(request):
    if not request.user.is_authenticated: #유효성검사
        return redirect("studyGroup:Main")
    
    if request.method == 'POST':
        studyInfo = study()
        studyInfo.author = request.user.username
        studyInfo.name = request.POST.get('stdPurpose')
        studyInfo.purpose = request.POST.get('stdPurpose')
        studyInfo.groupNum = request.POST.get('groupNum')
        studyInfo.contents = request.POST.get('content')
        studyInfo.summary = request.POST.get('contentSum')
        studyInfo.title = request.POST.get('stdTitle')
        studyInfo.save()
        return redirect('studyGroup:Main')

    return render(request, 'studygroup/newstudy.html')
