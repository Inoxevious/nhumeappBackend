"""grabitapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from mush_store.views import index
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
urlpatterns = [
    # path('', include(router.urls)),
    path('', index, name='index'),
    path('mush_store/', include('mush_store.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('products/', include('products.urls')),
    # path('api/', include('api.urls')),
    url(r'api/', include('api.urls')),
    path('o/', include('oauth2_provider.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)