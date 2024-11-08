"""
URL configuration for bloom project.

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
from django.urls import include, path
from profiles import views
from register import views as reg
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView


def redirect_if_logged_in(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_if_logged_in(views.home), name='home'),  # Перенаправлення з головної сторінки
    path('partners/', include('partners.urls')),
    path('sign-up/', redirect_if_logged_in(reg.sign_up_view), name='sign_up'),
    path('login/', redirect_if_logged_in(views.login_view), name='login'),
    path('info/', views.info_view, name='info'),
    path('statistics/', views.statistics, name='statistics'),
    path('settings/', include('profiles.urls')),
    path('homepage/', include('usertasks.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

