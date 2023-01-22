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

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = '메세지글자수'
