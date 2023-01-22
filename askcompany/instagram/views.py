# Create your views here.
from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    # q라는 인자가 있으면 가져온다. 없으면 none을 반환
    print('리퀘스트', request)
    q = request.GET.get('q', '')
    print('q', q)
    if q:
        print('실행됐노')
        qs = qs.filter(message__icontains=q)
        # instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })
