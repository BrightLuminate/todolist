
from django.contrib import admin
from django.urls import path,include


# 어떤 주소로 요청이 들어오면 요청에 대한 
# 뷰를 매필하는 속성명이 바로 urlpatterns 
# '' 는 127.0.0.1:8000/myapp/ 뒷부분 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/',include('todoapp.urls')),
    
]

