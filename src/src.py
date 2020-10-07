import math
import numpy as np


# Testati ca un numar este prim
def ex1():
    print('Function that tests if a number is prime')
    nr = int(input('Introduce number: '))
    if nr < 2:
        print('Number is not prime!')
        return False
    for div in range(2, int(math.sqrt(nr) + 1)):
        if nr % div == 0:
            print('Number is not prime!')
            return False
    print('Number is prime!')
    return True


# Ordonati cuvintele din fisier-ul urmator: Latin-Lipsum.txt
def ex2():
    file = open('../files/output_file.txt', 'w')

    with open('../files/Latin-Lipsum.txt') as f:
        for t in sorted(i for line in f for i in line.split()):
            if t[-1] in [',', '.']:
                t = t[:-1]
            t = t + '\n'
            file.write(t)
    file.close()


# Data matricea si vectorul, afisati rezulatul produsului lor scalar.
# [                 ]       [    2    ]
# [    1 2  3  4    ]       [   -5    ]
# [   11 12 13 14   ]       [    7    ]
# [   21 22 23 24   ]       [   -10   ]
def ex3():
    matrix = [[1, 2, 3, 4],
              [11, 12, 13, 14],
              [21, 22, 23, 25]]

    vector = [2, -5, 7, -10]

    if len(vector) is not len(matrix[0]):
        print('Functia nu poate sa calculeze produsul scalar;vectorul si matricea nu au aceeasi dimanesiune')
        return 'Failed'

    result = []

    for line in matrix:
        s = 0
        for i in range(len(vector)):
            s += line[i]*vector[i]
        result.append(s)

    print('Produsul scalar este: ', result)
    return {'Success': result}


# Creati matricea si vectorul de mai sus in numpy.
# a. Afisati doar ultimele 2 coloane din primele 2 randuri ale matricei
# b. Afisati ultimele 2 elemente din vector
def npex1():
    matrix = np.array([[1, 2, 3, 4],
                      [11, 12, 13, 14],
                      [21, 22, 23, 25]])
    vector = np.array([2, -5, 7, -10])
    for v in matrix[:2]:
        print(v[-2:])
    print(vector[-2:])


# Creati doi vectori cu numere aleatoare intre 0 si 1 de aceleasi dimensiuni.
# a. Afisati care dintre cei doi vectori are suma elementelor mai are.
# b. Adunati cei doi vectori. Inmultiti cei doi vector (vectorial si scalar).
# c. Calculati radical din fiecare element din vector
def npex2():
    vect1 = np.random.random((1, 5))
    vect2 = np.random.random((5,))
    print('Primul vector este: ', vect1)
    print('Al doilea vector este: ', vect2)
    if np.sum(vect1) > np.sum(vect2):
        print('Vect1 are suma elementelor mai mare!')
    else:
        print('Vect2 are suma elementelor mai mare!')
    print('Vectorul suma este : ', np.add(vect1, vect2))
    print('Produsul scalar al celor doi vectori este: ', np.dot(vect1, vect2))
    print('Produsul vectorial al celor doi vectori este: ', vect1 * vect2)
    print('Radical din fiecare element al primului vector: ', vect1 ** 0.5)


# Creati o matrice cu numere aleatoare intre 0 si 1 de dimensiune 5x5.
# a. Afisati transpusa matricei
# b. Afisati inversa matricei si determinantul.
def npex3():
    matrix = np.random.random((5, 5))
    trnsposed_matrix = np.transpose(matrix)
    determinant = np.linalg.det(matrix)
    inverse = np.linalg.inv(matrix)
    print(matrix)
    print(trnsposed_matrix)
    print(determinant)
    print(inverse)
    return matrix


# Creati un vector de dimensiune 5 cu numere aleatoare:
# a. Afisati produsul scalar intre matricea definite la punctul 3 si vectorul curent
def npex4(matrix):
    array = np.random.random((5,))
    print(np.dot(array, matrix))


if __name__ == '__main__':
    # ex1()
    # ex2()
    # ex3()
    # npex1()
    npex2()
    # matrix = npex3()
    # npex4(matrix)
