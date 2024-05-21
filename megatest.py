lista = []
bigm=0
c=0
seye=0
with open('registro.txt', 'r') as f:
    for riga in f:
        riga = riga.strip()  # Rimuove eventuali spazi bianchi e caratteri di nuova linea
        riga = riga.split('#')
        
        voti = [float(voto) for voto in riga[1:6]]
        media = sum(voti) / len(voti)
        
        #tupla = (riga[0], media)
        tupla=(riga[0], riga[3])
        
        lista.append(tupla)
seye=float(tupla[1])

lista = sorted(lista)

listona=[]
for tupla in lista:
    if tupla[1]=='8.5':
        listona.append(tupla)
for i in range(len(listona)):
    print(listona[i][0], listona[i][1])
if len(listona)==0:
    print(listona)
