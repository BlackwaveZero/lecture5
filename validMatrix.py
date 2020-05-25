def isValidMatrix(mat):
    if(mat==False):
        return '0,0'
    lenRow=len(mat[0])
    lenRows=len(mat)
    for i in range(1,lenRows):
        if len(mat[i])!=lenRow:
            return 'invalid matrix'
    return str(lenRows)+','+str(lenRow)
def convertToList(mat):
    matrix=[]
    mat=mat[1:len(mat)-1]
    if not len(mat):
        return False
    mat=mat.split(',')
    for row in mat:
        matrix.append(row.split(' '))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j]=int(matrix[i][j])
    return matrix

print(isValidMatrix(convertToList(input())))
