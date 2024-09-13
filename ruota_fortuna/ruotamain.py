import random
from termcolor import colored  

filename = "frasi.txt"

def carica(filename):
    frasi = []  
    with open(filename, 'r') as file:
        lines = file.readlines()  
        for i in range(0, len(lines), 2): 
            frasex = lines[i].strip().upper()  
            nomex = lines[i + 1].strip() 
            frasi.append((nomex, frasex))  
    return frasi 

def inizializza():
    giocatori = []
    num_giocatori = int(input("Quanti giocatori vogliono giocare? "))
    for i in range(num_giocatori):
        nome = input(f"Inserisci il nome del giocatore {i+1}: ")
        colore = input(f"Inserisci un colore per il giocatore {i+1} (es: red, blue, green, yellow): ")
        giocatori.append({'nome': nome,'colore': colore,'montepremi': 0,'jolly': 0})
    return giocatori

def contenutoruota():
    return [
        "500€", "300€", "600€", "800€", "Passa-mano", "Perdi-tutto", "Jolly", "1000€", "700€"]

def frasefinale(frasex, guessedletters):
    frase_nascosta = ""
    for letter in frasex:
        if letter in guessedletters or letter == ' ':
            frase_nascosta += letter
        else:
            frase_nascosta += '*'
    return frase_nascosta

def gira_la_ruota(ruota):
    return random.choice(ruota)

def turno(giocatore, frasex, guessedletters, ruota):
    nome_colored = colored(giocatore['nome'], giocatore['colore'])
    
    print(f"\nÈ il turno di {nome_colored} (Montepremi: {giocatore['montepremi']}€, Colore: {giocatore['colore']})")
    print("Frase attuale:", frasefinale(frasex, guessedletters))

    while True:
        scelta = input("Vuoi girare la ruota, usare un jolly o comprare una vocale? (gira/jolly/vocale): ").lower()

        if scelta == 'gira':
            esito = gira_la_ruota(ruota)
            print(f"La ruota ha detto: {esito}")
            
            if esito == "Passa-mano":
                print("Passa al prossimo giocatore.")
                return False
            elif esito == "Perdi-tutto":
                print("Hai perso tutto!")
                giocatore['montepremi'] = 0
                return False
            elif esito == "Jolly":
                print("Hai ottenuto un jolly!")
                giocatore['jolly'] += 1
                return False
            else:
                premio = int(esito.replace("€", ""))
                consonante = ''
                while True:
                    consonante = input("Inserisci una consonante: ").upper()
                    if consonante in "AEIOU" or len(consonante) != 1:
                        print("Devi inserire una consonante valida!")
                    else:
                        break

                if consonante in frasex and consonante not in guessedletters:
                    occorrenze = frasex.count(consonante)
                    giocatore['montepremi'] += premio * occorrenze
                    guessedletters.add(consonante)
                    print(f"La consonante '{consonante}' è presente {occorrenze} volte!")
                else:
                    print(f"La consonante '{consonante}' non è presente.")
                return True

        elif scelta == 'jolly':
            if giocatore['jolly'] > 0:
                giocatore['jolly'] -= 1
                vocale = ''
                while True:
                    vocale = input("Inserisci una vocale: ").upper()
                    if vocale not in "AEIOU" or len(vocale) != 1:
                        print("Devi inserire una vocale valida!")
                    else:
                        break

                if vocale in frasex and vocale not in guessedletters:
                    occorrenze = frasex.count(vocale)
                    guessedletters.add(vocale) #tipo append ma per i set
                    print(f"La vocale '{vocale}' è presente {occorrenze} volte!")
                else:
                    print(f"La vocale '{vocale}' non è presente.")
                return True
            else:
                print("Non hai jolly disponibili!")

        elif scelta == 'vocale':
            if giocatore['montepremi'] > 0:
                vocale = ''
                while True:
                    vocale = input("Inserisci una vocale: ").upper()
                    if vocale not in "AEIOU" or len(vocale) != 1:
                        print("Devi inserire una vocale valida!")
                    else:
                        break

                if vocale in frasex and vocale not in guessedletters:
                    occorrenze = frasex.count(vocale)
                    giocatore['montepremi'] //= 2  # Dimezza il montepremi
                    guessedletters.add(vocale)
                    print(f"La vocale '{vocale}' è presente {occorrenze} volte!")
                else:
                    print(f"La vocale '{vocale}' non è presente.")
                return True
            else:
                print("Non puoi comprare una vocale perché il tuo montepremi è zero!")
        else:
            print("Scelta non valida. Riprova.")


def controlz(frasex, guessedletters):
    for letter in frasex:
        if letter not in guessedletters and letter != ' ':
            return False
    return True


def bubblesort_lb(giocatori):
    n = len(giocatori)
    for i in range(n):
        for j in range(0, n-i-1):
            if giocatori[j]['montepremi'] < giocatori[j+1]['montepremi']:
                giocatori[j], giocatori[j+1] = giocatori[j+1], giocatori[j]

    print("\nClassifica finale:")
    for i, giocatore in enumerate(giocatori, 1):
        nome_colored = colored(giocatore['nome'], giocatore['colore'])
        print(f"{i}. {nome_colored} - Montepremi: {giocatore['montepremi']}€")



def gioca():

    frasi = carica('frasi.txt')
    titolo, frase_misteriosa = random.choice(frasi)
    print(f"\nTitolo: {titolo}")
    giocatori = inizializza()
    ruota = contenutoruota()
    guessedletters = set()
    turno = 0
    while not controlz(frase_misteriosa, guessedletters):
        giocatore = giocatori[turno]
        turno_valido = turno(giocatore, frase_misteriosa, guessedletters, ruota)
        
        if turno_valido:
            while True:  
                soluzione = input("Vuoi provare a indovinare la soluzione? (s/n): ").lower()
                if soluzione in ['s', 'n']:
                    break
                print("Risposta non valida. Inserisci 's' o 'n'.")
                
            if soluzione == 's':
                tentativo = input("Inserisci la soluzione: ").upper()
                if tentativo == frase_misteriosa:
                    print(f"Complimenti {giocatore['nome']}! Hai indovinato la frasex!")
                    giocatore['montepremi'] *= 2
                    break
                else:
                    print("Soluzione errata.")
        turno = (turno + 1) % len(giocatori)
    bubblesort_lb(giocatori)


import os

def carica_classifica():
    classifica = {}
    if os.path.exists("montepremi.txt"):
        with open("montepremi.txt", 'r') as file:
            for linea in file:
                dati = linea.strip().split(':')
                nome = dati[0]
                montepremi, partite_giocate = map(int, dati[1].split())
                classifica[nome] = {'montepremi': montepremi, 'partite_giocate': partite_giocate}
    return classifica
if __name__ == "__main__":
    gioca()



"""
        for i in parola:
            if i != " ":
                print("*")
        print(ruota)

        if isinstance(ruota, int):
            pass
"""