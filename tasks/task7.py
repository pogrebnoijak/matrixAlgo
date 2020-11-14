from common import*

def max_eigenvalue(A, v, eps, reasonable_time = 1000):
    for i in range(reasonable_time):
        Av = A * v
        lam = ((v ^ "T") * Av).to_num()
        if (abs(Av - lam * v) < eps):
            return (lam, v)
        v = A.simple_iter_eigenvalue(v)
    return (0, 0)

def simple_iteration_spectrum(A, v, eps):
    A = Matrix(A)
    v = Matrix(v) ^ "T"
    assert (A.is_square())
    assert (v.is_vector())
    assert (eps > 0)
    print("simple iteration spectrum.\nA:")
    A.printC()
    print("v:")
    v.printC()
    print(f"epsilon: \n{eps}")
    lam, v = max_eigenvalue(A, v.norm_vec(), eps)
    if (lam, v) == (0,0):
        print(0)
    else:
        print(f"lam:\n{lam}")
        print("v:")
        v.printC()
    