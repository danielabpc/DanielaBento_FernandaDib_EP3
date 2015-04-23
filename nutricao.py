# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:28:29 2015

@author: david
"""

arquivoa = open("alimentos.csv", encoding="latin1")
alimentos = arquivoa.readlines()

arquivou = open("usuario.csv", encoding = "utf-8")
usuario = arquivou.readlines()

print("Ola, voce esta no nosso programa de dietas!")
print("")

linha1 = usuario[1]
dados1 = linha1.split(",")
print(dados1)
print("")

peso = int(dados1[2])
altura = float(dados1[4])*100
idade = int(dados1[1])
alturaimc = float(dados1[4])

if dados1[3]=="M":
    formulah = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    print("A quantidade diaria de calorias ideal para seu corpo eh:", formulah)
    print("")
if dados1[3]=="F":
    formulam = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
    print("A quantidade diaria de calorias ideal para seu corpo eh:", formulam)
    print("")

dic_cal = {}
for linha in alimentos:
    comidas = linha.split(",")
    chave = comidas[0]
    calorias = comidas[2]
    dic_cal[chave] = calorias

dic_datas = {}
listadatas =[]
caldia = {}

for i in usuario[3::]:
    if i[0] not in listadatas:
        x = i.split(",")
        caldia[x[0]]= 0
        
for i in usuario[3::]:
    if i[0] not in listadatas:
        x = i.split(",")
        listadatas.append(x[0])
        dic_datas[x[0]]= {}
    caloriasingeridas = int((int(dic_cal[x[1]])/100)*float(x[2]))
    caldia[x[0]] += caloriasingeridas
    
print("A quantidade diaria de calorias ingeridas no dia 1 foi de:", caldia["6/4/15"])
print(formulah - caldia["6/4/15"], "calorias para atingir a quantidade diaria ideal")
dia2 = print("A quantidade diaria de calorias ingeridas no dia 2 foi de:", caldia["7/4/15"])
print(formulah - caldia["7/4/15"], "calorias para atingir a quantidade diaria ideal")
print("")

protdia = {}
dic_pro = {}

for linha in alimentos:
    comidas = linha.split(",")
    chave = comidas[0]
    proteinas = comidas[3]
    dic_pro[chave] = proteinas
print(dic_pro)
 
for chave in dic_pro:
    if comidas[0] not in usuario:
        y = chave.split(",")
        protdia[y[0]]= 0
        
for chave in usuario[3::]:
    if comidas[0] not in usuario:
        y = chave.split(",")
        usuario.append(y[0])
        dic_pro[y[0]]= {}
    proteinasingeridas = int((float(dic_pro[y[1]])/100)*float(y[2]))
#print(proteinasingeridas)
    protdia[y[0]] += proteinasingeridas

dic_carb = {}
for linha in alimentos:
    comidas = linha.split(",")
    chave = comidas[0]
    carboidratos = comidas[4]
    dic_carb[chave] = carboidratos

dic_gord = {}
for linha in alimentos:
    comidas = linha.split(",")
    chave = comidas[0]
    gorduras = comidas[5]
    dic_gord[chave] = gorduras

IMC = float((1.3*peso)/(alturaimc**2.5))
print("Seu indice de massa corporal eh de:", IMC)
print("")

if IMC < 18.5:
    print("Se alimente melhor, pois voce esta abaixo do peso!")
if IMC >= 18.5 and IMC <= 24.9:
    print("Continue assim, voce esta no peso ideal!")
if IMC > 24.9:
    print("Cuidado, voce esta acima do peso!")
    
import matplotlib.pyplot as plt
#from pylab import *

dias = range (0, 1, 2)
caloriass = range (0, 461, 1090)
plt.plot(dias, caloriass, label='Calorias consumidas')
plt.plot(dias, formulah, label='Calorias ideais')
plt.axis([0, 2, 0, 1100])
plt.xlabel('dias analisados')
plt.ylabel('calorias consumidas [kcal]')
plt.title('Calorias consumidas') 
plt.show()

proteinass = range (0, p)
plt.plot(dias, proteinass)
plt.xlabel('dias analisados')
plt.ylabel('proteinas consumidas [g]')
plt.title('Proteinas consimidas')  
plt.show()