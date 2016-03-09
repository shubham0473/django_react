from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^login/$', views.login, name = 'login'),
	url(r'^signUp/$', views.signUp, name = 'signUp'),
	url(r'^forgotPassword/$' , views.forgotPassword, name = 'forgotPassword'),
	url(r'^faculty/$' , views.faculty, name = 'faculty'),
	url(r'^[a-z/]*home/$', views.home , name = 'home'),
	url(r'^profile/$', views.profile , name = 'profile'),
	url(r'^addLecture/$', views.addLecture, name = 'addLecture'),
	url(r'^[a-z]*/listcourses/$', views.listcourses , name = 'listcourses'),
	url(r'^index2/$', views.index2 , name = 'index2'),
	url(r'^allcourses/$', views.allcourses , name = 'allcourses'),
	url(r'^allfacultycourses/$', views.allfacultycourses , name = 'allfacultycourses'),
	url(r'^allstudentcourses/$', views.allstudentcourses , name = 'allstudentcourses'),
	url(r'^listfacultycourses/$', views.listfacultycourses , name = 'listfacultycourses'),
	url(r'^liststudentcourses/$', views.liststudentcourses , name = 'liststudentcourses'),
	url(r'^logout/$', views.logout , name = 'logout'),
    url(r'^$', 'myapp.views.index')]
