import numpy

# initializam o matrice de 4 linii si 5 coloane cu tipul datelor double
mat = numpy.zeros([4, 5], dtype="double")

mat[0:4, 0:4] = numpy.genfromtxt("data")

for i in range(4):  # i de la 0 la 4
    mat[i, 4] = numpy.sum(mat[i, 0:4])  # facem pe ultima coloana suma elemenetelor

print("matricea dupa calcul ultima coloana: \n")
print(mat)

matrice_aleator = numpy.random.uniform(0, 1, [5, 3])  # valori intre 0 si 1, matrice de 5 linii si 3 coloane
print(matrice_aleator)

#inmultiti mat cu mat_aleator
newmat = numpy.zeros([len(mat), len(matrice_aleator[0])], dtype="double") # initializam noua matrice

for i in range(len(mat)):   # NR RANDURI PRIMA MATRICE (4)
    for j in range(len(matrice_aleator[0])):    # NR COLOANE A 2-A MATRICE (3)
        for k in range(len(matrice_aleator)):   # NR RANDURI A 2-A MATRICE (5)
            newmat[i, j] = numpy.sum(mat[i, k]*matrice_aleator[k, j])

print("\n", newmat)
