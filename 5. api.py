import requests

url = 'https://api.exchangerate-api.com/v6/latest'
req = requests.get(url)

if req.status_code == 200:
    print(req.json())
    valor_BRL = float(input('Inform the amount in reais to be converted to dollars: R$'))
    valor_USD = req.json()['rates']['BRL']
    print(f'Convertion:\nR${valor_BRL:.3f} for dollars = US${(valor_BRL/valor_USD):.3f}')
else:
    print(f'Could not get a response from the API. Status: {req.status_code}')
