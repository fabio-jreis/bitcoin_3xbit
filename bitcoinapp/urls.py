# howdy/urls.py
from django.conf.urls import url
from bitcoinapp import views
from bitcoinapp import api


urlpatterns = [
    url(r'^$', api.getIp, name='getIp'),
    url(r'^new_wallet_deposit/$', api.newWallet),
    url(r'^step_02/$', api.getDepositWallet),
    url(r'^send_btc/$', api.send_btc),
    url(r'^details_deposit/$', api.addr_details),
    
    url(r'^new_wallet/$', api.newWallet),
    #url(r'^step_02/$', views.step02PageView.as_view()),
    #url(r'^step_03/$', views.step03PageView.as_view()),
    url(r'^faucet/$', api.send_faucet),
    url(r'^details/$', api.addr_details)
    
    #url(r'^teste/$', api.teste, name='teste')
    #url(r'^$', views.HomePageView.as_view()),
    #url(r'^about/$', views.AboutPageView.as_view()),
    #url(r'replace/$', views.replace, name='replace'),
]