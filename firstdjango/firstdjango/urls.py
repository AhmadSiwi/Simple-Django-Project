from django.conf.urls import include, url
from django.contrib import admin

from inventory import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'firstdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name ='item_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
