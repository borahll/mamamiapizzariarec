import sys


"""
The following code is to find out if the given x and y coordinate exists in the given list
(This function will be used in the algorithm for the path finding)
"""


def doesexist(existlist, originx, originy):
    for element in existlist:
        if str(originx) + str(originy) == element:
            return True
    return False


"""
The following code is to check if the given x and y coordinate is valid
"""


def isvalid(matrixlenght, x1, y):  # check if the provided x and y are valid in the matrix
    if 0 <= x1 < matrixlenght and 0 <= y < matrixlenght:
        return True
    else:
        return False


"""
The following code is to find the maximum element in the matrix
this number will be the result of the input
"""


def findmax(amatrix):  # function to return the maximum number in a matrix
    max1 = amatrix[0][0]
    for row in amatrix:
        for element in row:
            if max1 < element:
                max1 = element
    return max1


"""
The following portion of the code is for debugging purposes 
you can see the matrix(s) content
"""


def printmatrix(amatrix):
    for row in amatrix:
        print(" ".join(str(element) for element in row))


"""
The following code is to recursively go through the file contents
and also increment the provided matrix
"""


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
    following_line = sys.stdin.readline()
    rec(following_line, matrix1)


"""
The following code is the main algorithm of the question.
It works as follows:
    1. If the provided x and y coordinate exists in the list (this list is the visited coordinates in the matrix, stored 
    in a specific manner, eg: x:1 y:2 list item: "12") or the serve radius is smaller than 0 or the given provided x and
    y coordinates are not valid the functions returns
    2. Else the current x and y coordinate of the matrix gets incremented by one and the current location will be 
    appended to the list of visited locations
    3. From the current location the function will recursively try to travel at the 4 different neighbors 
    4. At last the function will return the final matrix
"""


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
    print(f"{findmax(matrix)}")
