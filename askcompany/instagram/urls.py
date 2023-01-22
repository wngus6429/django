from django.urls import path
from . import views
urlpatterns = [
    # 아무것도 없는 주소라면 views.post_list 함수 그 자체를 넘김
    path('', views.post_list)
]