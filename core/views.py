from django.shortcuts import render
from django.http import HttpResponse

def nome(request, nome):
    return HttpResponse('O nome recebido é '+nome)

def idade(request, idade):
    return HttpResponse('Você tem '+str(idade) + ' anos e nasceu em '+ str(2022-idade))

def media(request, valor1, valor2):
    resultado = (float(valor1) + float(valor2))/2
    if resultado > 60: 
        return HttpResponse('Sua média é ' + str(resultado) +' APROVADO')
    else:
        return HttpResponse('Sua média é ' + str(resultado) +' REPROVADO')

    
    


