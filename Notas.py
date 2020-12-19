# Programa que ler duas notas de um aluno, e se as media nao for maior ou igual a 5
# e se uma das notas for menor que 3, pessa ao usuario a nota da 3 para calcular a media geral prova
# e indica se ele esta reprovado ou não.

p1 = float(input("Digite o valor da sua primeira nota: "))
p2 = float(input("Digite o valor da sua segunda nota: "))

media1 = (p1 + p2)/2

if (media1 >= 5) and (p1 > 3) and (p2 > 3):
    print("Parabéns, Aprovado.")
else:
    p3 = float(input("Digite o valor da nota da sua terceira nota: "))
    if p1 > p2:
        media1 = (p1 + p3)/2
        if media1 >= 5:
            print("Aprovado.")
        else:
            print("Reprovado.")
    else:
        media1 = (p2 + p3)/2
        if media1 >= 5:
            print("Aprovado.")
        else:
            print("Reprovado.")
