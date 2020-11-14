from common import*
from tasks import task10, task9, task6

def non_isomorphism_test(A, B):
    A = Matrix(A)
    B = Matrix(B)
    assert (A.is_square())
    assert (B.is_square())
    print("non-isomorphism test.\nA:")
    A.printC()
    print("B:")
    B.printC()
    if len(A) != len(B):
        print(0)
        return
    x = Matrix([[1]] * len(A))
    dA = ((A * x) ^ "T")[0]
    dB = ((B * x) ^ "T")[0]
    dA.sort(); dB.sort()
    if dA != dB:
        print(0)
        return
    degeneracyA = 0 in task6.QR_decomp(A.copy()).diag_line()[0]
    degeneracyB = 0 in task6.QR_decomp(B.copy()).diag_line()[0]
    if degeneracyA != degeneracyB:
        print(0)
        return
    
    if degeneracyA == False:
        task9.tri_diagonalization(A)
        task9.tri_diagonalization(B)
        A.printM("some.txt")
        A = Matrix("some.txt")
        (_, spA) = task10.all_spectrum(A, 0.001)
        B.printM("some.txt")
        B = Matrix("some.txt")
        (_, spB) = task10.all_spectrum(B, 0.001)
        if spA != spB:
            print(0)
            return
    print(1)
