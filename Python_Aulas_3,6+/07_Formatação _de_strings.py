nome = 'Paulo'
idade = 21
altura = 1.89

# Exsitem algumas manerieas de se fazer concatenação. Uma delas, que foi 
# implementada na Versão 3.6 do Python, se chama f string. 
# Para se fazer isso, se começa colocando f antes das aspas. Em seguida você
# coloca entre chaves a variavel que deseja utilizar {assim}
print(f' Ola {nome}, me disseram que você tem {idade} anos e {altura} metros de altura')

x = 3.14159265359
g = 8001

# Outra coisa que podemos utilizar na formatação é dimuir numeros(ou palavras) 
# muito longos. Utiliza junto a f string. 
print(f'{x:.2f}')
print(f'{nome:.2s}')

# Caso seja necessaria uma concatenação em uma versão mais antiga do Python da
# para se fazer este tipo de concatenação. Aviso, não sei se vale para Python 2.
# Para fazer isso iremos colocar chaves dentro do texto, e com o auxilio da função
# ajudante .format iremos definir as variaveisa serem utilizadas naquele espaço
# e sua ordem
print('{} tem {} anos e tem {} de altura'.format(nome, idade, altura))

# Outra coisa que pode ser feita caso se utilize este tipo de concatenação é
# colocar a posição do que esta dentro do .format
# E vale ressaltar que posição começa em 0 e não 1
print('{0} {2} {2} tem {1} {0} anos e tem {2} de altura'.format(nome, idade, altura))