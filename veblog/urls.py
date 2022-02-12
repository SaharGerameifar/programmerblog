"""veblog URL Configuration

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
from django.conf.urls.static import static
from account.views import Login, Register, activate
from veblog import settings
from django.contrib import admin
from django.urls import path, include, re_path
from .views import home, navbar, header, footer, meta_header, about_us
from payment.views import send_request, verify
from article.views import aside

app_name = 'veblog'
urlpatterns = [
    path('', home, name="home"),
    path('about_us/', about_us, name='about_us'),
    path('', include('contactus.urls', namespace='contactus')),
    path('login/', Login.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('register', Register.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('comment/', include('comment.urls')),
    re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    path('navbar', navbar, name="navbar"),
    path('aside', aside, name="aside_partial"),
    path('article/', include('article.urls', namespace='articles')),
    path('account/', include('account.urls', namespace='accounts')),
    path('header', header, name="header"),
    path('footer', footer, name="footer"),
    path('meta_header', meta_header, name="meta_header"),
    path('request/', send_request, name='request'),
    path('verify/', verify, name='verify'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
