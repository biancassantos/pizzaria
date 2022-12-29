from time import sleep

sabores = ('Caipira', 'Calabresa', 'Carijó', 'Margherita', 'Frango com Catupiry', 'Portuguesa')
infos = {}
total_valores = {}


def titulo(msg):
    """
    >Cria um cabeçalho personalizado.
    :param msg: Título/frase do cabeçalho.
    :return: sem retorno
    """
    tam = 40
    print('\033[32m-\033[m' * tam)
    print(f'\033[1;33m{msg.center(tam)}\033[m')
    print('\033[32m-\033[m' * tam)


def menu():
    """
    >Mostra o menu de sabores.
    :return: sem retorno
    """
    titulo('PIZZARIA MEIA LUA')
    print('Seja bem vindo(a)! Escolha abaixo o \nsabor que deseja comprar.')
    for cont, sabor in enumerate(sabores):
        print(f' {cont:<2}- {sabor}')
    print('-' * 40)


def menu_tam():
    """
    >Mostra o menu de tamanhos e adiciona 'tamanho' e 'preço' aos dicionários.
    :return: sem retorno
    """
    titulo('TAMANHO DA PIZZA')
    tamanhos = ('Broto (20cm)', 'Média (30cm)', 'Grande (40cm)', 'SG (45cm)')
    precos = (20, 28, 45, 55)
    for c in range(0, 4):
        print(f'{c:<2}- {tamanhos[c]:<20} R${precos[c]:.2f}')
    print('-' * 40)

    while True:
        try:
            opcao = int(input('\033[34m>>OPÇÃO (0 à 3):\033[m '))
            while opcao > (len(tamanhos) - 1):
                print('\033[31mERRO! Digite uma opção válida.\033[m')
                opcao = int(input('\033[34m>>OPÇÃO (0 à 3):\033[m '))
        except ValueError:
            print('\033[31mERRO! Digite uma opção válida.\033[m')
        else:
            infos['tamanho'] = tamanhos[opcao]
            total_valores['preço'] = precos[opcao]
            break


def ingredientes(n):
    """
    >Mostra os ingredientes da pizza, pergunta se o cliente deseja retirar algum deles e mostra a montagem.
    :param n: número da opção correspondente ao sabor da pizza desejada
    :return: sem retorno
    """
    mostrar = []
    caipira = ['Molho de tomate', 'Mussarela', 'Milho', 'Ervilha', 'Catupiry']
    calabresa = ['Molho de tomate', 'Mussarela', 'Calabresa fatiada', 'Cebola', 'Orégano']
    carijo = ['Molho de tomate', 'Mussarela', 'Filé de frango', 'Catupiry', 'Orégano']
    margherita = ['Molho de tomate', 'Mussarela', 'Fatias de tomate', 'Parmesão']
    frango_cat = ['Mussarela', 'Peito de frango', 'Catupiry']
    portuguesa = ['Mussarela', 'Presunto', 'Ovo', 'Cebola', 'Pimentão', 'Azeitonas pretas']

    if n == 0:
        mostrar = caipira[:]
        infos['sabor'] = 'Caipira'
    elif n == 1:
        mostrar = calabresa[:]
        infos['sabor'] = 'Calabresa'
    elif n == 2:
        mostrar = carijo[:]
        infos['sabor'] = 'Carijó'
    elif n == 3:
        mostrar = margherita[:]
        infos['sabor'] = 'Margherita'
    elif n == 4:
        mostrar = frango_cat[:]
        infos['sabor'] = 'Frango c/ Catupiry'
    elif n == 5:
        mostrar = portuguesa[:]
        infos['sabor'] = 'Portuguesa'

    titulo(f'Ingredientes de {sabores[n]}:')
    lista_ingredientes(mostrar)
    resposta = deseja_cont('\033[34m>>Deseja retirar algum ingrediente? [S/N]\033[m ')

    if resposta == 'S':
        while True:
            try:
                total_item = len(mostrar) - 1
                ingrediente = int(input('\033[36m>>Digite o número do ingrediente'
                                        ' \nque desja retirar (1 de cada vez):\033[m '))
                while ingrediente > total_item:
                    print('\033[31mERRO! Digite uma opção válida.\033[m')
                    ingrediente = int(input('\033[36m>>Digite o número do ingrediente '
                                            '\nque desja retirar (1 de cada vez):\033[m '))
            except ValueError:
                print('\033[31mERRO! Digite uma opção válida.\033[m')
            else:
                del mostrar[ingrediente]
                print('-' * 40)
                lista_ingredientes(mostrar)

                resposta = deseja_cont('\033[34m>>Deseja retirar mais algum? [S/N]\033[m ')
                if resposta == 'N':
                    break

    montagem(mostrar)


def lista_ingredientes(lista):
    """
    >Mostra a lista de ingredientes da pizza.
    :param lista: lista de ingredientes.
    :return: sem retorno
    """
    for cont, ing in enumerate(lista):
        print(f'{cont:<2} - {ing}')
    print('-' * 40)


def deseja_cont(msg):
    """
    >Verifica se o cliente quer ou não realizar alguma ação.
    :param msg: frase que deseja colocar no input.
    :return: retorna uma resposta
    """
    res = input(msg).upper().strip()[0]
    while res not in 'SN':
        print('\033[31mERRO! Digite uma resposta válida.\033[m')
        res = input(msg).upper().strip()[0]
    return res


def montagem(lista):
    """
    >Mostra a montagem da pizza na tela.
    :param lista: lista dos ingredientes.
    :return: sem retorno
    """
    sleep(0.5)
    titulo('PREPARANDO A PIZZA...')
    sleep(0.5)
    for ing in lista:
        print(f'Adicionando {ing}', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.')
    print(f'\033[33mPizza PRONTA!\033[m')
    print('-' * 40)


def bebida():
    """
    >Verifica se o cliente deseja adicionar uma bebida ao pedido.
    :return: sem retorno
    """
    res = deseja_cont('\033[34m>>Deseja adicionar uma bebida? \n(Adicional de R$9.00) [S/N]:\033[m ')
    if res == 'S':
        total_valores['bebida'] = 9
        total_valores['total'] = total_valores['preço'] + total_valores['bebida']
    else:
        total_valores['total'] = total_valores['preço']


def lista_total():
    """
    >Retorna a conta do cliente em uma lista.
    :return: retorna uma lista
    """
    conta = [infos, total_valores]
    return conta


def conta_final(lista):
    """
    >Mostra detalhadamente a conta final do cliente.
    :param lista: lista de informações do pedido.
    :return: sem retorno
    """
    print('AGUARDE...')
    sleep(1.5)
    titulo('CONTA DETALHADA')
    for k, v in lista[0].items():
        print(f'{k.title():.<20} {v}')

    for k, v in lista[1].items():
        print(f'{k.title():.<20} R${v:.2f}')
