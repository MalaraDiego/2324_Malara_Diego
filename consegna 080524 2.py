import json
from termcolor import colored
gusti = []
 
with open ("gusti4.json", "r") as file:
    dati = json.load(file)
 
 
for gusto in dati["gusti"]:
    nome_gusto = gusto["gusto"]
    colore = gusto["colore"]
    gusti.append((nome_gusto,colore))
 
for i in range (len(lista)):
    print(colored(lista[i][0], lista[i][1]))

    