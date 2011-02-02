from django.conf.urls.defaults import *
from django.contrib import admin
from activitydisplay.views import index

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)

