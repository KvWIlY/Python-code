#Problema: Considere as equações de movimento para calcular a posição(s) e a velocidade(v)
#de uma particula em determinado instante t, dado sua aceleração a, posição inicial
#s0 e velocidade inicial v0. Escreva um programa que capture os valores de s0, v0, a e t,
#Todos os valores tratados no programa devem ser números reais(float e double)

s0 = float(input("Digite o valor da posição inicial: "))
v0 = float(input("Digite o valor da velocidade inicial: "))
a = float(input("Digite o valor da aceleração: "))
t = float(input("Digite o valor do intante t(tempo): "))

s = s0 + v0*t + ((a+t**2)/2)
v = v0 + a * t

print("\n")

print("A Posição(S) é de ",s)
print("A velocidade(v) é de ",v)