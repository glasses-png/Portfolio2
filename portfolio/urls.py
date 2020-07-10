from django.conf.urls import url,include
from django.contrib import admin
from charlotte import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',v.index),
]
urlpatterns += staticfiles_urlpatterns()
