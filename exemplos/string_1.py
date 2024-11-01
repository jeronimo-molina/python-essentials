# Atribuição literal no objeto

first = "Dave"
last = "Smith"

# Verificando tipos de dados
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Métodos de String
print(first)
print(first.lower())  # Imprime o valor de 'first' em letras com a minúsculas.
print(first.upper())  # Imprime o valor de 'first' em letras maiúsculas.

pizza = str("Pepperoni")  # Atribuição como parãmetro

# Concatenação de Strings
fullname = first + " " + last
print(fullname)

# Interpolação de Strings
fullname = f"{first} {last}"
print(fullname)

# Interpolação de Strings com métodos
fullname = f"{first.upper()} {last.upper()}"
print(fullname)

# Transformar um número em uma string
decade = str(1980)
print(type(decade))
print(decade)

# Frases (statement)
statement = "I was born in " + decade + "s."
print(statement)

# Múltiplas linhas

multiline = '''

Hey, how are you?

I was just thinking about you.

		I hope you are doing well.

'''

print(multiline)

# O código realiza três operações na variável 'multiline':
# 1. Imprime o valor de 'multiline' com a primeira letra de cada palavra em maiúscula.
# 2. Substitui todas as ocorrências da palavra "well" por "great" e imprime o resultado.
# 3. Imprime o valor original de 'multiline'.
print(multiline.title())
print(multiline.replace("well", "great"))
print(multiline)

# Utilizando caracteres especiais com escape

sentence = 'I\'m a "good" student.\tHey!\n\nWhere\'s the bathroom?'
print(sentence)

# Tamanho de uma string
print(len(multiline))
multiline += "                              "
multiline = "                           " + multiline
print(len(multiline))

# Removendo espaços em branco
print(multiline.strip())
# Remove espaços em branco à direita e à esquerda
print(len(multiline.strip()))
print(len(multiline.rstrip()))  # Remove espaços em branco à direita
print(len(multiline.lstrip()))  # Remove espaços em branco à esquerda

# Dividindo uma string
words = multiline.split()
print(words)
print(len(words))

# Dividindo uma string com base em um caractere específico
words = multiline.split("a")
print(words)
print(len(words))

# Criando um texto com base em uma lista de strings
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Pie".ljust(16, ".") + "$5".rjust(4))
print("Chesecake".ljust(16, ".") + "$8".rjust(4))

# Indexador de string
print(first[0])  # Primeira posição no index
print(first[1])
print(first[-1])  # To get last value in the string
print(first[1:-1])  # To get the second letter to the second to last letter
print(first[0:])  # To get the last value on a string
