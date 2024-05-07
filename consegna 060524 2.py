from termcolor import colored
gusti=[]
f=open('gusti2.txt','r')

char='Ê'
c=0
while char !='':
    char=f.readline()[:-1]
    c+=1
    if c==1:
        gelato=char
    if c==2:
        color=char
        dati=(gelato,color)
        gusti.append(dati)
        c=0
for i in range(len(gusti)):
    print(colored(i[0],i[1]))


f.close()
    