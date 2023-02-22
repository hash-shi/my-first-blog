from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):

	#
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

	# post_list.htmlをリダイレクトする(画面表示)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def qrPrint(request):
	return render(request, 'qrPrint/qrPrint.html', {})
