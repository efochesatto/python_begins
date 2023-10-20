import board

def welcome():
    print("Seja bem-vindo(a) ao melhor do mundo dos games!")

def menu(): 
    print("\nPara continuar, informe uma das opções:\n1) Novo jogo\n2) Regras\n0) Sair\n")
    opt = int(input())
    return opt

def winner(sequence,players):
    playerWinnerId = board.winner(sequence)
    playerWinnerName = players[(playerWinnerId-1)]
    print(f"\n\nParabéns, {playerWinnerName}! Você é o vencedor!\n\n")
    board.printer(sequence)

def exit():
    print("Até a próxima!")

def rules(): 
    print("Aqui vai ter a descrição das regras")

