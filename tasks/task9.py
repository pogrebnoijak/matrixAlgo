from common import*

def tri_diagonalization(A):
    Q = E(len(A))
    for i in range(len(A) - 1):
        v = A.column(i, i + 1).norm_vec()
        v[i + 1][0] -= 1
        A.Householder_mul_double(v.norm_vec())
        Q.Householder_mul(v)
    return Q

def tridiagonal_matrices(A):
    A = Matrix(A)
    assert (A.is_symmetric())
    print("tridiagonal matrices.\nA:")
    A.printC()
    T = A.copy()
    Q = tri_diagonalization(T)
    print("Q:")
    Q.printC()
    print("tridiagonal:")
    T.printC()
    # ((Q ^ "T") * T * Q).printC()
