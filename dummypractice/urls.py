"""dummypractice URL Configuration


"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import  url
from dummyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home),
url(r'^home/',views.base_home),
url(r'^contacts/',views.base_contacts),
url(r'^courses/',views.base_courses),
url(r'^ourteam/',views.base_ourteam),
url(r'^feedback/',views.base_feedback),
url(r'^gallery/',views.base_gallery),

]
