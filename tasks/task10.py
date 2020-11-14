from common import*
from tasks import task4, task8
from math import copysign

def QR_decomp(A, rang = -1):
    if rang == -1: rang += len(A)
    Q = E(len(A))
    for i in range(rang):
        j = i + 1
        (c, s) = task4.pred_Givens(A, i, i, j)
        A.Givens_mul(j, i, s, c)
        Q.Givens_mul(j, i, s, c)
    return Q ^ "T"

def all_spectrum(R, eps):
    Q_k = E(len(R))
    while (not task8.Gershgorin_check(R, eps)):
        Q = QR_decomp(R)
        Q_k *= Q
        R *= Q
        # R.printC()
    # (Q_k * R * (Q_k ^ "T")).printC()
    return (Q_k, R.diag_line())

def tridiagonal_QR(A, eps):
    A = Matrix(A)
    assert (A.is_square())
    assert (eps > 0)
    # A.toCMatrix()
    print("tridiagonal QR spectrum.\nA:")
    A.printC()
    print(f"epsilon: \n{eps}")
    (Q, diag) = all_spectrum(A, eps)
    print("spectrum:")
    diag.printC()
    print("Q_k:")
    Q.printC()
