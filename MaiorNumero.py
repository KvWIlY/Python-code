'''
    Programa que recebe três números inteiros como entrada e imprime,como sáida,o maior número recebido.
'''
num1 = int(input('Digite um número interio: '))
num2 = int(input('Digite um número interio: '))
num3 = int(input('Digite um número interio: '))

if (num1 > num2) and (num1 > num3) :
    print('O maior número é: ',num1)
elif (num2 > num3) and (num2 > num1):
    print('O maior número é: ',num2)
elif (num3 > num2) and (num3 > num1):
    print('O maior número é: ',num3)


'''
# outra Forma de Fazer

from functools import reduce 

num1 = int(input('Digite um número interio: '))
num2 = int(input('Digite um número interio: '))
num3 = int(input('Digite um número interio: '))

listaNum = [num1,num2,num3]  
maxNum = lambda a,b: a if a > b else b
print('O maior número é: ' , reduce(maxNum,listaNum))

'''