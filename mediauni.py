#!/bin/python3 #seleciona o interpretador python3
n1=float(input(" digite a primeira nota ")) #nota da primeira unidade 
n2=float(input("digite a segunda a segunda nota ")) #nota da segunda unidade #otimização semantica para ecnomizar memória testamos primeiro a condição de recuperação
media=(n1+n2)/2
if (media>3) and (media<7):
    print("recuperacao")
    rec=float(input("digite a nota da recuperação "))
    #calculo da media da recuperacao
    mrec=(rec+media)/2
    if mrec<5:
        print("lamento")
    else:
        print("parabéns")
elif media>7:
    print("passou! parabéns")
else:
    print("lamento")


