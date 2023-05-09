from django.shortcuts import render, redirect
from .models import Post, Comment

def Bulletinboard(request): #게시판 렌더링 함수
    if request.method == 'POST':   #POST 요청인지 확인, POST 요청이면 새로운 게시물 생성
        postTitle = request.POST.get('title')
        postContent = request.POST.get('content')
        postAuthor = request.POST.get('author')
        postLectName = request.POST.get('lectName') #전달된 데이터 변수에 할당
        postIt = Post.objects.create(
            title=postTitle,
            content=postContent,
            author=postAuthor,
            lectName=postLectName
        ) # 새 postIt 개체를 생성하여 데이터 할당
        return redirect('BulletinBoard') # 사용자를 게시판 페이지로 리디렉션
    
    
    if request.method == 'GET' and 'COMMENT' in request.GET:
        # 메서드가 GET이고, 매개변수에 COMMENT가 있는 경우 새로운 댓글 생성
        commentContent = request.GET.get('COMMENT')
        commentAuthor = request.GET.get('commentAuthor')
        postID = request.GET.get('postID')
        # 전달된 데이터 변수에 할당

        if commentContent and commentAuthor and postID:
        # commentContent, commentAuthor, postID가 모두 존재할경우
            post = Post.objects.get(pk=postID) # 해당 postID에 해당하는 Post 객체를 가져옴
            comment = Comment.objects.create(
                content=commentContent,
                author=commentAuthor
            ) # 새 comment 객체 생성하여 데이터를 할당
            post.comments.add(comment) # post 객체의 comments 필드에 새로운 comment 추가
     
