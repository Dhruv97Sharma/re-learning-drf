"""drf_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import routers
from basics import views
from snippets import views as snippetviews

router = routers.DefaultRouter()
router.register(r'users', snippetviews.UserViewSet, basename="user")
router.register(r'snippets', snippetviews.SnippetViewSet, basename="snippet")


urlpatterns = [
    path('',include(router.urls)),
    # path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    # path('snippets/', snippetviews.SnippetListAPIView.as_view(), name='snippet-list'),
    # path('snippets/<int:pk>/', snippetviews.SnippetRetrieveAPIView.as_view(), name='snippet-detail'),
    # path('snippets/<int:pk>/highlight/', snippetviews.SnippetHighlight.as_view(), name='snippet-highlight'),
    # path('users/', snippetviews.UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', snippetviews.UserDetail.as_view(), name='user-detail'),
    path('admin/', admin.site.urls),
]