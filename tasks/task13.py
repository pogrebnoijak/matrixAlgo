from common import*
from tasks import task9, task10, task11

eps = 5e-5

def regularing(A):
    x = Matrix([[1]] * len(A))
    vec = ((A * x) ^ "T")[0]
    d = vec[0]
    assert (all([vec[i] == d for i in range(len(A))]) and "G is not regular!")
    return d

def expander_any(file):
    A = Matrix(file)
    d = regularing(A)
    A.printC()

    task9.tri_diagonalization(A)
    A.printM(file)
    A = Matrix(file)
    (_, diag) = task11.all_spectrum(A, eps)
    diagonal = diag[0]
    diagonal.sort(reverse = True)
    # print(diagonal)
    print(max(abs(diagonal[1]), abs(diagonal[len(A)-1]))/d)


def expander1(n):
    A = [[0] * n * n for i in range(n * n)]
    edge_to = lambda x, y: [((x+2*y)%n, y), ((x-2*y)%n, y), ((x+2*y+1)%n, y), ((x-2*y-1)%n, y),
                            (x, (y+2*x)%n), (x, (y-2*x)%n), (x, (y+2*x+1)%n), (x, (y-2*x-1)%n)]
    for x in range(n):
        for y in range(n):
            for (a,b) in edge_to(x,y):
                A[x*n+y][a*n+b] += 1
    Matrix(A).printM("task13.txt")
    expander_any("task13.txt")

def expander2(p):
    back = []
    back.append(p), back.append(1)
    for i in range(2, p):
	    back.append(-(p//i) * back[p%i] % p)
    back.append(0)
    # for i in range(p+1): print(back[i] * i % p)

    A = [[0] * (p+1) for i in range(p+1)]
    edge_to = lambda x: [(x+1)%p, (x-1)%p, back[x]]
    for x in range(p+1):
        for y in edge_to(x):
            A[x][y] += 1
    Matrix(A).printM("task13.txt")
    expander_any("task13.txt")