from django.shortcuts import render

# Create your views here.

def post_list(request):
	# post_list.htmlをリダイレクトする(画面表示)
	return render(request, 'blog/post_list.html', {})
