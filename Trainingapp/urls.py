from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views

app_name='Trainingapp'

urlpatterns = [

    url(r'^home/$',views.home,name='home'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$',views.logout,name='logout'),
    # url(r'^login/$','django.contrib.auth.views.login',name='login'),
    # url(r'^logout/$',auth_views.logout,{'next_page': 'login'},name='logout'),

]