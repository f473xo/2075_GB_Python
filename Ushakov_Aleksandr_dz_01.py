class Matrix:
    def __init__(self, matrix: list[list]):
        self._matrix = matrix
        _matrix_length = len(self._matrix)
        self._matrix_size = set([(_matrix_length, len(row)) for row in self._matrix])

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self._matrix])

    def __add__(self, other):
        lst = []
        for i in zip(self._matrix, other._matrix):
            lst.append([sum([el1, el2]) for el1, el2 in zip(*i)])
        return Matrix(lst)


first_matrix = Matrix([[31, 22], [37, 43], [51, 86]])
print(first_matrix, '\n')

second_matrix = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(second_matrix, '\n')

third_matrix = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(third_matrix, '\n')

print(first_matrix + second_matrix + third_matrix)
