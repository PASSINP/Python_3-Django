# Como em qualquer linguagem de programação, a abertura e fechamento de aspas
# ocorrem quando existe uma função. No caso do Python, também ocorre quando é uma
# classe.
# Cada função é executada individualmente. A não ser que você a junte de alguma
# maneira elas não irão trabalhar juntas. No caso do print. Cada  comando print 
# que for dado ira mostrar uma linha e não todas e nem ira juntar o conteudo das
#linhas anteriores.
print(123456)

# É possivel enviar mais de um argumento para uma string. Por padrão o comando
# ja vai dar um espaço. Mas não é sempre. Então cuidado pois algumas ações não
# geram espaço.
print('Paulo', 'ASC', 'Programador')

# Existe a possibilidade de se colocar um separador dentro de um print
print('Paulo', 'ASC', sep='-')

# Temos 2 possibilidades de colocar um item no fim de um print. Ou por definir
# uma ordem colocando o fim que você quer ou por usar end
print('Paulo', 'ASC', end='-')

# Python sabe diferenciar letra minuscula de maisucula ou seja. Print() não existe.
# Apenas print() existe. A não ser que criemos ua função Print() que sirva para 
# dar print()
