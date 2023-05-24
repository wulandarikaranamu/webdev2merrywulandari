from django.contrib import admin
from django.urls import path, include

# from django.http import HttpResponse

# def buku(request):
#     return HttpResponse('Teknik Informatika Unsulbar, Merry Wulandari')

from django.shortcuts import render

def buku(request):
    return render(request,'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',buku)
    # path('registrasi',buku),
]
