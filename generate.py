import random as rand

def generate(n = 10, m = 10, at = 0, to = 25, path = "generate.txt", isZ = False, isC = False, isSymmetric = False, isR_overC = False):
    (atC, toC) = (0, 0) if isC and isR_overC else (at, to)
    rand_num = rand.randint if isZ else rand.uniform
    complex_line = lambda k : [complex(round(rand_num(at, to), 10), round(rand_num(atC, toC), 10)) if k >= j else 0 for j in range(m)]
    real_line = lambda k : [round(rand_num(at, to), 10) if k >= j else 0 for j in range(m)]
    line = complex_line if isC else real_line
    with open("conclusion/" + path, 'w') as f:
        f.write(str(n) + " " + str(m) + (" C" if isC else "") + "\n")
        if isSymmetric:
            assert(n == m)
            matrix = [line(i) for i in range(n)]
            for i in range(n):
                for j in range(i+1, n):
                    matrix[i][j] = matrix[j][i]
        else:
            matrix = [line(m) for i in range(n)]

        for i in range(n):
            f.write(str(matrix[i]) + "\n")
        f.close()