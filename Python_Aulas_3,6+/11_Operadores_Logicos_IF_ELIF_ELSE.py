"""
Operadores lógicos
and, or, not, in e not in
"""

# O operador lógico and serve para verificar se dueas ou mais condições são verdadeiras antes
# de dar resultado verdadeiro. Se uma das partes der false, tudo da false, mesmo que exista
# algum resultado true ali dentro.
a = 2
b = 2
c = 3
d = 3
e = 4

if a == b and c == d:
    print('Verdadeiro')
else:
    print('Falso')

# O operador lógico or serve para verificar se ao menos uma das condições é verdadeira. 
# Diferente do and, no or, uma true supera o fato de ter outras false e da resultado true
if a == e or c == d:
    print('Verdadeiro')
else:
    print('Falso')

# E como os operadores lógicos é possivel montar uma verificação de algo
age = int(input('Digite sua idade: '))

idade_menor = 18
idade__maior = 90

if age >= idade_menor and age <= idade__maior:
    print('Pode andar de jetski em alta velocidade')
else:
    print('Se você conseguir. Só não recomendo')

# O operador lógico not não precisa de duas ou mais expressões, apenas uma. Ele é um operador
# inversor. Ele "inverte" o valor. No caso true por false e false por true. Isso pode ser 
# ser util por exmplo para saber se um campo esta vazio. 
x = ''
if not x:
    print('Campo vazio. Por favor preencha com algo')

# O operador lógico in e not in tem a função de verificar se tem algo dentro ou se não tem 
# algo dentro

nome = 'Paulo'

if 'u' in nome:
    print("Seu nome tem a letra u")

if 'V' not in nome:
    print("Seu nome não tem a letra V")