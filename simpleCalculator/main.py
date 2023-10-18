import infos
import operations

def menuOperations():
    print("Informe a operação desejada:")
    op = input()
    opElements = op.split()
    res = None
    match opElements[1]:
        case 'add': res = operations.add(opElements[2],opElements[3])
        case 'sub': res = operations.sub(opElements[2],opElements[3])
        case 'mul': res = operations.mul(opElements[2],opElements[3])
        case 'div': res = operations.div(opElements[2],opElements[3])
        case 'din': res = operations.din(opElements[2],opElements[3])
        case 'rst': res = operations.rst(opElements[2],opElements[3])
        case 'pot': res = operations.pot(opElements[2],opElements[3])
        case 'raz': res = operations.raz(opElements[2],opElements[3])
    return res

def menu():
    menu = True
    while(menu):
        print("\n1) Realizar cálculo\n2)Ajuda\n3)Sobre\n0)Sair\nInforme a ação desejada:")
        option = int(input())
        if (option == 1):
            print(f'O resultado é {menuOperations()}')
        elif (option == 2):
            infos.help()
        elif (option == 3):
            infos.about()
        elif (option == 0):
            menu = False
        else: 
            print("\nA opção informada não é válida.\n")

def main():
    infos.welcome()
    menu()
    infos.exit()

main()