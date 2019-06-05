from fractions import Fraction
import itertools


def Input():
    matrix = []
    print('Введите в первой строке количество  строк и столбцов(через пробел):')
    m, n = map(int, input().split())
    print('Вводите строки по очереди,с пробелами между цифрами:')
    for i in range(0, m):
        matrix.append(list(map(Fraction, input().split())))
    return m, n, matrix


def Sum_Matrix():
    m1, n1, mat1 = Input()
    m2, n2, mat2 = Input()
    results_matrix = []
    if n1 != n2 and m1 != m2:
        print('Матрицы не соразмерны!Попробуйте ещё раз!')
        return False
    for q in range(0, m1):
        str = []
        for t in range(0, n1):
            str.append(mat1[q][t] + mat2[q][t])
        results_matrix.append(str)
    return results_matrix


def Multiplication_Matrix():
    m1, n1, mat1 = Input()
    m2, n2, mat2 = Input()
    results_matrix = []
    if n1 != m2:
        print('Длинна строки первой матрицы не совпадает с длинной столбца второй!Попробуйте ещё раз!')
        return False
    for i in range(0, m1):
        str = []
        for k in range(0, m1):
            element_matrix = 0
            for l in range(0, n2):
                element_matrix += (mat1[i][l] * mat2[l][k])
            str.append(element_matrix)
        results_matrix.append(str)
    return results_matrix


def Transpose_Matrix():
    m, n, matrix = Input()
    result_matrix = []
    for i in range(0, n):
        str = []
        for l in range(0, m):
            str.append(matrix[l][i])
        result_matrix.append(str)
    return result_matrix


def Output(matrix):
    if not matrix:
        return
    else:
        for i in matrix:
            print(*map(Fraction, i))
            #заменить первый аргумент на float или Fraction, в зависимости от того, какой формат требуется)
        return


def El_Transformation1(matrix, m1, m2, n, s, gamma):
    for i in range(s, n):
        matrix[m1][i] -= (matrix[m2][i] * gamma)
    return matrix


def El_Transformation2(matrix, m1, m2, n):
    for i in range(0, n):
        matrix[m1][i], matrix[m2][i] = matrix[m2][i], matrix[m1][i]
    return matrix


def El_Transformation3(matrix, m, n, gamma):
    for i in range(0, n):
        matrix[m][i] = (matrix[m][i] * gamma)
    return matrix


def SLU():
    m, n, matrix = Input()
    s = 0
    null_str = m - 1
    for i in range(0, n - 1):
        for k in range(m - 1, s - 1, -1):
            if matrix[k][i] == 0:
                matrix = El_Transformation2(matrix, k, null_str, n)
                null_str -= 1
        for k in range(m - 1, s, -1):
            if matrix[k][i] != 0 and matrix[s][i] != 0:
                gam = matrix[k][i] / matrix[s][i]
                matrix = El_Transformation1(matrix, k, s, n, s, gam)
        s += 1
        null_str = m - 1
    return matrix

def InvertibleMatrix():
    m, n, matrix = Input()
    new_matrix = [[0] * m for i in range(n)]
    detA = Det(matrix, m)
    for i in range(0, m):
        for j in range(0, m):
            algadd = AlAdd(matrix, i, j, m)
            new_matrix[i][j] = Det(algadd, len(algadd[0])) / detA * pow(-1, i + j)
    result_matrix = []
    for i in range(0, n):
        str = []
        for l in range(0, m):
            str.append(new_matrix[l][i])
        result_matrix.append(str)
    return result_matrix


def AlAdd(matrix, a, b, n):
    new_matrix = [[0] * (n - 1) for i in range(n - 1)]
    for i in range(n):
        for j in range(n):
            if i < a:
                if j < b:
                    new_matrix[i][j] = matrix[i][j]
                elif j > b:
                    new_matrix[i][j - 1] = matrix[i][j]
            elif i > a:
                if j < b:
                    new_matrix[i - 1][j] = matrix[i][j]
                elif j > b:
                    new_matrix[i - 1][j - 1] = matrix[i][j]
    return new_matrix

def Det(matrix, m):
    per = list(itertools.permutations(range(0, m)))
    det = 0
    for i in per:
        j = 0;
        el = pow((-1), Inv(i))
        for q in i:
            el *= matrix[j][q]
            j += 1
        det += el
    return det

def Inv(per):
    inv = 0
    for i in range(0, len(per)):
        for j in range(i, len(per)):
            if per[i] > per[j]:
                inv += 1;
    return inv

while True:
    print('Введите нужную вам операцию (+,*,T,SLU, Invertible,exit)')
    operation = input()
    if operation == 'exit':
        exit()
    elif operation == '+':
        Output(Sum_Matrix())
    elif operation == '*':
        Output(Multiplication_Matrix())
    elif operation == 'T':
        Output(Transpose_Matrix())
    elif operation == 'SLU':
        Output(SLU())
    elif operation == 'Invertible':
        Output(InvertibleMatrix())
    else:
        print('Неизвестная операция.Попробуйте ещё раз.')
