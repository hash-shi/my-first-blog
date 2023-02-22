from django.urls import path
from . import views

urlpatterns = [
	# ルートなしはviews.post_listへ遷移
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),

	path('blog', views.post_list, name='post_list'),
	path('qrPrint', views.qrPrint, name='qrPrint'),
]
