import infos
import operations

def menuOperations():
    print("Informe a operação desejada:")
    op = input()
    opElements = op.split()
    opElements[1] = int(opElements[1])
    opElements[2] = int(opElements[2])
    res = None
    match opElements[0]:
        case 'add': res = operations.add(opElements[1],opElements[2])
        case 'sub': res = operations.sub(opElements[1],opElements[2])
        case 'mul': res = operations.mul(opElements[1],opElements[2])
        case 'div': res = operations.div(opElements[1],opElements[2])
        case 'din': res = operations.din(opElements[1],opElements[2])
        case 'rst': res = operations.rst(opElements[1],opElements[2])
        case 'pot': res = operations.pot(opElements[1],opElements[2])
        case 'raz': res = operations.raz(opElements[1],opElements[2])
    return res

def menu():
    menu = True
    while(menu):
        infos.menu()
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