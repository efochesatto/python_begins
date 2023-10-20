import messages
import controlPlay


def getPlayers():
    players = []
    players.append(input("Nome do Jogador 1: "))
    players.append(input("Nome do Jogador 2: "))
    return players

def menu():
    a = None

def main(): 
    messages.welcome()
    playing = True
    while (playing):
        opt = messages.menu()
        if (opt == 1):
            players = getPlayers()
            print(f"O nome dos jogadores são: {players}")
            controlPlay.main(players)
        elif (opt == 2):
            messages.rules()
        elif (opt == 0):
            playing = False
        else:
            print("A opção informada não é válida.")
    messages.exit()

main()
