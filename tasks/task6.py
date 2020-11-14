from common import*

def QR_decomp(A):
    Q = E(len(A))
    for i in range(len(A)):
        v = A.column(i, i).norm_vec()
        v[i][0] -= 1
        A.Householder_mul(v.norm_vec())
        Q.Householder_mul(v)
    return Q ^ "T"

def Householder_QR(A):
    A = Matrix(A)
    assert (A.is_square())
    print("Householder QR.\nA:")
    A.printC()
    R = A.copy()
    Q = QR_decomp(R)
    print("Q:")
    Q.printC()
    print("R:")
    R.printC()
    # (Q * R).printC()
