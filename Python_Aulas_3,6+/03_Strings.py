# Tudo em Python é considerado um objeto.
# String pode ser definido por str - string.
# Python é uma linguagem interpretada. Por isso se você utilizar texto sem aspas
# (string), pois se não utilizar ele vai achar que é ua função, como ela nã existe
# vai dar erro
print("Podemos utilizar aspas duplas")
print('Ou aspas simples')

# Não faça isso.
#print("Esse é um erro com "string" (str).")

# Quado você utiliza a segunda aspas o texto fecha, você querendo ou não. Apesar
# da sua intenção de colocar string entre aspas, a linguagem acha que você esta 
# tentando fazer outra coisa. Para dar certo você tem de misturar as aspas. No
# caso, abrir o texto com aspas simples, para que as aspas duplas estejam livres
# para serem usadas no texto ao inves de fechar um trecho na função
print('Esse é o metodo correto de utilizar "string", viu? Sem erros')

# Na verdade é por isso que tutorial gringo tende a utilizar aspas duplas, pois 
# para varias palavras eles utilizam aspas simples, como It's ou haven't

# Mas se por alguma razão você precisar utilizar tanto aspas simples quanto aspas 
# duplas em seu texto, isso é possivel. Graças ao caractere de escape. Ao 
# utilizar o caractere de escape, o interpretador entende que você não esta
# dando um fim ao colocar aquelas aspas, entende que apenas esta as
# adicionando em seu texto. O unico defeito é que é um pouco feio e as vezes pode
# ser um pouco confuso de se trabalhar com ele. 
# Só para garantir. Barra invertida \ antes de cada uma das aspas que você precisa
 #que sejam utilizadas
print("Esse é um erro com \"string\" (str).")

# E uma coisa boa, mas que deve se tomar cuidado, é o fato de ser possivel pular
# uma linha utilizando caractere de escape com n. E isso é como dar um enter num
# documneto de texto, ou seja se você der espaço depois, o texto não ira ficar
# no canto da tela ele tera um espaço
print("Isso vai \npular uma linha")
print("Isso vai \n pular uma linha e dar um espaço")
