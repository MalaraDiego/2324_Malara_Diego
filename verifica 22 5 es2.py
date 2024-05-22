import requests
import json
valute={'euro':'EUR','dollaro americano':'USD', 'franco svizzero':'CHF', 'dollaro inglese':'GBP', 'dollaro australiano': 'AUD', 'yen giapponese':'JPY' }
valuta_nome=0
valutaf=0

    
try:
    numero=int(input('inserisci il numero di unità che vuoi convertire'))
except:
    print('inserisci un valore numerico')
while valuta_nome not in valute:
    valuta_nome=input('inserisci la valuta iniziale')
    if valuta_nome not in valute:
        print('valuta non valida')
    else:
        valuta=valute[valuta_nome]
API=requests.get(f'https://open.er-api.com/v6/latest/{valuta}')
jsonAPI=API.json()
while valutaf not in valute:
    valutaf=input('inserisci la valuta finale')
    if valutaf not in valute:
        print('valuta non valida')
    else:
        valutar=valute[valutaf]
conversione=jsonAPI['rates'][valutar]
coversione=int(conversione)
print(f'{numero} {valuta} sono uguali a {conversione*numero} {valutar}')


