
lista=[]
scelta=900000


def inserisci(lista,oggetto):
    f=open('oggetti','w')
    lista.append(oggetto)
    f.write(lista[0]+'\n')
    f.close()
def visualizza(lista):
    for elemento in lista:
        print(elemento)
def elimina(lista,oggettoe):
    f=open('oggetti','w')
    for elemento in lista:
        lista.remove(oggettoe)
    for i in range(len(lista)):
        f.write(lista[i])
    f.close()


while scelta!=0:
    print('premi 1 per inserire un nuovo oggetto')
    print('premi 2 per visualizzare gli oggetti')
    print('premi 3 per eliminare un oggetto')
    print('premi 4 per salvare gli oggetti su un file')
    print('premi 5 per caricare da file un elenco già fatto')
    scelta=int(input('scegli'))
    match scelta:
        case 1:
            oggetto=input("inserisci il nome dell'oggetto da inserire")
            inserisci(lista,oggetto)
        case 2:
            visualizza(lista)
        case 3:
            oggettoe=input("inserisci il nome dell'oggetto da eliminare")
            elimina(lista,oggettoe)


