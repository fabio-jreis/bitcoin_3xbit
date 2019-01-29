# howdy/urls.py
from django.conf.urls import url
from bitcoinapp import views
from bitcoinapp import api
from django.views.decorators.cache import never_cache


urlpatterns = [
    url(r'^$', never_cache(api.init), name='init'),
    url(r'^new_wallet_deposit/$', never_cache(api.newWallet)),
    url(r'^step_02/$', never_cache(api.getDepositWallet)),
    url(r'^send_btc/$', never_cache(api.send_btc)),
    url(r'^details_deposit/$', never_cache(api.addr_details))

]