# Em Python não definimos blocos de código
# Caso seja necessario escrever um código que precisamos que execute mas não podemos escrever
# todas as funções necessarias naquela hora podemos utilizar o pass. Ele finje que existe 
#aguma função, permitindo que o código rode sem erros, apenas dando um resposta vazia ou 
#imcompleta.
valor = False
if valor:
    pass
else:
    print("Tchau")

# Outramaneira de se fazer isso é ulilizando Ellipsis que são 3 pontos. Não é o ideal mas 
# ao menos funciona. 
valor = True
if valor:
    ...
else:
    print("Tchau")