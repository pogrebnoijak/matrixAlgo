from common import*

def is_diag_zero(A):
    for i in range(len(A)):
        if (A[i][i] == 0):
            return True
    return False

def Gauss_Seidel_method(A, b, eps):
    A = Matrix(A)
    b = Matrix(b) ^ "T"
    assert (A.is_square())
    assert (b.is_vector())
    assert (eps > 0)

    print("Gauss-Seidel method.\nA:")
    A.printC()
    print("b:")
    b.printC()
    print(f"epsilon: \n{eps}")

    if (is_diag_zero(A)):
        print("answer:\n0")
        return

    bad_steps_kol = 0
    x_old = Matrix([[1] * len(A)]) ^ "T"
    L = A.get_L()
    U = A - L
    # L.printC()
    # U.printC()

    print("steps:")

    while (bad_steps_kol != 20):
        x = L.lower_triangular_solution(-U * x_old + b)
        # print(abs(A * x - b))
        print(abs(x) - abs(x_old))
        if (abs(A * x - b) < eps):
            break
        if (abs(x) - abs(x_old) >= 1 or abs(A * x - b) > 1e100):
            bad_steps_kol += 1
        else:
            bad_steps_kol = 0
        x_old = x

    print("answer:")
    if (bad_steps_kol != 20):
        x.printC()
    else:
        print(0)
