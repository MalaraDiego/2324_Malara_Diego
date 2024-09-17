import random
from termcolor import colored 
import os

filename = "frasi.txt"

def carica(filename):
    frasi = []  
    file = open(filename, 'r')
    lines = file.readlines() 
    for i in range(0, len(lines), 2):
        frase = lines[i].strip().upper()
        sostantivo = lines[i + 1].strip()
        frasi.append((sostantivo, frase))
    return frasi

def inizializza():
    giocatori = []
    
    while True: 
        try:
            num_giocatori = int(input("Quanti giocatori vogliono giocare? "))
            if num_giocatori > 0:
                break
            else:
                print("Il numero di giocatori deve essere almeno 1.")
        except ValueError:
            print("Inserisci un numero valido.")
    
    colori_validi = ['red', 'blue', 'green', 'yellow']  
    
    for i in range(num_giocatori):
        nome = input(f"Inserisci il nome del giocatore {i+1}: ")
        
        while True: 
            colore = input(f"Inserisci un colore per il giocatore {i+1} (es: red, blue, green, yellow): ")
            if colore in colori_validi:
                break
            else:
                print("Colore non valido. Per favore, scegli un colore tra 'red', 'blue', 'green', 'yellow'.")
        
        giocatori.append({'nome': nome,'colore': colore,'montepremi': 0,'jolly': 0})
    return giocatori

def contenutoneruota():
    return [
        "500€", "300€", "600€", "800€", "Passa-mano", "Perdi-tutto", "Jolly", "1000€", "700€"
    ]

def stampa_frase_nascosta(frase, lettere_indovinate):
    frase_nascosta = ""
    for lettera in frase:
        if lettera in lettere_indovinate or lettera == ' ':
            frase_nascosta += lettera
        else:
            frase_nascosta += '*'
    return frase_nascosta

def gira_la_ruota(ruota):
    return random.choice(ruota)


def gioca_turno(giocatore, frase, lettere_indovinate, ruota):
    nome_colored = colored(giocatore['nome'], giocatore['colore'])
    
    print(f"\nÈ il turno di {nome_colored} (Montepremi: {giocatore['montepremi']}€, Colore: {giocatore['colore']})")
    print("Frase attuale:", stampa_frase_nascosta(frase, lettere_indovinate))

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

                if consonante in frase and consonante not in lettere_indovinate:
                    occorrenze = frase.count(consonante)
                    giocatore['montepremi'] += premio * occorrenze
                    lettere_indovinate.add(consonante)
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

                if vocale in frase and vocale not in lettere_indovinate:
                    occorrenze = frase.count(vocale)
                    lettere_indovinate.add(vocale)
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

                if vocale in frase and vocale not in lettere_indovinate:
                    occorrenze = frase.count(vocale)
                    giocatore['montepremi'] //= 2  
                    lettere_indovinate.add(vocale)
                    print(f"La vocale '{vocale}' è presente {occorrenze} volte!")
                else:
                    print(f"La vocale '{vocale}' non è presente.")
                return True
            else:
                print("Non puoi comprare una vocale perché il tuo montepremi è zero")
        else:
            print("Scelta non valida. Riprova.")

def frase_completa(frase, lettere_indovinate):
    for lettera in frase:
        if lettera not in lettere_indovinate and lettera != ' ':
            return False
    return True

def stampa_classifica(giocatori):
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
    ruota = contenutoneruota() 
    lettere_indovinate = set()
    turno = 0
    while not frase_completa(frase_misteriosa, lettere_indovinate):
        giocatore = giocatori[turno]
        turno_valido = gioca_turno(giocatore, frase_misteriosa, lettere_indovinate, ruota)
        if turno_valido:
            while True:  
                print("\nFrase attuale:", stampa_frase_nascosta(frase_misteriosa, lettere_indovinate))
                soluzione = input("Vuoi provare a indovinare la soluzione? (s/n): ").lower()
                if soluzione in ['s', 'n']:
                    break
                print("Risposta non valida. Inserisci 's' o 'n'.")
                
            if soluzione == 's':
                tentativo = input("Inserisci la soluzione: ").upper()
                if tentativo == frase_misteriosa:
                    print(f"Complimenti {giocatore['nome']}! Hai indovinato la frase!")
                    giocatore['montepremi'] *= 2
                    break
                else:
                    print("Soluzione errata.")

        turno = (turno + 1) % len(giocatori)
    
    stampa_classifica(giocatori)

def carica_classifica():
    classifica = {}
    if os.path.exists("montepremi.txt"):
        file = open("montepremi.txt", 'r')  
        for linea in file:
            dati = linea.strip().split(':')
            nome = dati[0]
            montepremi_str, partite_giocate_str = dati[1].split() 
            montepremi = int(montepremi_str)  
            partite_giocate = int(partite_giocate_str)  
            classifica[nome] = {'montepremi': montepremi, 'partite_giocate': partite_giocate}
    return classifica
if __name__ == "__main__":
    gioca()
