from django.db import models


# Create your models here.
class Post(models.Model):
    message = models.TextField()
    # 이미지 라이브러리 pillow 를 설치했음, upload_to 연월일시간분초 까지 가능함.
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d', max_length=200)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return f"Custom 커스텀 Post object({self.id})"
        return self.message

    class Meta:
        ordering = ['-id']

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = '메세지글자수'

class Comment(models.Model):
    # Post하고 관계가 있다는 말임, # post_id 필드가 생성이 된다
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)