import numpy as np

#Exemplos de como usar o pacote numpy do Python para trabalhar com array em data science.

# Criando um array unidimensional
array01 = np.array([2,4,6,7])
print("Array unidimensional: ", array01)

#Criando um array bidimensional
array02 = np.array([[2,3,2],[1,5,8]])
print("Array bidimensional: ", array02)

# Verificando o shape do array - nesse caso, são 2 linhas e 2 colunas
print("Shape do array02: ", array02.shape)

# Verificando a dimensão do array (uni ou bidimensional)
print("Dimensão do array01: ", array01.ndim)
print("Dimensão do array02: ", array02.ndim)

#Verificando qual item do array é maior e menor
print("Maior item do array01: ", array01.max())
print("Maior item do array02: ", array02.max())
print("Menor item do array01: ", array01.min())
print("Menor item do array02: ", array02.min())

#Criando array com o método arange
array03 = np.arange(5)
print("Array com 5 items: ", array03)

array04 = np.arange(0,10,2)
print("Array com start/end de 2 em 2: ", array04)

#Criando usando o método linspace - start, end e número de elementos
array05 = np.linspace(0, 10, 5, dtype=int) #Podemos setar o tipo de elemento com int, float, string, etc.
print("Array com start, end e número de elementos: ", array05)

#Criando array de zeros
array06 = np.zeros((3,3), dtype=int)
print("Array de zeros: ", array06)

#Criando array de 1
array07 = np.ones((3,3), dtype=int)
print("Array de 1: ", array07)

#Criando uma matriz identidade
array08 = np.eye(3)
print("Matriz identidade: ", array08)

#Criando uma matriz diagonal
array09 = np.diag((1,2,3,4))
print("Matriz diagonal: ", array09)

#Criando números aleatórios
np.random.seed(100)
array10 = np.random.rand(5)
print(array10)

#Criando um array vazio
array11 = np.empty((4,4))
print("Array vazio: ", array11)

#Aplicar o tile, ou seja, repetir o array por n vezes, tanto para uma dimensão ou mais
array12 = np.tile(np.array([[9, 4], [3, 7]]), 4)
print("Tile para uma dimensão: ", array12)

array13 = np.tile(np.array([[9, 4], [3, 7]]), (3,3))
print("Tile para duas dimensões: ", array13)

#Operação com arrays

array14 = np.arange(5)
print("Array original: ", array14)
print("Array multiplicado por 2: ", array14 * 2)
print("Array somando 3: ", array14 + 3)
print("Array subtraindo 2: ", array14 - 2)
print("Array dividindo por 2; ", array14 / 2)

#Potência
array15 = np.arange(5)
print("Potência: ", array15 ** 2)

#Cálculo entre arrays
print("Soma: ", array14 + array15)
print("Subtração: ", array14 - array15)
print("Multiplicação: ", array14 * array15)
print("Divisão: ", array14 / array15)
print("Maior ou menor:", array14 > array15) # resultado vai sempre ser booleano

#Acessando os dados do array
print("Posição 2 do array15: ", array15[2])
print("ùltima posição do array15: ", array15[-1])
print("Inverter o array15: ", array15[::-1])

#Criando uma matriz
array16 = np.array([[22, 24, 32], [33, 44, 56], [80, 39, 51]])
print("Pegando a primeira linha: ", array16[0])
print("Pegando a linha 1 e coluna 2: ", array16[1,2])
print("Pegando até a linha 2 exclusiva: ", array16[:2])
print("Pegando a partir da linha 1 inclusiva: ", array16[1:])
