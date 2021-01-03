"""
Operadores Relacionais. Eles fazem comparações de valores. Não obrigatoriamente numeros, pode
ser um texto ou dado, como login
== - Igual a. Ja que um = é utilizado para criar variaveis, para verificações de igualdade se
utiliza 2 iguais

> - Maior que

>= = Maior ou igual

< - Menor que

<= - Menor ou igual

!= - Diferente
"""
# Cono descrito a cima os operadores relacionais comparam valores ou algum outro tipo de
# dado
print(2 == 2)
print('V' == 'V')


# Como tudo em Python, operadores relacionais são sensiveis a tipos de dados. Ou seja o
# exemplo a seguir vai dar false. E tambem ele é case sensitive, ou seja sabe se a letra é
# minuscula ou maiscula.
print (2 == '2')
print ('v' == 'V')

# Também é possivel fazer com que uma variavel contenha uma comparação
num_1 = 2
num_2 = 2

comp = num_1 == num_2
print (comp)


# É possivel utilizar operadores condicionais como condição no if, elif e else. Para isso
# colocamos o que queremos analizar e alguma base. Por exemplo: Pegar o input do usuario e
# verificar se ele ou ela é menor ou maior de idade.

nome = input("Qual o seu nome ")
idade = int(input("Qual a sua idade "))

if idade > 18:
    print (f"Ola {nome}, você é maior de idade")
elif idade ==  18:
    print (f"Bem em cima {nome}")
else:
    print (f"Desculpe {nome}. Menores não entram")


