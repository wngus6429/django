"""askcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from django.conf import global_settings
# from askcompany import settings
# 밑에와 같이 적어주면 위에꺼 2개 포함되어짐
from django.conf import settings

urlpatterns = [
    # 장고는 URL Reverse를 적극적으로 사용함
    path('admin/', admin.site.urls), #앞에 주소는 마음대로 바꾸기 가능, 이게 URL Reverse
    path('accounts/', include('accounts.urls')),
    path('blog1/', include('blog1.urls')),
    path('instagram', include('instagram.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        # path에서 debug로 시작되는 주소는 debug_toolbar.urls에서 처리하겠다
        path('__debug__/', include('debug_toolbar.urls')),
    ]
# settings.MEDIA_URL
# settings.MEDIA_ROOT
