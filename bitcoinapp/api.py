import requests
import blockcypher
from blockcypher import generate_new_address, is_valid_address
from django.shortcuts import render

blockchainName = 'btc-testnet'
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
        else:
            raise Exception('Ocorreu um erro, por favor tente novamente')

    except :
        result = 'Ocorreu um erro, por favor tente novamente'

    return render(request, 'index.html', {'result': result})