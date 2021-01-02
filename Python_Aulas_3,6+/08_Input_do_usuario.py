# Em diversas ocasiões, precisaremos pedir um input ao usuario. Para isso iremos
# utilizar a função input(). Ela ira se omunicar com o usuario e ira extrair 
# as informações que precisamos. Nesse caso não da espaço depois do que você 
# escreve. Portanto de um espaço manualmente antes da segunda aspas. 
input("Qual o seu nome? ")

# Podemos armazenar um input dentro de uma variavel. Um input sempre sera uma
# string, mesmo que seja digitado um numero ou boolean.
nome = input("Qual é o seu nome? ")

print(nome)

# Existe uma maneira de converter o tipo de dado. Coloque o tipo que você precisa
# em forma de função e a funç~çao input dentro
idade = int(input("Digite sua idade: "))

print(idade)