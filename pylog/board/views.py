from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'board/post_list.html', {'posts': posts})
@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment_content = request.POST["comment"]
        Comment.objects.create(
            post=post,
            content=comment_content,
            author=request.user
        )
        return redirect('board:post_detail', post_id=post_id)

    context = {
        "post": post,
        "comments": Comment.objects.filter(post=post)
    }
    return render(request, "board/post_detail.html", context)
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # PostForm에서 데이터를 가져옴
            post.author = request.user      # 현재 로그인된 사용자를 author로 설정
            post.save()                     # 데이터를 DB에 저장
            return redirect(f"/board/{post.id}/")  # 저장된 post의 ID로 리다이렉트
    else:
        form = PostForm()  # GET 요청 시 빈 폼을 전달

    return render(request, 'board/post_create.html', {'form': form})

