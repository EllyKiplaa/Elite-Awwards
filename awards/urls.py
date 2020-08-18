from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView,  LogoutView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns=[
    
    url(r'^$', views.index, name='homepage'),
    url('accounts/profile/$', views.myProfile, name='profile'),
    url(r'^search/$', views.search_title, name='search_title'),
    url(r'^details/(\d+)$', views.details, name='details'),
    url(r'^api/profile/$', views.Profile_list.as_view()),
    url(r'^api/projects/$', views.Project_list.as_view()),
    url('accounts/login/',LoginView.as_view(redirect_authenticated_user=True,template_name='accounts/login.html'),name='login'),
    url('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
   
    # url('logout/',LogoutView.as_view(), name='logout'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)