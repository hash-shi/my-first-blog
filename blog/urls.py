from django.urls import path
from . import views

urlpatterns = [
	# ルートなしはviews.post_listへ遷移
	path('', views.post_list, name='post_list'),
]
