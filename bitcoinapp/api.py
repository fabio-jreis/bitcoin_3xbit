import requests
import blockcypher
from blockcypher import generate_new_address 
from blockcypher import is_valid_address
from blockcypher import send_faucet_coins
from blockcypher import get_address_details
from django.shortcuts import render

blockchainName = 'btc-testnet'
#blockchainName = 'bcy'
token = '6149e29abaeb46f0a778caf1b8a6db9b'

def getIp(request):
    response = requests.get('http://ip-api.com/json')
    geodata = response.json()
    return render(request, 'index.html', {
        'ip': geodata['query'],
        'country': geodata['country']
    })

def get_hostname(request):
    print('get_hostname')
    print(blockcypher.constants.COIN_SYMBOL_LIST)
    print(blockcypher.get_token_info(token))
    texto = 'FABIO'
    return render(request, 'index.html', {'result': texto})


def newWallet(request):
    try:
        resp = generate_new_address(coin_symbol=blockchainName, api_key=token)
        assert is_valid_address(resp['address']), resp

        if resp:
            result = str(resp['address'])
            print(str(resp))
        else:
            raise Exception('Ocorreu um erro, por favor tente novamente')

    except :
        result = 'Ocorreu um erro, por favor tente novamente'

    return render(request, 'index.html', {'result': result})

def send_faucet(request):
    resp = send_faucet_coins(address_to_fund='C7rHYXAkuk93n2umpgmG96nrwDawyS2SC6', satoshis=100000, api_key=token, coin_symbol=blockchainName)
    print(str(resp))
    return render(request, 'index.html')
    
def addr_details(request):
    addrObj = get_address_details('mtZFGURoy8HTqJXXGdR6jGPywM38e7aPLD', api_key=token, coin_symbol=blockchainName)
    txrefs = addrObj['txrefs']
    
    lenn = len(txrefs)
    print(lenn)
    print(str(txrefs))

    return render(request, 'index.html', {'txrefs': txrefs})