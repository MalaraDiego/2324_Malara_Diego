from termcolor import colored
 
gusti = []
FILE = "gusti3.txt"
 
def funzione(gusti,FILE):
    f = open(FILE, "r")
    for i in f:
        row = i[:-1]
        dati = row.split("#")
        gusti.append((dati[0],dati[1]))

funzione(gusti,FILE)
try:
    for i in range (len(gusti)):
        print(colored(gusti[i][0],gusti[i][1]))
except:
    print(colored('COCCO','green' ))

    