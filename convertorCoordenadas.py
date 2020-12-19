#Programa que converte coordenadas polare(raio r e Ângulo a) em coordenadas cartesianas (abscissa x e ordenada y).
import math

print("Insira os valores a baixo para  a conversão das \n" 
      "coordenadas polares para coordenadas cartesianas.\n")
    
raio = float(input("Digite o valor do raio: "))
angulo = float(input("Digite o valor do angulo: "))

x = raio * math.cos(angulo)
y = raio * math.sin(angulo)

print("Coordenadas Cartesianas -> ","(",round(x,5),round(y,5),")")
