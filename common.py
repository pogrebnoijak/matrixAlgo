from generate import*
from re import findall
from math import sqrt


def E(n): return Matrix([[1 if i == j else 0 for i in range(n)] for j in range(n)])

class Matrix:
    eps = 1e-6
    def __init__(self, smth = "generate.txt"):
        if (type(smth) is list):
            self.A = smth
        elif (type(smth) is str):
            self.A = []
            with open("conclusion/" + smth, 'r') as f:
                line = f.readline()
                n = int(findall(r"\d+", line)[0])
                isC = findall(r"C", line) != []
                if isC:
                    temp = r'(?:\(-?\d+\.\d+|\(-?\d+|)[+-]?(?:\d+\.\d+|\d+)j\)|[+-]?(?:\d+\.\d+|\d+)j'
                    for i in range(n):
                        self.A.append(list(map(complex, findall(temp, f.readline()))))
                        print(self.A[i])
                else:
                    temp = r'(?:-?\d+\.\d+|-?\d+)'
                    for i in range(n):
                        self.A.append(list(map(float, findall(temp, f.readline()))))
        else:
            raise Exception(f"Need path to file or [[]], but value: {smth}")

    def __getitem__(self, i):
        return self.A[i]

    def printM(self, path = "res.txt", accuracy = 3):
        roundd = self.__roundd()
        with open("conclusion/" + path, 'w') as f:
            f.write(str(len(self)) + " " + str(len(self.A[0])) + (" C" if self.isCMatrix() else "") + "\n")
            for i in range(len(self)):
                f.write(str(list(map(lambda x: roundd(x, accuracy), self.A[i]))) + "\n")

    def printC(self, accuracy = 3):
        lam = lambda x: self.__roundd()(x, accuracy)
        for i in range(len(self)):
            print(list(map(lam, self.A[i])))
        print("-" * 100)

    def __xor__(self, other):
        assert(other == "T")
        new_A = []
        for j in range(len(self.A[0])):
            new_A.append([self.A[i][j] for i in range(len(self))])
        return Matrix(new_A)

    def __mul__(self, other):
        if (type(other) == int or type(other) == complex):
            return self.__skal_mul(other)
        else:
            n, m, k = len(self), len(other), len(other.A[0])
            assert(len(self.A[0]) == m and "wrong size of matrices")
            return Matrix([[sum([self.A[i][l] * other.A[l][j] for l in range(m)])
                for j in range(k)] for i in range(n)])

    def __rmul__(self, k):
        return self.__skal_mul(k)
    
    def __add__(self, other):
        n, m = len(self), len(self.A[0])
        assert(len(other) == n and "wrong size of matrices")
        assert(len(other.A[0]) == m and "wrong size of matrices")
        return Matrix([[self.A[j][i] + other.A[j][i] for i in range(m)] for j in range(n)])

    def __neg__(self):
        return self.__skal_mul(-1)

    def __sub__(self, other):
        return self + (-other)

    def __isub__(self, other):
        self.A = self - other
        return self

    def __eq__(self, other):
        range_ = range(len(self.A))
        return all([all([abs(self.A[i][j] - other.A[i][j]) < 
            self.eps for j in range_]) for i in range_])

    def __abs__(self):
        assert(self.is_vector())
        return sqrt(sum([(self.A[i][0] * self.A[i][0].conjugate()).real for i in range(len(self))])
            if self.isCMatrix() else
                sum([self.A[i][0] * self.A[i][0] for i in range(len(self))]))

    def __skal_mul(self, k):
        n, m = len(self), len(self.A[0])
        return Matrix([[k * self.A[j][i] for i in range(m)] for j in range(n)])

    def __len__(self):
        return len(self.A)

    def __roundd(self):
        round_complex = lambda x, ac : complex(round(x.real, ac), round(x.imag, ac))
        round_real = lambda x, ac: round(x, ac)
        return round_complex if self.isCMatrix() else round_real

    def is_square(self): return len(self) == len(self.A[0])

    def is_vector(self): return len(self.A[0]) == 1

    def is_symmetric(self):
        assert(self.is_square())
        return all([all([abs(self.A[i][j] - self.A[j][i]) < 
            self.eps for j in range(i, len(self))]) for i in range(len(self))])

    def copy(self):
        return 1 * self

    def norm_vec(self):
        s = abs(self)
        if s != 0:
            self.A = [[self.A[i][0]/s] for i in range(len(self.A))]
        return self

    def column(self, i, k = 0):
        if self.isCMatrix():
            return Matrix([[self.A[j][i] if j >= k else 0j for j in range(len(self.A))]]) ^ "T"
        return Matrix([[self.A[j][i] if j >= k else 0.0 for j in range(len(self.A))]]) ^ "T"

    def line(self, i):
        return Matrix([self.A[i]])

    def diag_plus(self, k):
        assert(self.is_square())
        for i in range(len(self)):
            self.A[i][i] += k
        return self

    def diag_line(self):
        assert(self.is_square())
        roundd = self.__roundd()
        return Matrix([[roundd(self.A[i][i], 10) for i in range(len(self))]])

    def isCMatrix(self):
        return True if type(self.A[0][0]) is complex else False

    def toCMatrix(self):
        if self.isCMatrix(): return
        for j in range(len(self)):
            for i in range(len(self.A[0])):
                self.A[j][i] = complex(self.A[j][i], 0)

    def Gershgorin_circle(self, i):
        a = sum([abs(self.A[i][j]) for j in range(len(self.A[0]))]) - abs(self.A[i][i])
        # print(f" - {a}")
        return a
        # return sum([abs(self.A[i][j]) for j in range(len(self.A[0]))]) - abs(self.A[i][i])

    def Gershgorin_circle_rev(self, i):
        a = sum([abs(self.A[j][i]) for j in range(len(self.A[0]))]) - abs(self.A[i][i])
        # print(f" + {a}")
        return a
        # return sum([abs(self.A[j][i]) for j in range(len(self.A[0]))]) - abs(self.A[i][i])

    def get_L(self):
        assert(self.is_square())
        n = len(self)
        return Matrix([[self.A[j][i] if i <= j else 0 for i in range(n)] for j in range(n)])

    def to_num(self):
        assert(self.is_vector())
        assert(len(self.A[0]) == 1)
        return self.A[0][0]

    def lower_triangular_solution(self, b):
        assert(self.is_square())
        x = []
        for i in range(len(self)):
            last = b[i][0]/self.A[i][i]
            x.append(last)
            for j in range(i, len(self)):
                b[j][0] -= last * self.A[j][i]
        return Matrix([x]) ^ "T"

    def Givens_mul(self, i, j, c, s):
        u_i_new = [c * self.A[i][k] + s * self.A[j][k] for k in range(len(self.A))]
        u_j_new = [c * self.A[j][k] - s * self.A[i][k] for k in range(len(self.A))]
        self.A[i] = u_i_new
        self.A[j] = u_j_new

    def Householder_mul(self, v):
        _2vT = 2 * v ^ "T"
        self -= v * (_2vT * self)

    def Householder_mul_rev(self, v):
        _2vT = 2 * v ^ "T"
        self -= (self * v) * _2vT

    def Householder_mul_double(self, v):
        self.Householder_mul(v)
        self.Householder_mul_rev(v)

    def simple_iter_eigenvalue(self, v):
        return (self * v).norm_vec()
