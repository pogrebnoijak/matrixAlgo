from common import*

def inequality_of_Gershgorin_circles(A):
    for i in range(len(A)):
        if (abs(A[i][i]) + A.Gershgorin_circle(i) > 1):
            return False
    return True

def simple_iteration_method(A, b, eps):
    A = Matrix(A)
    b = Matrix(b) ^ "T"
    assert (A.is_square())
    assert (b.is_vector())
    assert (eps > 0)

    print("Simple iteration method.\nA:")
    A.printC()
    print("b:")
    b.printC()
    print(f"epsilon: \n{eps}")

    bad_steps_kol = 0
    x_old = Matrix([[1] * len(A)]) ^ "T"
    A = - A.diag_plus(-1)

    print("steps:")

    while (bad_steps_kol != 20):
        x = A * x_old + b
        Ax = A * x
        print(abs(x - Ax - b))
        if (abs(x - Ax - b) < eps):
            break
        if (not inequality_of_Gershgorin_circles(A) and abs(x) - abs(x_old) >= 1):
            bad_steps_kol += 1
        else:
            bad_steps_kol = 0
        x_old = x

    print("answer:")
    if (bad_steps_kol != 20):
        x.printC()
    else:
        print(0)
