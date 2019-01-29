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
from django.http import HttpResponse

from bitcoinapp.models import Deposits
import random, string

blockchainName = 'btc-testnet'
token = settings.TOKEN
privkey = settings.PRIVKEY
_toSendSatoshis = 1
sessionID = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(64))

def init(request):
    print(sessionID)

    deposits = Deposits.objetos.all()

    if deposits.count() > 0:
        deposits.delete()

    return render(request, 'index.html')

def getDepositWallet(request):
    print(sessionID)
    deposit = Deposits.objetos.filter().first()
    return render(request, 'step2.html', {'gDepositBTC': deposit.address})    


def newWallet(request):
    print(sessionID)
    try:
        resp = generate_new_address(coin_symbol=blockchainName, api_key=token)
        assert is_valid_address(resp['address']), resp

        if resp:
            result = str(resp['address'])
            deposits =  Deposits.objetos.all()
            
            if deposits.count() > 0:
                deposits.delete()
        
            deposit = Deposits(address=result)
            deposit.save()          
            
        else:
            raise Exception('Ocorreu um erro, por favor tente novamente')

    except Exception as e :
        result = 'Ocorreu um erro, por favor tente novamente'
        print(e)

    return render(request, 'index.html', {'result': result})
    
def addr_details(request):
    print(sessionID)
    try:
        deposit = Deposits.objetos.filter().first()
        addrObj = get_address_details(deposit.address, api_key=token, coin_symbol=blockchainName)
    except:
        raise Exception('Ocorreu um erro, por favor tente novamente')

    return render(request, 'step3.html', {'addrObj': addrObj, 'gDepositBTC': deposit.address})

def send_btc(request):
    print(sessionID)

    email = request.GET["email"]
    deposit = Deposits.objetos.filter().first()

    if deposit.address == "":
        return render(request, 'step2.html')

    tx_hash = simple_spend(
                    from_privkey=privkey,
                    to_address=deposit.address,
                    to_satoshis=_toSendSatoshis,
                    privkey_is_compressed=True,
                    api_key=token,
                    coin_symbol=blockchainName)

    send_mail('Depósito realizado', 'Hash de transação: ' + tx_hash, settings.EMAIL_HOST_USER, [email], fail_silently=False)

    return render(request, 'step2.html', {'tx_hash_send': tx_hash, 'email_send': email})
