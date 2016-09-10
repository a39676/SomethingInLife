
from django.conf.urls import include, url
from django.contrib import admin
from mysite05.views import hello, current_datetime

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', hello),
    url(r'^time/', current_datetime),
    

]