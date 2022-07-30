
# media = 7

# materia1 = float(input('Digite sua média na matéria n°1: '))
# materia2 = float(input('Digite sua média na matéria n°2: '))
# materia3 = float(input('Digite sua média na matéria n°3: '))

# if materia1 and materia2 and materia3>= media:
#     print('Aprovado')
# else:
#     print('Reprovado')
# -------------------------------------------------------------------------------------------------------------------
# nome='Iosephvs'
# idade=59
# dinheiro=599.89325
# print("%s é um homem de %d anos, que tem R$ %f atualmente" % (nome,idade,dinheiro))

# String: %s  Float:%f   Int:%d
# -------------------------------------------------------------------------------------------------------------------


# valor_metros= float(input("Digite um valor em metros: "))
# valor_milimetros = valor_metros * 1000

# print("Este valor em milímetros corresponde a:%5.0f milímetros" % (valor_milimetros))
# -------------------------------------------------------------------------------------------------------------------
# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos.
# dias= int(input("Quantidade de dias: "))
# horas= int(input("Quantidade de horas: "))
# minutos= int(input("Quantidade de minutos: "))
# segundos= int(input("Quantidade de segundos: "))
# tempo=  dias/86400 + horas/3600 + minutos/60 + segundos

# print('Você ficou um total de %d dias, %d horas, %d minutos e %d segundos. Total de segundos: %d' %(dias, horas, minutos, segundos, tempo))
# print(f'Você  passou um total de {tempo} segundos')

# -------------------------------------------------------------------------------------------------------------------
"""
Faça um programa que calcule o aumento de um salário. Ele deve
solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
e do novo salário.
"""

# salario = float(input("Digite o seu salário: "))
# aumento = float(input("Digite o aumento salarial: "))
# aumento_total = (aumento/100) * salario
# novo_salario = salario + aumento_total 
# print(f'o acréscimo será de:{aumento_total}. E o novo salário será R$ {novo_salario}')
# print('O acréscimo será de %5.2f novo salário será R$: %5.2f' %  (aumento_total, novo_salario))

# print(f'O salário novo é:'{salario}+{aumento})
# -------------------------------------------------------------------------------------------------------------------
"""
Faça um programa que solicite o preço de uma mercadoria e o percentual
de desconto. Exiba o valor do desconto e o preço a pagar
"""
# preco_produto = float(input("Qual o preço do produto?"))
# percentual_desconto = float(input("O percentual de desconto será?"))
# desconto = percentual_desconto/100 * preco_produto
# valor_total = desconto - preco_produto
# print('O desconto foi de %5.2f' % (desconto))
# print('O preço final do produto com desconto será: %5.2f' % (valor_total))
# -------------------------------------------------------------------------------------------------------------------

"""
Faça um programa que solicite o preço de uma mercadoria e o percentual
de desconto. Exiba o valor do desconto e o preço a pagar
"""

"""
preco_produto = float(input("Qual o preço do produto?"))
percentual_desconto = float(input("O percentual de desconto será?"))
desconto = percentual_desconto/100 * preco_produto
valor_total = preco_produto - desconto
print('O desconto foi de: %5.2f reais' % (desconto))
print('O preço final do produto com desconto será: %5.2f reais' % (valor_total))
"""
# -------------------------------------------------------------------------------------------------------------------

"""
Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""
# distancia_percorrer = float(input('Qual a distância a percorrer?'))
# vel_media = float(input('Qual a velocidade media esperada para a viagem?'))
"""
# -------------------------------------------------------------------------------------------------------------------

Escreva um programa que converta uma temperatura digitada em
°C em °F. A fórmula para essa conversão é:


"""
# temperatura = float(input('Digite a temperatura em C°: '))
# c_converter = (9 * temperatura) /5 + 32
# print('A temperatura em C° corresponde a: %5.1f.\n------------------------------------------------\nE a temperatura em F° é: %5.1f.' % (temperatura, c_converter))

"""
Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais
o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
dia e R$ 0,15 por km rodado.
"""
# km_percorrido = float(input('Quantos quilômetros percorridos? '))
# dias_alugados = int(input('Quantos dias alugados?'))
# pagamento = km_percorrido * 0.15 + dias_alugados * 60
# print('Considerando que percorreu %5.2f km e foi alugado por %d dias, o total a pagar será: R$ %5.2f ' % (km_percorrido, dias_alugados, pagamento))

"""
Escreva um programa  para calcular a redução do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""
# qtd_cigarros = int(input('Quantos cigarros fumados diariamente: '))
# anos_fumando = int(input('Quantos anos fumando: '))
# calculo_tempo = (qtd_cigarros *10) * (anos_fumando * 365)
# converte_dia = (calculo_tempo /60) /24
# print('Se você fuma %d cigarros por dia, há %d anos, perdeu %d minutos da sua vida. %d em dias.' % (qtd_cigarros, anos_fumando, calculo_tempo, converte_dia))
# -------------------------------------------------------------------------------------------------------------------

"""
Escreva programa que leia 3 numeros e imprima o maior e o menor.
"""
# n1 = int(input('valor 1: '))
# n1 = int(input('valor 2: '))
# n3 = int(input('valor 3: '))

# if n1> n2 > n3:
#     print(n1,n3)
# if n1<n2<n3:
#     print(n3, n1)
# if n2>n3>n1:
#     print(n2,n1)
# elif n2>n1>n3:
#     print(n2,n3)
# else:
#     ('zzzzz')
# -------------------------------------------------------------------------------------------------------------------

"""
Escreva um programa que pergunte o salário do funcionário e calcule
o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
10%. Para os inferiores ou iguais, de 15%.
"""

# salario = float(input('Qual o seu salário? '))
# salario_base = salario  
# aumento = 0
# salario_aumentado = 0

# if salario_base >1250:
#     aumento = aumento + salario_base * 0.10
#     salario_aumentado = salario_aumentado + salario + aumento
#     print('Salário aumentado: R$ %5.2f ' % (salario_aumentado))

# if salario_base <= 1250:
#     aumento = aumento + salario_base * 0.15
#     salario_aumentado = salario_aumentado + salario + aumento
#     print('Salário com aumento: R$ %5.2f '%(salario_aumentado))

# -------------------------------------------------------------------------------------------------------------------
"""
Escreva um programa que pergunte a distância que um passageiro
deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
"""
# distancia_percorrer = float(input('Distância a ser percorrida em km: '))
# distancia_base = distancia_percorrer
# preco = 0
# if distancia_base <= 200:
#     preco = preco + distancia_base * 0.50
#     print('O preço é: %5.2f reais' % (preco))
# else:
#     preco = preco + distancia_base * 0.45
#     print('O preço é: %5.2f reais' % (preco))
"""
# -------------------------------------------------------------------------------------------------------------------

Abaixo de 200
minutos, a empresa cobra R$ 0,20 por minuto. Entre 200 e 400 minutos, o preço
é de R$ 0,18. Acima de 400 minutos, o preço por minuto é de R$ 0,15.
"""
# minutos = int(input('minutos utilizados no mês: '))
# if minutos < 200:
#     preco = 0.20

# else:
#     if minutos < 400:
#         preco = 0.18

#     else:
#         preco = 0.15

# print('Você vai pagar este mês: R$ %6.2f' %(minutos * preco))
# -------------------------------------------------------------------------------------------------------------------
# n1 = int(input('Digite primeiro numero: '))
# n2 = int(input('Digite primeiro segundo: '))
# operador = str(input('Digite um operador (+) (-) (*) (/): '))

# if operador == "+":
#     print(n1+n2)

# elif operador == "-":
#     print(n1-n2)
# elif operador == "*":
#     print(n1*n2)
# elif operador == "/":
#     print(n1/n2)
# else:
#     print('operação inválida')
# -------------------------------------------------------------------------------------------------------------------

"""
Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
casa a comprar dividido pelo número de meses a pagar.
"""
# valor_casa = int(input('Valor da casa: '))
# salario = int(input('Salário: '))
# anos_pagar = int(input('Quantos anos para pagar: '))
# prestacao_mensal = valor_casa / (anos_pagar * 12)
# print('Prestação Mensal:R$ %5.2f' % (prestacao_mensal))

# if prestacao_mensal < salario * 0.30:
#     print('Aprovado')

# else:
#     print('reprovado')
# -------------------------------------------------------------------------------------------------------------------
"""
Modifique o programa para exibir os números de 1 a 100.
"""
# x=1
# while x< 101:
#     print(x)
#     x= x+ 1
# -------------------------------------------------------------------------------------------------------------------

"""
Modifique o programa para exibir os números de 50 a 100.
"""
# x=50
# while x <101:
#     print(x)
#     x += 1
# -------------------------------------------------------------------------------------------------------------------

"""
Faça um programa para escrever a contagem regressiva do lançamento
de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.
"""

# x=10
# while x >0:
#     print(x)
#     x-= 1 
# print('fogo')

# fim = int(input('Digite um numero: '))
# x = 1 
# while x <= fim:
#     print(x)
#     x += 1

