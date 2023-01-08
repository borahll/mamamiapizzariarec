import sys


def doesexist(existlist, originx, originy):
    for element in existlist:
        if str(originx) + str(originy) == element:
            return True
    return False


def isvalid(matrixlenght, x1, y):  # check if the provided x and y are valid in the matrix
    if 0 <= x1 < matrixlenght and 0 <= y < matrixlenght:
        return True
    else:
        return False


def findmax(amatrix):  # function to return the maximum number in a matrix
    max1 = amatrix[0][0]
    for row in amatrix:
        for element in row:
            if max1 < element:
                max1 = element
    return max1


def printmatrix(amatrix):
    for row in amatrix:
        print(" ".join(str(element) for element in row))


def rec(currentline, matrix2):
    if currentline == '':
        return
    temp = currentline.split(" ")
    originx = matrixlen - int(temp[0])
    originy = int(temp[1]) - 1
    serveradius = int(temp[2]) + 1
    visited = []
    visited.clear()
    matrix1 = increment(matrix2, originx, originy, serveradius, visited)
    printmatrix(matrix1)
    following_line = sys.stdin.readline()
    rec(following_line, matrix1)


def increment(matrixin, originx, originy, serveradius, visited):
    if doesexist(visited, originx, originy) or serveradius <= 0 or not isvalid(matrixlen, originx, originy):
        return
    matrixin[originx][originy] += 1
    visited.append(str(originx) + str(originy))
    increment(matrixin, originx + 1, originy, serveradius - 1, visited)
    increment(matrixin, originx - 1, originy, serveradius - 1, visited)
    increment(matrixin, originx, originy + 1, serveradius - 1, visited)
    increment(matrixin, originx, originy - 1, serveradius - 1, visited)
    return matrix


if __name__ == "__main__":
    firstline = sys.stdin.readline()
    x = firstline.split(" ")
    matrixlen = int(x[0])
    numofpizzarias = int(x[1])
    matrix = [[0 for j in range(int(matrixlen))] for i in range(int(matrixlen))]
    secondline = sys.stdin.readline()
    rec(secondline, matrix)
    print(f"The maximum is {findmax(matrix)}")
