from modulos import *

menu()

while True:
    opcao = int(input('\033[34m>>OPÇÃO (0 à 5):\033[m '))
    while opcao > 5:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
        opcao = int(input('\033[34m>>OPÇÃO (0 à 5):\033[m '))
    break

menu_tam()
ingredientes(opcao)
bebida()
conta = lista_total()
conta_final(conta)
print('-' * 40)
print(f"\033[1;33m{'Obrigado pela preferência'.center(40)}\033[m")
print(f"\033[1;33m{'VOLTE SEMPRE!'.center(40)}\033[m")
