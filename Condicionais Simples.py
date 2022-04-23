# nome = str(input('Qual o seu nome? '))
# if nome == 'Gustavo':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal')
# print('Bom dia {}'.format(nome))

# nota1 = float(input("Digite sua primeira nota: "))
# nota2 = float(input('Digite sua segunda nota: '))
# m = (nota1 + nota2)/2
# if m >= 5:
#     print('Sua média foi {:.1f}, parabéns você foi aprovado!'.format(m))
# else:
#     print('Sua média foi baixa, continue estudando, você foi reprovado!')


#Escreva um programa que faça o computador pensar em um número inteiro de 0 a 5, e peça para o usuário
#tentar descobrir qual foi o número escolhido pelo computador, o programa deverá escrever na tela se
#usuário ganhou ou perdeu!
#

# from random import randint
# computador = randint(0,5)
# jogador= int(input('Que número você acha que o computador escolheu? '))
# if computador == jogador:
#    print('Parabéns Você acertou!')
# else:
#     print('Tente de novo até acertar, eu pensei no número {}, e não no número {}'. format(computador,jogador))


# --------------CALCULODE VELOCIDADE COM APLICAÇÃO DE MULTA-----------------
# vel = float(input('Digite a velocidade atual do carro: '))
# if vel > 80:
#     print('MULTADO! Você excedeu o limite de velocidade que é de 80 km/h')
#     multa = (vel-80) * 7
#     print('O valor da sua multa foi de R$ {:.2f}'.format (multa))
# print('Tenha um bom dia, dirija com segurança')


#Crie um programa que leia um número inteiro e informe se ele é Par ou Impar!
# num = int(input('Digite um número qualquer para saber se é par um impar: '))
# resultado = num % 2
# if resultado == 0:
#     print('O número {} é par.'.format(num))
# else:
#     print('O numero {} é impar.'.format(num))

# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$ 0,50 por km para viagem até 200km e R$ 0,45 para viagens mais longas.

# viagem = float(input('Qual a distância da sua viagem em km? '))
# d1 = viagem * 0.50
# d2 = viagem * 0.45
# if viagem <= 200:
#     print('O valor da sua passagem é de R$ {:.2f}'. format(d1))
# else:
#     print('O valor da sua passagem é de R$ {:.2f} '.format(d2))


#OUTRA FORMA DE RESOLVER O MESMO PROBLEMA-----------------------------------------
# viagem = float(input('Qual a distância da sua viagem em km? '))
# if viagem <= 200:
#     valor = viagem * 0.50
# else:
#     valor = viagem * 0.45
# print('O valor de sua passagem é de R$ {:.2f} '.format(valor))


#FAÇA UM PROGRAMA QUE PEGUE UM ANO QUALQUER E DIGA SE ELE É BISSEXTO! ---------------

# from datetime import date
# ano = int(input('Digite um ano para saber se é Bissexto, ou coloque 0 para saber sobre o ano atual: '))
# if ano == 0:
#     ano = date.today().year
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print('O ano {} é Bissexto'.format(ano))
# else:
#     print('O ano {} não é Bissexto'.format(ano))

#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais o aumento é de 15%.

# sal = float(input('Qual o valor do seu salário atual? R$  '))
# print('Meu salário atual é de R$ {:.2f}'.format(sal))
# if sal <= 1250:
#     aumento = (sal * 115) / 100
#     print('Seu aumento será de 15% e você ganhará R$ {:.2f}'.format(aumento))
# else:
#     aumento = (sal * 110) / 100
#     print('Seu aumento será de 10% e você ganhará R$ {:.2f}'.format(aumento))

#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

lado1 = int(input('Digite o primeiro lado do triângulo: '))
lado2 = int(input('Digite o segundo lado do triângulo: '))
lado3 = int(input('Digite o terceiro lado do triângulo: '))
print('Você digitou {}, {} e {}'.format(lado1, lado2, lado3))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('\033[1;33mEstes números podem formar um triângulo\033[m')
else:
    print('\033[34;40mEstes números não podem formar um triângulo\033[m')

