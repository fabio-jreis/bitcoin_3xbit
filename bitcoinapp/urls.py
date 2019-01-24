# howdy/urls.py
from django.conf.urls import url
from bitcoinapp import views
from bitcoinapp import api


urlpatterns = [
    url(r'^$', api.getIp, name='getIp'),
    url(r'^new_wallet/$', api.newWallet)
    #url(r'^teste/$', api.teste, name='teste')
    #url(r'^$', views.HomePageView.as_view()),
    #url(r'^about/$', views.AboutPageView.as_view()),
    #url(r'replace/$', views.replace, name='replace'),
]