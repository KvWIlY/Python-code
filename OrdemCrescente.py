#  Programa que recebe três números interiros como entrada e imprime, como sáida, os números em ordem crescente.
num1 = int(input('Digite um número interio: '))
num2 = int(input('Digite um número interio: '))
num3 = int(input('Digite um número interio: '))

#forma 1 de fazer 
listaNum = [num1,num2,num3] 
print(sorted(listaNum))
#--------------------------------------------------------
'''
# Forma 2 de fazer 
listaNum.sort()
print(listaNum)

'''
#-------------------------------------------------------
#forma 3 de fazer
'''
if (num1 < num2) and (num2 < num3) :
    print(num1,num2,num3)
else:
    if (num2 < num1) and (num1 < num3):
        print(num2,num1,num3)
    else:
        if (num2 < num3) and (num3 < num1):
            print(num2,num3,num1)
        else:
            if (num3 < num2) and (num2 < num1):
                print(num3,num2,num1)
            else:
                if (num3 < num1) and (num1 < num2):
                    print(num3,num1,num2)
                else:
                    if (num1 < num3) and (num3 < num2):
                        print(num1,num3,num2)
'''