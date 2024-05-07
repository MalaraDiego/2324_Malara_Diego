gusti=[]
f=open('gusti1.txt','r')

char='Ê'
while char !='':
    char=f.readline()[:-1]
    gusti.append(char)
for i in range(len(gusti)):
    print(gusti[i])


f.close()
    