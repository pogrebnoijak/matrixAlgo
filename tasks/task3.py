from common import*

def Givens_rotations(A, i, j, c, s):
    A = Matrix(A)
    assert (A.is_square())
    assert (0 <= i <= len(A))
    assert (0 <= j <= len(A))
    assert ((c * c + s * s - 1) <= 0.001)
    print("Givens rotations.\nA:")
    A.printC()
    print(f"i = {i}, j = {j}, c = {c}, s = {s}")
    A.Givens_mul(i, j, c, s)
    A.printC()
