from django.urls import path
from . import views

urlpatterns = [
	# ルートなしはviews.post_listへ遷移
	path('', views.post_list, name='post_list'),

	path('blog', views.post_list, name='post_list'),
	path('qrPrint', views.qrPrint, name='qrPrint'),
]
