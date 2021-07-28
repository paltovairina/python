class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        for line in self.matrix_list:
            for i in line:
                print(f"{i:6}", end="")
            print()
        return str("")

    def __add__(self, other):
        for el in range(len(self.matrix_list)):
            for other_el in range(len(other.matrix_list[el])):
                self.matrix_list[el][other_el] = self.matrix_list[el][other_el] + other.matrix_list[el][other_el]
        return Matrix.__str__(self)


m = Matrix([[3, 2, -4], [1, 7, 3], [0, -8, -2], [2, 2, 5]])
new_m = Matrix([[2, 7, -3], [4, 6, 0], [-1, 1, 5], [4, 7, -2]])
print(m.__add__(new_m))
