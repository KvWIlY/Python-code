a = int(input('valor a: '))
b = int(input('valor b: '))
op= input('escolha a operação: soma +,sub - ,div / ,mult * : ')

def soma (a,b):
    c = a + b
    return c

def sub(a,b):
    c = a - b
    return c

def div (a,b):
    c = a / b
    return c

def mult(a,b):
    c = a * b
    return c

op1={'*' : mult(a,b),
     '+' : soma(a,b),
     '/' : div(a,b),
     '-' : sub(a,b)
}

print(op1[op])
