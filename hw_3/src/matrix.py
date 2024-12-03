import numpy as np
from copy import deepcopy


class Matrix:
    def __init__(self, data):
        self.data = np.asarray(deepcopy(data))

    def __add__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Bad dimensions")
        res = Matrix(self.data)
        for lhs_row, rhs_row in zip(res.data, other.data):
            if len(lhs_row) != len(rhs_row):
                raise ValueError("Bad dimensions")
            for i in range(len(lhs_row)):
                lhs_row[i] += rhs_row[i]

        return res

    def __mul__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Bad dimensions")
        res = Matrix(self.data)
        for lhs_row, rhs_row in zip(res.data, other.data):
            if len(lhs_row) != len(rhs_row):
                raise ValueError("Bad dimensions")
            for i in range(len(lhs_row)):
                lhs_row[i] *= rhs_row[i]

        return res

    def __matmul__(self, other):
        if len(self.data) == 0 and len(other.data) == 0:
            return Matrix([])

        n, m, k = len(self.data), len(other.data), len(other.data[0])

        res = Matrix(np.zeros((n, k), dtype=self.data.dtype))

        for i in range(n):
            if len(self.data[i]) != len(other.data):
                raise ValueError("Bad dimensions")
            for j in range(k):
                for u in range(m):
                    res.data[i][j] += self.data[i][u] * other.data[u][j]

        return res

    def __str__(self):
        return str(self.data)


np.random.seed(0)

a = Matrix(np.random.randint(0, 10, (10, 10)))
b = Matrix(np.random.randint(0, 10, (10, 10)))

with open("../artifacts/3.1/matrix+.txt", "w") as file:
    file.write(str(a + b))

with open("../artifacts/3.1/matrix*.txt", "w") as file:
    file.write(str(a * b))

with open("../artifacts/3.1/matrix@.txt", "w") as file:
    file.write(str(a @ b))
