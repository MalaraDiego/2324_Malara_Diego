vocalist=['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
consonantlist = [
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z',
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
playerlist=[]
def giocatori(players,playerlist):
    for i in range(players):
        giocatore=input(f'inserisci il nome del {i+1}° giocatore')
        playerlist.append(giocatore)
        print(playerlist)


players=int(input('quanti giocatori giocheranno? '))
giocatori(players,playerlist)