import random
lista=[]
giocatori=5
ruota={1:'+1000 euro', 2:'+500 euro', 3:'+700 euro', 4:'perdi tutto', 5:'passa turno'}
def carica(lista):
    f=open('frasi.txt','r')
    for elemento in f:
        elemento=elemento[:-1]
        lista.append(elemento)
carica(lista)
#print(lista)
while giocatori>4:
    try:
        giocatori=int((input('inserisci il numero di giocatori che parteciperà (max 4)')))
        if giocatori>4:
            print('troppi giocatori')

    except:
        print('va inserito un numero in cifre')
def ruotx(ruota,montepremi):
    a=random.randint(1,5)
    print("l'evento ruota è", ruota[a])
ruotx(ruota)


    

    
    
    
