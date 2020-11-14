from common import*
from tasks import*

def for_task10_11(file = "generate.txt"):
    generate(5, 5, -5, 5, file, isZ = True, isSymmetric = True)
    A_for_10 = Matrix(file)
    task9.tri_diagonalization(A_for_10)
    A_for_10.printM(file)

vect = lambda n: [[i for i in range(1,n+1)]]
epsilon = 0.001

def all_tasks():
    # task1.simple_iteration_method("for_task1_2.txt", vect(3), epsilon)
    # task1.simple_iteration_method("for_task1_2_big.txt", vect(5), epsilon)
    # task2.Gauss_Seidel_method("for_task1_2.txt", vect(3), epsilon)
    # task2.Gauss_Seidel_method("for_task1_2_big.txt", vect(5), epsilon)
    # task3.Givens_rotations("for_task3_4.txt", 1, 4, 0.6, 0.8)
    # task4.Givens_QR("for_task3_4.txt")
    # task5.Householder_reflections("for_task5_6.txt", vect(5))
    # task6.Householder_QR("for_task5_6.txt")
    # task7.simple_iteration_spectrum("for_task7.txt", vect(5), epsilon)
    # task8.QR_spectrum("for_task8.txt", epsilon)
    # task9.tridiagonal_matrices("for_task9.txt")
    # # for_task10_11("for_task10.txt")
    # task10.tridiagonal_QR("for_task10.txt", epsilon)
    # # for_task10_11("for_task11.txt")
    # task11.tridiagonal_QR_shift("for_task11.txt", epsilon)
    # task12.non_isomorphism_test("graphA1.txt", "graphB1.txt")
    # task12.non_isomorphism_test("graphA2.txt", "graphB2.txt")
    # task13.expander1(4)
    # task13.expander1(10) # long
    # task13.expander2(5)   # ?
    # task13.expander2(31)  # ?
    return

def main():
    all_tasks()
    return

if __name__ == "__main__":
    main()
