def printer(sequence):
    print("\n")
    print(f'{sequence[0]} | {sequence[1]} | {sequence[2]}')
    print(f'{sequence[3]} | {sequence[4]} | {sequence[5]}')
    print(f'{sequence[6]} | {sequence[7]} | {sequence[8]}')
    print("\n")

# Com base nas coordenadas iniciais, identifica o índice na lista de gravação dos valores das posições
def identifyId(coords):            
    return (3*(coords[0]-1))+(coords[1]-1)

# Verifica se a posição que o jogador selecionou para a jogada ainda está disponível
def idIsDisp(sequence,pos):
    if (sequence[pos] == ' '):
        return True
    else:
        return False

# Estando a posição disponível, registra a jogada, conforme o identificador de cada jogador ("X" ou "O")
def update(sequence,coords,player):
    pos = identifyId(coords)
    if (idIsDisp(sequence,pos)):
        if (player == 1):
            sequence[pos] = 'X'
        else:
            sequence[pos] = 'O'
    return sequence

# Checa se há sequência vencedora
def winner(sequence):
    if (sequence[0] == sequence[1] and sequence[0] == sequence[2]):
        if (sequence[0] == 'X'):
            return 1
        elif (sequence[0] == 'O'):
            return 2
    elif (sequence[3] == sequence[4] and sequence[3] == sequence[5]):
        if (sequence[3] == 'X'):
            return 1
        elif (sequence[3] == 'O'):
            return 2
    elif (sequence[6] == sequence[7] and sequence[6] == sequence[8]):
        if (sequence[6] == 'X'):
            return 1
        elif (sequence[6] == 'O'):
            return 2
    elif (sequence[0] == sequence[3] and sequence[0] == sequence[6]):
        if (sequence[0] == 'X'):
            return 1
        elif (sequence[0] == 'O'):
            return 2
    elif (sequence[1] == sequence[4] and sequence[1] == sequence[7]):
        if (sequence[1] == 'X'):
            return 1
        elif (sequence[1] == 'O'):
            return 2
    elif (sequence[2] == sequence[5] and sequence[2] == sequence[8]):
        if (sequence[2] == 'X'):
            return 1
        elif (sequence[2] == 'O'):
            return 2
    elif (sequence[0] == sequence[4] and sequence[0] == sequence[8]):
        if (sequence[0] == 'X'):
            return 1
        elif (sequence[0] == 'O'):
            return 2
    elif (sequence[2] == sequence[4] and sequence[2] == sequence[6]):
        if (sequence[2] == 'X'):
            return 1
        elif (sequence[2] == 'O'):
            return 2
    return 0
