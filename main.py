"""
the recursive function signature would be like the following:
    visited = []
    def rec(currentLine, matrix)
        if(EOF):
            return
        x = currentLine.split(" ")
        originx = x[0]
        originy = x[1]
        serveRadius = x[2]
        matrix = increment(matrix, originx, originy, serveRadius, serveRadius + 1, visited)
        rec(theFollowingLine, matrix)
    def increment(matrix, originx, originy, serveRadius, visited)
        dijksstras algorithm?
        if doesExist(visited, originx, originy) or serveRadius <= 0 or not isValid(matrix, originx, originy)
            return
        visited.append(""+originx+originy)
        matrix[originx][originy] += 1
        increment(matrix, originx + 1, originy, serveRadius - 1, visited)
        increment(matrix, originx - 1, originy, serveRadius - 1, visited)
        increment(matrix, originx, originy + 1, serveRadius - 1, visited)
        increment(matrix, originx, originy - 1, serveRadius - 1, visited)
        return matrix
"""
import sys


def doesexist(existlist, originx, originy):
    for element in existlist:
        if "" + originx + originy == element:
            return True
    return False


def isvalid(matrixlen, x1, y):  # check if the provided x and y are valid in the matrix
    if 0 <= x1 < matrixlen and 0 <= y < matrixlen:
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


def rec(currentline, matrix):
    if currentline == '':
        return
    x = currentline.split(" ")
    originx = x[0]
    originy = x[1]
    serveradius = x[2]
    visited = []
    matrix1 = increment(matrix, originx, originy, serveradius, visited)
    following_line = sys.stdin.readline()
    rec(following_line, matrix1)


def increment(matrix, originx, originy, serveradius, visited):
    if doesexist(visited, originx, originy) or serveradius <= 0 or not isvalid(matrix, originx, originy):
        return
    matrix[originx][originy] += 1
    increment(matrix, originx + 1, originy, serveradius - 1, visited)
    increment(matrix, originx - 1, originy, serveradius - 1, visited)
    increment(matrix, originx, originy + 1, serveradius - 1, visited)
    increment(matrix, originx, originy - 1, serveradius - 1, visited)
    return matrix

if __name__ == "__main__":
    firstline = sys.stdin.readline()
    x = firstline.split(" ")
    matrixlen = x[0]
    numofpizzarias = x[1]
    matrix = [[0 for j in range(int(matrixlen))] for i in range(int(matrixlen))]
    rec(sys.stdin.readline(), matrix)
    print(f"The maximum is {findmax(matrix)}")
