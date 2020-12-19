#Questão: Escreva um programa para fezer conversões entre diferentes unidades. As opções do programa devem ser exibidas em forma de um menu apresentado na tela,
#No primeiro nível, ousuário escolhe a unidade; no segundo níve, escolhe a cenvesão que deseja, fornecendo então o valor convertido.
#Por fim o programa exibe o valor resultante na tela.

tipoDeConversão = int(input('''Escolha qual opção de Conversão você quer fazer.
1. Peso
2. Volume
3. Comprimento 
-> '''))

# Declaração de variaveis
opção = 0
umalibra = 0.4536 #kg
umaOnça = 28.3495 #g
umGalão = 3.7854 #L
umaOnçaFluido = 29.5735 #ml
umaMilha = 1.6093 #Km
umaJarda = 0.9144 # M

# Funções
# I. Peso
def libraPquilograma():
    valorAconverter = float(input("\n Digite o valor que você que converter: "))
    resultado = umalibra * valorAconverter
    print( valorAconverter,' libras é igual a ',resultado,' quilograma' )
def quilogramaPlibra():
    valorAconverter = float(input("\n Digite o valor que você que converter: "))
    resultado = valorAconverter / umalibra
    print( valorAconverter,' Quilogramas é igual a ',resultado,' Libras' )
def onçaPgrama():
    valorAconverter = float(input("\n Digite o valor que você que converter: "))
    resultado = umaOnça * valorAconverter
    print( valorAconverter,' Onças é igual a ',resultado,' Gramas' )
def gramaPonça():
    valorAconverter = float(input("\n Digite o valor que você que converter: "))
    resultado = valorAconverter / umaOnça
    print( valorAconverter,' Gramas é igual a ',resultado,' Onças' )
# II. Volume
def galaoPlitro():
    valorAconverter = float(input("\n Digite o valor que você que converter: "))
    resultado = umGalão * valorAconverter
    print( valorAconverter,' Galões é igual a ',resultado,' Litros' )
def litroPgalao():
    valorAconverter = float(input("\n Digite o valor que você que converter: "))
    resultado =  valorAconverter / umGalão
    print( valorAconverter,' Litros é igual a ',resultado,' Galão' )
def onçaPmililitro():
    valorAconverter = float(input("\n Digite o valor que você que converter: "))
    resultado =  valorAconverter * umaOnçaFluido
    print( valorAconverter,' Onças é igual a ',resultado,' Mililitros' )
def mililitrosPonças():
    valorAconverter = float(input("\n Digite o valor que você que converter: "))
    resultado =  valorAconverter / umaOnçaFluido
    print( valorAconverter,' Onças é igual a ',resultado,' Mililitros' )
#III. Comprimento
def milhaPquilometro():
    valorAconverter = float(input("\n Digite o valor que você que converter: "))
    resultado = valorAconverter * umaMilha
    print( valorAconverter,' Milhas é igual a ',resultado,' Quilometros' )
def quilometroPmilha():
    valorAconverter = float(input("\n Digite o valor que você que converter: "))
    resultado = valorAconverter / umaMilha
    print( valorAconverter,' Milhas é igual a ',resultado,' Quilometros' )
def jardasPmetros():
    valorAconverter = float(input("\n Digite o valor que você que converter: "))
    resultado = valorAconverter * umaJarda
    print( valorAconverter,' jadas é igual a ',resultado,' Metros' )
def metrosPjardas():
    valorAconverter = float(input("\n Digite o valor que você que converter: "))
    resultado = valorAconverter / umaJarda
    print( valorAconverter,' Metros é igual a ',resultado,' Jardas' )
#-----------------------------------------------------------------------------------#
if tipoDeConversão == 1:
    opção = int(input(''' 
 1. Libra -> Quilograma
 2. Quilograma -> Libra
 3. Onça -> Grama
 4. Grama -> Onça
 Escolha entre as opções de conversão acima:  '''))
    if opção == 1:
        libraPquilograma()
    elif opção == 2:
        quilogramaPlibra()
    elif opção == 3:
        onçaPgrama()
    elif opção == 4:
        gramaPonça()
    else:
        print(" Você não inseriu uma das opções dadas, reinicie o programa.")
elif tipoDeConversão == 2:
    opção = int(input('''
 1. Galão -> Litro
 2. Litro -> Galão
 3. Onça -> Mililitro
 4. Mililitro -> Onça
 Escolha entre as opções de conversão acima:  '''))
    if opção == 1:
        galaoPlitro()
    elif opção == 2:
        litroPgalao()
    elif opção == 3:
        onçaPmililitro()
    elif opção == 4:
        mililitrosPonças()
    else:
        print(" Você não inseriu uma das opções dadas, reinicie o programa.")
elif tipoDeConversão == 3:
    opção = int(input('''
 1. Milha -> Quilômetro
 2. Quilômetro -> Milha
 3. Jardas -> Metro
 4. Metro -> Jardas
 Escolha entre as opções de conversão acima:  '''))
    if opção == 1:
        milhaPquilometro()
    elif opção == 2:
        quilogramaPlibra()
    elif opção == 3:
        jardasPmetros()
    elif opção == 4:
        metrosPjardas()
    else:
        print(" Você não inseriu uma das opções dadas, reinicie o programa.")