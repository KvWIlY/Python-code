a = int(input('valor a: '))
b = int(input('valor b: '))
op= input('escolha a operação: soma +,sub - ,div / ,mult * : ')

class Calculadora:

    a = b = None
    
    def __init__(self):
        pass     

    def soma(self, a, b):
        c = a + b
        return c

    def sub(self, a, b):
        c = a - b
        return c

    def div (self, a, b):
        c = a / b
        return c

    def mult(self, a, b):
        c = a * b
        return c

c = Calculadora();

op1={'*' : c.mult(a,b),
     '+' : c.soma(a,b),
     '/' : c.div(a,b),
     '-' : c.sub(a,b)
}

print(op1[op])
