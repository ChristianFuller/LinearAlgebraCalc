import Determinite

def get_2x2_eigenvalues_and_eigenvectors(Matrix, ScaleFactor):

    if(ScaleFactor == 0):

        #& When a and d are the same there is only 1 eigenvalue
        if(Matrix[0][0] == Matrix[1][1]):
            eigenvalue1 = Matrix[0][0]
            solve_eigenVectors_2x2(Matrix, eigenvalue1)
        else:
            eigenvalue1 = Matrix[0][0]
            eigenvalue2 = Matrix[1][1]
            solve_eigenVectors_2x2(Matrix, eigenvalue1)
            solve_eigenVectors_2x2(Matrix, eigenvalue2)

    
def solve_eigenVectors_2x2(Matrix, eigenvalue):
    Final_Vector = []

    #& A - lambda * I
    Eigen_Matrix = [[Matrix[0][0] - eigenvalue, Matrix[0][1]], [Matrix[1][0], Matrix[1][1] - eigenvalue]]

    # | a b | | e |
    # | c d | | f |

    #& If a is the only value in a*e and b*f and a is not 0
    if(Eigen_Matrix[0][1] == 0 and Eigen_Matrix[0][0] != 0):
        x = 0
    #&





