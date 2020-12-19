# Jogo de par ou impar onde o pc escolhe se é par ou ímpar
from random import randint

usuario = int(input("Digite um valor numérico inteiro: "))
computador = randint(0,1000)
escolha = randint(0,1)
total = computador + usuario
if (total % 2) == 0:
    a = 'par'
else:
    a = 'ímpar'

if escolha == 0:
    usuario1 = 'par'
    computador1 = 'ímpar'
else:
    usuario1 = 'ímpar'
    computador1 = 'par'

if (((total) % 2) == escolha):
    print('Usuario é ',usuario1,"----", "Computador é ,",computador1)
    print("Usuario escolheu: ",usuario)
    print("Computador escolheu: ",computador,"\n")
    print("O total foi de ",total," que é ",a," Logo, O vencedor é você usuário.") 
else:
    print('Usuario é ',usuario1,"----", "Computador é ",computador1)
    print("Usuario escolheu: ",usuario)
    print("Computador escolheu: ",computador,"\n")
    print("O total foi de ",total," que é ",a," Logo, O vencedor Sou eu o Computador HEHEHEHEHEHE.") 