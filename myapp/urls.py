from django.urls import  re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.index,name='index'),
    re_path(r'^blog/',views.viewblog,name='blog'),
    re_path('login/',views.signin,name='login'),
    re_path('register/',views.register,name='register'),
    re_path('signout/',views.signout,name='signout'),
    re_path('profile/',views.profile,name='profile'),
    re_path('update', views.update_profile, name='update'),
    re_path('new-camp/', views.postcompany, name='newcampany'),
    re_path('newblog/', views.postblog, name='newblog'),

    re_path(r'^project/(?P<post_id>\d+)?$', views.project, name='project'), 
    re_path(r'^review/(?P<company_id>\d+)?$', views.review, name='review'),
    re_path(r'^singleblog/(?P<blog_id>\d+)?$', views.singleblog, name='singleblog'), 

    # re_path('review/', views.review, name='review'),
    # re_path('review/<int:pk>' , views.review, name='comment'),

 




]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)