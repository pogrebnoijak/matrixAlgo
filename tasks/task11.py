from common import*
from tasks import task10

def all_spectrum(R, eps, kol_iter = 5):
    Q_k = E(len(R))
    condition = lambda j : R.Gershgorin_circle(j) < eps and R.Gershgorin_circle_rev(j) < eps
    for j in range(len(R) - 1, 0, -1):
        print(j)
        for i in range(kol_iter):
            if condition(j): break
            Q = task10.QR_decomp(R, j)
            Q_k *= Q; R *= Q
        if condition(j): continue
        s = R[j][j]
        R.diag_plus(-s)
        while (not condition(j)):
            Q = task10.QR_decomp(R, j)
            Q_k *= Q; R *= Q
            # R.printC()
        R.diag_plus(s)
    # (Q_k * R * (Q_k ^ "T")).printC()
    # R.printC()
    return (Q_k, R.diag_line())

def tridiagonal_QR_shift(A, eps):
    A = Matrix(A)
    assert (A.is_square())
    assert (eps > 0)
    # A.toCMatrix()
    print("tridiagonal QR shift spectrum.\nA:")
    A.printC()
    print(f"epsilon: \n{eps}")
    (Q, diag) = all_spectrum(A, eps)
    print("spectrum:")
    diag.printC()
    print("Q_k:")
    Q.printC()
