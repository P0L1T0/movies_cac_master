"""
URL configuration for movies_cac_master project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from core import views as core_views
from catalogue import views as catalogue_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalogue_views.home, name='home'),   #   Las comillas vacias indican que la pagina se encuentra en la raiz -> '/'
    #path('detail/<int:id>', catalogue_views.detail, name='detail'),   #
    path('detail/', catalogue_views.detail, name='detail'),
    path('login/', core_views.login, name='login'),   #
    path('signup/', core_views.signup, name='signup')   #
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)