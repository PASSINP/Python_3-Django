user = input("Digite a sua senha: ")

# Existe a possibilidade de se verificar a quantidade de caracteres de uma string. Utilizando
# a função len. Que vem de length ou comprimento. Isso poder ser util por exemplo para saber 
# se o usuario esta cumprindo o tamanho da senha que foi requisitado que fosse usado.
# Len não analiza int ou float, apenas string
qtd = len(user)
print(qtd)

if qtd < 6:
    print("Senha muito pequena")
elif qtd == 6:
    print("Aconselho a aumentar a sua senha em no minimo 4 caracteres")
elif qtd > 6 and qtd <= 10:
    print("Poderia ser melhor, mas ja é o suficiente")
else:
    print("Perfeito. Senha segura") 