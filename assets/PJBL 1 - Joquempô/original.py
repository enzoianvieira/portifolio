from random import randint
from time import sleep
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_opcoes():
    print('''Opções de jogo:
    [0]  PLAYER X COMPUTADOR
    [1]  COMPUTADOR X COMPUTADOR
    [2]  PLAYER X PLAYER''')

def obter_modo_jogo():
    return int(input('Escolha qual será a modalidade de jogo: '))

def jogar_pedra_papel_tesoura(jogador_1, jogador_2):
    itens = ('Pedra', 'Papel', 'Tesoura')
    print('Jogando:')
    sleep(1)
    print('=-' * 11)
    print('Jogador 1 jogou {}'.format(itens[jogador_1]))
    sleep(1)
    print('Jogador 2 jogou {}'.format(itens[jogador_2]))
    print('=-' * 11)
    sleep(1)
    resultado = determinar_vencedor(jogador_1, jogador_2)
    print(resultado)

def determinar_vencedor(jogador_1, jogador_2):
    itens = ('Pedra', 'Papel', 'Tesoura')
    if jogador_1 == jogador_2:
        return 'EMPATE'
    elif (jogador_1 == 0 and jogador_2 == 2) or (jogador_1 == 1 and jogador_2 == 0) or (jogador_1 == 2 and jogador_2 == 1):
        return 'Jogador 1 GANHOU'
    else:
        return 'Jogador 2 GANHOU'

def jogar_novamente():
    opcao = input('Deseja jogar novamente? (s/n) ')
    if opcao.lower() == 's': 
        return True
    elif opcao.lower() == 'n':
        print('Obrigado por jogar! Até a próxima.')
        return False
    else:
        print('Opção inválida. Digite "s" para jogar novamente ou "n" para sair.')
        return jogar_novamente()

while True:
    limpar_tela()
    imprimir_opcoes()
    modo = obter_modo_jogo()

    if modo == 0:
        limpar_tela()
        itens = ('Pedra', 'Papel', 'Tesoura')
        computador = randint(0, 2)
        print('''Escolha sua jogada:
        [0]  PEDRA
        [1]  PAPEL
        [2]  TESOURA''')
        jogador = int(input('Entre com o número da sua jogada: '))
        print('=-' * 11)
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('=-' * 11)
        resultado = determinar_vencedor(jogador, computador)
        print(resultado)

    elif modo == 1:
        limpar_tela()
        itens = ('Pedra', 'Papel', 'Tesoura')
        computador_1 = randint(0, 2)
        computador_2 = randint(0, 2)
        print('Jogando:')
        sleep(1)
        print('=-' * 11)
        print('Computador 1 jogou {}'.format(itens[computador_1]))
        sleep(1)
        print('Computador 2 jogou {}'.format(itens[computador_2]))
        print('=-' * 11)
        resultado = determinar_vencedor(computador_1, computador_2)
        print(resultado)

    elif modo == 2:
        limpar_tela()
        itens = ('Pedra', 'Papel', 'Tesoura')
        print('Jogador 1:')
        print('''Escolha sua jogada:
        [0]  PEDRA
        [1]  PAPEL
        [2]  TESOURA''')
        jogador_1 = int(input('Entre com o número da sua jogada: '))
        print('Jogador 2:')
        print('''Escolha sua jogada:
        [0]  PEDRA
        [1]  PAPEL
        [2]  TESOURA''')
        jogador_2 = int(input('Entre com o número da sua jogada: '))
        sleep(1)
        print('=-' * 11)
        print('Jogador 1 jogou {}'.format(itens[jogador_1]))
        sleep(1)
        print('Jogador 2 jogou {}'.format(itens[jogador_2]))
        print('=-' * 11)
        resultado = determinar_vencedor(jogador_1, jogador_2)
        print(resultado)

    else:
        print('Modo de jogo inválido, tente novamente.')

    retorna = jogar_novamente()
    if not retorna:
        break