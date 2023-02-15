from django.contrib import admin

# Register your models here.
# modelsのPostをimport
from .models import Post

# admin(管理画面)上でPostが開けるように登録する。
admin.site.register(Post)