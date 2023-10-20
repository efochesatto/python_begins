import board
import messages

def getPos(playerName):
    pos = []
    print(f"{playerName}, informe a sua jogada:\n")
    pos.append(int(input('Linha: ')))
    pos.append(int(input('Coluna: ')))
    return pos

def jogada(player, playerName, sequence):
    print(f"Entrou na jogada com a sequence = {sequence}")
    board.printer(sequence)
    coords = getPos(playerName)
    print(f'As coordenadas são {coords}')
    pos = board.identifyId(coords)
    print(f'Índice {pos}')
    disp = board.idIsDisp(sequence,pos)
    if (disp):
        sequence = board.update(sequence,coords,player)
    board.printer(sequence)
    return sequence
    
def main(players): 
    sequence = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print(f"A sequência de início é {sequence}")
    continuePlay = 0
    while (continuePlay == 0):
        sequence = jogada(1,players[0],sequence)
        continuePlay = board.winner(sequence)
        if (continuePlay == 0):
            sequence = jogada(2,players[1],sequence)
            continuePlay = board.winner(sequence)
    messages.winner(sequence,players)