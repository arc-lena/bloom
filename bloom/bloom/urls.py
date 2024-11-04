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
from tasks import views as tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
    path('partners/', include('partners.urls')),
    path('sign-up/', reg.sign_up_view, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('info/', views.info_view, name='info'),
    path("homepage/", tasks.homepage, name="homepage"),
    path('statistics/', views.statistics, name='statistics'),
    path('homepage/', include('usertasks.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)