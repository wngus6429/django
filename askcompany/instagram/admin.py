from django.contrib import admin
from .models import Post, Comment
from django.utils.safestring import mark_safe
# Register your models here.

# 1번째 등록방법
# admin.site.register(Post)

# 2번째 등록방법
# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Post, PostAdmin)

# 3번쨰 등록방법 (이진석), 장식하는 방법
@admin.register(Post)  # wrapping, 감싸서 대상 기능을 변경가능
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']  # 링크 클릭을 어느걸로 할건지
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            # mark_safe를 적어야 뒤의 태그가 안전하다 판단해서 이미지를 보여주게 되는거임.
            return mark_safe(f'<img src="{post.photo.url}" style="width:200px; height:200px" />')
        return None

    def message_length(self, post):
        return f"{len(post.message)} 글자"
        # return len(post.message)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass