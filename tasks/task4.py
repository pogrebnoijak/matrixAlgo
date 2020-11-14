from common import*
from math import copysign

def pred_Givens(A, st, i, j):
    if A.isCMatrix():
        kv = sqrt((A[j][st] * A[j][st].conjugate() + A[i][st] * A[i][st].conjugate()).real)
    else:
        kv = sqrt(A[j][st] * A[j][st] + A[i][st] * A[i][st])
    if (kv == 0): return (1, 0)
    c = A[j][st]/kv; s = -A[i][st]/kv
    return (c, s)

def QR_decomp(A):
    Q = E(len(A))
    for i in range(len(A) - 1):
        j = len(A) - 1
        while (j >= i):
            if (A[j][i] != 0): break
            j-=1
        jj = j; j-=1
        while (j >= i):
            (c, s) = pred_Givens(A, i, j, jj)
            A.Givens_mul(j, jj, c, s)
            Q.Givens_mul(j, jj, c, s)
            j-=1
        Q.Givens_mul(i, jj, 0, copysign(1, A[jj][i]))
        A.Givens_mul(i, jj, 0, copysign(1, A[jj][i]))
    return Q ^ "T"

def Givens_QR(A):
    A = Matrix(A)
    assert (A.is_square())
    print("Givens QR.\nA:")
    A.printC()
    R = A.copy()
    Q = QR_decomp(R)
    print("Q:")
    Q.printC()
    print("R:")
    R.printC()
    # (Q * R).printC()
