def convertToList(mat):#if its empty it return an empty list
    mat = mat[1:len(mat) - 1]
    if not len(mat):
        return []
        
    matrix = []
    mat = mat.split(',')
    for row in mat:
        matrix.append(row.split(' '))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])
    return matrix


def isValidMatrix(mat):#if its not valid it returns False otherwise i returns a list that first and second member of it are length of rows and length of each row
    lenRows = len(mat)
    if (not lenRows):
        return [0,0]
    lenRow = len(mat[0])
    for i in range(1, lenRows):
        if len(mat[i]) != lenRow:
            return False
    return [lenRows, lenRow]
def canAdd(mat1,mat2):#check if the matrix is square
    if mat1[0]==mat2[0] and mat1[1]==mat2[1]:
        return True
    return False
def addMatrix(mat1,mat2,op='+'):#returns False if invalid matrix and returns -1 if couldnt add and returns empty list if both were empty matrixes
    lenMat1=isValidMatrix(mat1)
    lenMat2=isValidMatrix(mat2)
    if not lenMat1 or not lenMat2 :
        return False
    if not lenMat1[0] and not lenMat2[0]:
        return []
    if not lenMat1[0]:
        return mat2
    if not lenMat2[0]:
        return mat1
    if not canAdd(lenMat1,lenMat2):
        return -1
    mat=[[0 for x in range(lenMat1[1])] for y in range (lenMat1[0])]
    for x in range(lenMat1[0]):
        for y in range (lenMat1[1]):
            if(op=='+'):
                mat[x][y]=mat1[x][y] + mat2[x][y]
            else:
                mat[x][y] = mat1[x][y] - mat2[x][y]
    return mat


def convertToReadable(mat):#this function converts 2D list (matrix) to a readable string

    if mat==-1:
        return "couldn't add"
    if mat==False:
        return 'invalid matrix'
    lenRows=len(mat)
    if(not lenRows):
        return '[]'

    lenRow=len(mat[0])
    readable='['

    for i in range(lenRows):
        for j in range(lenRow):
            readable+=str(mat[i][j])
            if j+1!=lenRow:
                readable+=' '
        if i+1!=lenRows:
            readable+=','

    readable+=']'

    return readable

def run(mat1,op,mat2):
    mat1=convertToList(mat1)
    mat2=convertToList(mat2)
    mat=addMatrix(mat1,mat2,op)
    return [convertToReadable(mat)]

print(run(input(),input(),input()))
