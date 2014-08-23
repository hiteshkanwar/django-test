from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
admin.autodiscover()
from django.views.generic.base import TemplateView


# from post.forms import UserRegistrationForm
# import registration.backends.default.urls as regUrls
# from registration.backends.default.views import RegistrationView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'post.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^facebook/$', 'static.views.facebook'),
    url(r'^twitter/login/$',"static.views.twitter_login", name="twitter_login" ),
    url(r'^twitter/callback/$',"static.views.twitter_callback",name="twitter_callback"),  
    url(r'^userprofile/', include('userprofile.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'static.views.index', name='home'),
    url(r'^category/', include('category.urls')),
    
)
