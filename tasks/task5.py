from common import*

def Householder_reflections(A, v):
    A = Matrix(A)
    v = Matrix(v) ^ "T"
    assert (A.is_square())
    assert (v.is_vector())
    v.norm_vec()
    assert ((abs(v) - 1) < v.eps)
    print("Householder reflections.\nA:")
    A.printC()
    print("v:")
    v.printC()
    A.Householder_mul(v)
    A.printC()