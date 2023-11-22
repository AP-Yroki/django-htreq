"""
URL configuration for htreq project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from req import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),

    path('error/', views.error, name='error'),
    re_path(r'^user/(?P<login>\w+)/(?P<floder>\w+)/(?P<post_number>\d+)/$', views.user, name='user'),
    re_path(r'^user/$', views.user, {'login': 'Unknown', 'floder': 'unknown_floder', 'post_number': 0}, name='user_default'),
]
