from common import*
from tasks import task6

def Gershgorin_check(A, eps):
    return all([A.Gershgorin_circle(i) < eps for i in range(len(A))])

def all_spectrum(R, eps):
    Q_k = E(len(R))
    while (not Gershgorin_check(R, eps)):
        Q = task6.QR_decomp(R)
        Q_k *= Q
        R = R * Q
    # (Q_k * R * (Q_k ^ "T")).printC()
    return (Q_k, R.diag_line())

def QR_spectrum(A, eps):
    A = Matrix(A)
    assert (A.is_symmetric())
    assert (eps > 0)
    print("QR spectrum.\nA:")
    A.printC()
    print(f"epsilon: \n{eps}")
    (Q, diag) = all_spectrum(A, eps)
    print("spectrum:")
    diag.printC()
    print("Q_k:")
    Q.printC()
