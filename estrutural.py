# Aula 2
# Como o Python diferencia letras maiúsculas de minúsculas a função Print() não executa. O certo é print()
print("hello", "World", sep="-")  # O comando sep serve para separar as strings com o texto inserido
print("texto 1", end=" Junta ")   # o comando end junta o print da linha com o print imediatamente abaixo
print("texto 2")

# Aula 3

print("isso é uma \"string\" (str)")  # Aqui foi utilizada a "\" como caractere de escape (o caractere seguinte perde a função)
print("Esse texto será \n quebrado")  # o cimando \n quebra o comando print em 2 linhas.
print(r"Esse texto será \n quebrado") # o "r" antes das aspas no comando print inibe a execução de qualquer comando
print(type("string"))  # função type define a classe do objeto
print(bool(0), bool([]), bool(""))  # vazios configuram falso no booleano
print("Luiz", type("Luiz"), bool("Luiz"), type(bool(("Luiz"))))  # type casting para mudar o tipo do dado
print("10", type("10"), int("10"), type(int("10")))  # mais um exemplo de type casting
print("10" + "10")  # concatenação


# aula 7 - formatação de strings

imc = 25.3
nome = 'heinz'
idade = 20

print(f'meu nome é {nome}, tenho {idade} e meu imc é {imc:.2f}')  # utilização de f strings
print('meu nome é {}, tenho {} e meu imc é {}'.format(nome,idade,imc))
print('meu {0} nome é {0}, tenho {1} e meu imc {1} é {2}'.format(nome, idade,imc))  # outra forma de usar o .format()
print('meu nome é {n}, tenho {i} e meu imc é {im}'.format(n = nome, i = idade,im = imc))  # parâmetros nomeados no .format

# aula 10

if True:
    print('verdadeiro')

if False:
    print('false')
print('não é verdadeira')