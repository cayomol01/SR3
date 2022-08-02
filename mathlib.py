


class Mathlib(object):
    def __init__(self):
        pass
    def identity(self, size):
        self.matrix = []
        for i in range(size):
            self.matrix.append([])
            for j in range(size):
                if i == j:
                    self.matrix[i].append(1)
                else:
                    self.matrix[i].append(0)
                    
        return self.matrix
    
    def multiply(self, matrix_list):
        self.matrix = []
        matrix1 = matrix_list[0]
        matrix2 = matrix_list[1]
        
        for i in range(len(matrix1)):
            self.matrix.append([])
            for j in range(len(matrix2[0])):
                self.matrix[i].append(0)
                for k in range(len(matrix2)):
                    self.matrix[i][j] += matrix1[i][k] * matrix2[k][j]
                    
                    
        matrix_list[0] = self.matrix
        matrix_list.pop(1)

        if len(matrix_list) > 1:
            self.multiply(matrix_list)

        return self.matrix
    
    def HorVert(self, matrix):
        matrixFinal = []
        for i in range(len(matrix)):
            matrixFinal.append([matrix[i]])
        return matrixFinal

    def VertHor(self, matrix):
        matrixFinal = []
        for i in range(len(matrix)):
            matrixFinal.append(matrix[i][0])
        return [matrixFinal]
