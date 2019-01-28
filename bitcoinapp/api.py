import requests
import blockcypher
from blockcypher import generate_new_address 
from blockcypher import is_valid_address
from blockcypher import send_faucet_coins
from blockcypher import get_address_details
from blockcypher import simple_spend
from django.shortcuts import render
from django.core.mail import EmailMessage

from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm

blockchainName = 'btc-testnet'
token = settings.TOKEN
privkey = settings.PRIVKEY
_toSendSatoshis = 1
_depositBTC = ""

def getIp(request):
    response = requests.get('http://ip-api.com/json')
    geodata = response.json()
    return render(request, 'index.html', {
        'ip': geodata['query'],
        'country': geodata['country']
    })

def get_hostname(request):
    texto = 'FABIO'
    return render(request, 'index.html', {'result': texto})

def getDepositWallet(request):
    global _depositBTC
    return render(request, 'step2.html', {'gDepositBTC': _depositBTC})    


def newWallet(request):
    try:
        print(_depositBTC)
        resp = generate_new_address(coin_symbol=blockchainName, api_key=token)
        assert is_valid_address(resp['address']), resp

        if resp:
            result = str(resp['address'])
            global _depositBTC
            _depositBTC = result
        else:
            raise Exception('Ocorreu um erro, por favor tente novamente')

    except :
        result = 'Ocorreu um erro, por favor tente novamente'

    return render(request, 'index.html', {'result': result})

def send_faucet(request):
    resp = send_faucet_coins(address_to_fund='C7rHYXAkuk93n2umpgmG96nrwDawyS2SC6', satoshis=100000, api_key=token, coin_symbol=blockchainName)
    return render(request, 'index.html')
    
def addr_details(request):
    try:
        global _depositBTC
        addrObj = get_address_details(_depositBTC, api_key=token, coin_symbol=blockchainName)
    except:
        raise Exception('Ocorreu um erro, por favor tente novamente')

    return render(request, 'step3.html', {'addrObj': addrObj, 'gDepositBTC': _depositBTC})

def send_btc(request):

    email = request.GET["email"]
    global _depositBTC
    if _depositBTC == "":
        return render(request, 'step2.html')

    tx_hash = simple_spend(
                    from_privkey=privkey,
                    to_address=_depositBTC,
                    to_satoshis=_toSendSatoshis,
                    privkey_is_compressed=True,
                    api_key=token,
                    coin_symbol=blockchainName)

    send_mail('Depósito realizado', 'Hash de transação: ' + tx_hash, settings.EMAIL_HOST_USER, [email], fail_silently=False)
    
    return render(request, 'step2.html', {'tx_hash_send': tx_hash, 'email_send': email})
