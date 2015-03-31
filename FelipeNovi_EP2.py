# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:35:44 2015

@author: Felipe
"""

import turtle

window = turtle.Screen()    # cria uma janela
window.bgcolor("blue")
window.title("Jogo da Forca")

#importa a lista de palavras
arquivo=open("entrada.txt", encoding="utf-8")
leitura = arquivo.readlines()
lista = [] #criar uma lista limpa
for palavra in leitura: 
    palavraL = palavra.strip()
    if palavraL !="":
        lista.append(palavraL)
#escolher a palavra da lista
from random import choice
palavra_escolhida = choice(lista).lower() #escolhe a palavra
print(palavra_escolhida)
print(len(palavra_escolhida))

forca = turtle.Turtle()  # Cria um objeto "desenhador"
forca.hideturtle
forca.speed(2)  # velocidade do desenho
forca.penup()       
forca.setpos(-250,0)
forca.pendown()
forca.color("yellow")
    
for i in range(1):
    forca.forward(100)
    forca.left(180)  
    forca.forward(50) 
    forca.right(90)
    forca.forward(220)
    forca.right(90)
    forca.forward(100)
    forca.right(90)
    forca.forward(30)
#final do desenho da forca
    
#funções para o corpo do boneco
#desenha a cabeça
def Cabeça():
    cabeca = turtle.Turtle()
    cabeca.hideturtle
    cabeca.speed(5)
    cabeca.penup()
    cabeca.setpos(-100,145)
    cabeca.pendown()
    cabeca.color("pink")
    cabeca.circle(25)

#desenha o corpo
def Corpo():
    corpo = turtle.Turtle()
    corpo.hideturtle
    corpo.speed(5)
    corpo.penup()
    corpo.setpos(-100,145)
    corpo.pendown()
    corpo.color("pink")
    corpo.right(90)
    corpo.forward(70)
    
#desenha o braço direito
def BraçoDireito():
    bracoD = turtle.Turtle()
    bracoD.hideturtle
    bracoD.speed(5)
    bracoD.penup()
    bracoD.setpos(-100,135)
    bracoD.pendown()
    bracoD.color("pink")
    bracoD.right(120)
    bracoD.forward(50)
    
#desenha o braço esquerdo
def BraçoEsquerdo():
    bracoE = turtle.Turtle()
    bracoE.hideturtle
    bracoE.speed(5)
    bracoE.penup()
    bracoE.setpos(-100,135)
    bracoE.pendown()
    bracoE.color("pink")
    bracoE.right(60)
    bracoE.forward(50)
    
#desenha a perna direita
def PernaDireita():
    pernaD = turtle.Turtle()
    pernaD.hideturtle
    pernaD.speed(5)
    pernaD.penup()
    pernaD.setpos(-100,75)
    pernaD.pendown()
    pernaD.color("pink")
    pernaD.right(120)
    pernaD.forward(50)
    
#desenha a perna esquerda
def PernaEsquerda():
    pernaE = turtle.Turtle()
    pernaE.hideturtle
    pernaE.speed(5)
    pernaE.penup()
    pernaE.setpos(-100,75)
    pernaE.pendown()
    pernaE.color("pink")
    pernaE.right(60)
    pernaE.forward(50)
#final das funções do boneco
    
#desenha as "casas" das letras
linhas=turtle.Turtle()
linhas.color("yellow")
linhas.penup()
linhas.setpos(-250,-50)
linhas.pendown()
for i in range(0, len(palavra_escolhida)):
    if i == " ":
            linhas.penup()
            linhas.forward(30)
    if i != " ":   
        linhas.pendown()
        linhas.forward(20)
        linhas.penup()
        linhas.forward(10)
        
#Jogo:
erros = 0
acertos = 0
while erros<6 and acertos<len(palavra_escolhida):
    chute = window.textinput("Chutômetro", "Escolha uma letra")
    while len(chute) != 1:
        chute = window.textinput("Chutômetro", "Escolha uma letra")
    iniciar = 0
    while iniciar != -1:
        iniciar = palavra_escolhida.find(chute, iniciar)    
        if iniciar!=-1:
            linhas.setpos(-250+30*iniciar,-50)
            linhas.write(palavra_escolhida[iniciar],font=("Comic Sans MS",20,"normal"))
            acertos += 1
            iniciar += 1
    #Em caso de erros:
    if chute not in palavra_escolhida:
        erros += 1
        if erros == 1:
            Cabeça()
        if erros == 2:
            Corpo()
        if erros == 3:
            BraçoDireito()
        if erros == 4:
            BraçoEsquerdo()
        if erros == 5:
            PernaDireita()
        if erros == 6:
            PernaEsquerda()
        
window.exitonclick()