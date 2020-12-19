# Jogo Pedra, papel, Tesoura.
# obs: tem algumas forma de fazer o algoritmo .
import random

print("Seja bem vindo ao Jogo Pedra, Papel, Tesoura.\n")
print("Escolha entre as opções a seguir: Pedra, Papel ou Tesoura ")
player_jogada = input('Digite aqui sua opção em em letras minúscula: ')


dic = {'pedra' : 0 , 'papel' : 1 ,  'tesoura' : 2}

# metodo em que o pc vai usar para pegar aleatoriamente as opções
jogada_do_pc  = random.choice(['pedra', 'papel','tesoura'])
# Salvando em um variavel os valores da jogada do pc e do usuario
pesoJogadaPc = dic[jogada_do_pc]
pesoJogador = dic[player_jogada]

# Primeira forma.
if pesoJogadaPc == 0 and pesoJogador == 1:
    print('Jogada do Usuário: ',player_jogada)
    print('Jogada do Computador: ',jogada_do_pc)
    print('----------------------------------')
    print('O ganhador é o Usuário.')
else:
    if pesoJogadaPc == 0 and pesoJogador == 2:
        print('Jogada do Usuário: ',player_jogada)
        print('Jogada do Computador: ',jogada_do_pc)
        print('----------------------------------')
        print('O ganhador é o Computador') 
    else:
        if pesoJogadaPc == 0 and pesoJogador == 0:
            print('Jogada do Usuário: ',player_jogada)
            print('Jogada do Computador: ',jogada_do_pc)
            print('----------------------------------')
            print('O ganhador não é ninguém pois deu empate.')
        else:
            if pesoJogadaPc == 1 and pesoJogador == 0:
                print('Jogada do Usuário: ',player_jogada)
                print('Jogada do Computador: ',jogada_do_pc)
                print('----------------------------------')
                print('O ganhador é o Computador') 
            else:
                if pesoJogadaPc == 1 and pesoJogador == 1:
                    print('Jogada do Usuário: ',player_jogada)
                    print('Jogada do Computador: ',jogada_do_pc)
                    print('----------------------------------')
                    print('O ganhador não é ninguém pois deu empate.')  
                else:
                    if pesoJogadaPc == 1 and pesoJogador == 2:
                        print('Jogada do Usuário: ',player_jogada)
                        print('Jogada do Computador: ',jogada_do_pc)
                        print('----------------------------------')
                        print('O ganhador é o Usuário.')
                    else:
                        if pesoJogadaPc == 2 and pesoJogador == 0:
                            print('Jogada do Usuário: ',player_jogada)
                            print('Jogada do Computador: ',jogada_do_pc)
                            print('----------------------------------')
                            print('O ganhador é o Usuário.')
                        else:
                            if pesoJogadaPc == 2 and pesoJogador == 1:
                                print('Jogada do Usuário: ',player_jogada)
                                print('Jogada do Computador: ',jogada_do_pc)
                                print('----------------------------------')
                                print('O ganhador é o Computador.')
                            else:
                                if pesoJogadaPc == 2 and pesoJogador == 2:
                                    print('Jogada do Usuário: ',player_jogada)
                                    print('Jogada do Computador: ',jogada_do_pc)
                                    print('----------------------------------')
                                    print('O ganhador não é ninguém pois deu empate.')

# Outra Forma de fazer 

'''

def WinComputador():
    print('Jogada do Usuário: ',player_jogada)
    print('Jogada do Computador: ',jogada_do_pc)
    print('----------------------------------')
    print('O ganhador é o Computador.')

def WinUsuario():
    print('Jogada do Usuário: ',player_jogada)
    print('Jogada do Computador: ',jogada_do_pc)
    print('----------------------------------')
    print('O ganhador é o Usuario.')

def Empate():
    print('Jogada do Usuário: ',player_jogada)
    print('Jogada do Computador: ',jogada_do_pc)
    print('----------------------------------')
    print('O ganhador não é ninguém pois deu empate.')

#-----------------------------------------------------------------------

if pesoJogadaPc == 0 and pesoJogador == 1:
    print(WinUsuario())
else:
    if pesoJogadaPc == 0 and pesoJogador == 2:
        print(WinComputador()) 
    else:
        if pesoJogadaPc == 0 and pesoJogador == 0:
            print(Empate())
        else:
            if pesoJogadaPc == 1 and pesoJogador == 0:
                print(WinComputador()) 
            else:
                if pesoJogadaPc == 1 and pesoJogador == 1:
                    print(Empate())  
                else:
                    if pesoJogadaPc == 1 and pesoJogador == 2:
                        print(WinUsuario())
                    else:
                        if pesoJogadaPc == 2 and pesoJogador == 0:
                            print(WinUsuario())
                        else:
                            if pesoJogadaPc == 2 and pesoJogador == 1:
                                print(WinComputador())
                            else:
                                if pesoJogadaPc == 2 and pesoJogador == 2:
                                    print(Empate())
'''