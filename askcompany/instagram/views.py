# Create your views here.
from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    # q라는 인자가 있으면 가져온다. 없으면 빈문자열을 반환
    q = request.GET.get('q', '')
    print('q', q)
    # 검색어가 없다면 아래가 실행이 되지 않아서 전체가 표시됨
    if q:
        print('실행됐노')
        qs = qs.filter(message__icontains=q)
        # instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })
