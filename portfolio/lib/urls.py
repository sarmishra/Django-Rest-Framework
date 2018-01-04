from django.conf.urls import url
from django.conf import settings

from .views import dashboard
from django.conf.urls.static import static
from rest_framework.authtoken import views as rest_framework_views

from django.contrib.auth.views import login as auth_login, logout as auth_logout

urlpatterns = [
    url(r'^login/$', auth_login,{'template_name': 'lib/login.html'}, name='login'),
	url(r'logout/$', auth_logout, {'next_page': '/login'}, name='logout'),
    url(r'dashboard/$', dashboard, name='dashboard' ),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)