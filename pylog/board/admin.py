from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # 목록 페이지에 표시할 필드
    search_fields = ('title', 'content')  # 검색 기능 활성화
    inlines = [CommentInline]  # 댓글 관리할 수 있는 인라인 추가

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'content')  # 목록 페이지에 표시할 필드
    search_fields = ('content',)  # 댓글 내용으로 검색 가능

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
