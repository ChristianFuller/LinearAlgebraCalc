import Determinite, Inverse
import magnitude, angle, dot_product, projection, v_s, threeD_shortcut
import rotation, scale_matrix, skew, orthographic_projection, mutiply_matrix
import eigenthings

from plot_vectors import plot_matrix
from Vector_to_ArrayMatrix import make_vector_into_ArrayMatrix, make_vector_into_ArrayMatrix_Square
from math import cos, sin, radians


class Determinites():
    def run():
        choice = input("Choose Detrminite size\n1 for 2x2\n2 for 3x3\n3 for 4x4\n4 for finding inverse\n5. Go back\n")

        if choice == "1":
            a = int(input("Enter the value of a: "))
            b = int(input("Enter the value of b: "))
            c = int(input("Enter the value of c: "))
            d = int(input("Enter the value of d: "))
            Determinite.two_by_two_determinant(a, b, c, d)
        elif choice == "2":
            a = int(input("Enter the value of a: "))
            b = int(input("Enter the value of b: "))
            c = int(input("Enter the value of c: "))
            d = int(input("Enter the value of d: "))
            e = int(input("Enter the value of e: "))
            f = int(input("Enter the value of f: "))
            g = int(input("Enter the value of g: "))
            h = int(input("Enter the value of h: "))
            i = int(input("Enter the value of i: "))
            answer1 = int(input("What is the answer to the first equation: "))
            answer2 = int(input("What is the answer to the second equation: "))
            answer3 = int(input("What is the answer to the third equation: "))
            Determinite.three_by_three_determinant(a, b, c, d, e, f, g, h, i, answer1, answer2, answer3)
        elif choice == "3":
            a = int(input("Enter the value of a: "))
            b = int(input("Enter the value of b: "))
            c = int(input("Enter the value of c: "))
            d = int(input("Enter the value of d: "))
            e = int(input("Enter the value of e: "))
            f = int(input("Enter the value of f: "))
            g = int(input("Enter the value of g: "))
            h = int(input("Enter the value of h: "))
            i = int(input("Enter the value of i: "))
            j = int(input("Enter the value of j: "))
            k = int(input("Enter the value of k: "))
            l = int(input("Enter the value of l: "))
            m = int(input("Enter the value of m: "))
            n = int(input("Enter the value of n: "))
            o = int(input("Enter the value of o: "))
            p = int(input("Enter the value of p: "))
            answer1 = int(input("What is the answer to the first equation: "))
            answer2 = int(input("What is the answer to the second equation: "))
            answer3 = int(input("What is the answer to the third equation: "))
            answer4 = int(input("What is the answer to the fourth equation: "))
            Determinite.four_by_four_determinant(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,answer1,answer2,answer3,answer4)
        elif choice == "4":
            inverse_choice = input("Choose the size of the matrix you want to find the inverse of\n1 for 2x2:\n2 for 3x3: ")
            if inverse_choice == "1":
                Inverse.inverse(inverse_choice)
            elif inverse_choice == "2":
                Inverse.inverse(inverse_choice)
            else:
                print("Inverse for that size is not yet implemented.")
        else:
            return





class Projection():
    def run():
        choice = int(input("1. Get Projection\n2. Get Magnitude\n3. Get Dot Product\n4. Get Angle\n5. Get V's\n6. Get Orthogonal Vector\n7. Go Back\n"))
        if(choice == 1):
            Elements = int(input("How many elements are in each vector?\n"))

            currentElement = 0
            VectorA = []
            VectorB = []
            while(currentElement < Elements):
                VectorA.append(int(input(f"\nElement {currentElement} for Vector A:")))
                currentElement += 1
            currentElement = 0

            while(currentElement < Elements):
                VectorB.append(int(input(f"\nElement {currentElement} for Vector B:")))
                currentElement += 1

            projection.get_projection(VectorA, VectorB)
        elif(choice == 2):
            MatrixSize = float(input("How many elements are in the vector?\n"))
            elements = 0
            Vector = []
            while(elements < MatrixSize):
                Vector.append(float(input(f"\nElement {elements} for Vector:")))
                elements += 1
            magnitude.get_magnitude(Vector)
        elif(choice == 3):
            TotalElements = float(input("How many elements are in each vector?\n"))
            elements = 0
            VectorA = []
            VectorB = []
            while(elements < TotalElements):
                VectorA.append(float(input(f"\nElement {elements} for Vector A:")))
                elements += 1
            elements = 0
            while(elements < TotalElements):
                VectorB.append(float(input(f"\nElement {elements} for Vector B:")))
                elements += 1
            dot_product.solve_dot_product_2_vectors(VectorA, VectorB)
        elif(choice == 4):
            Elements = int(input("How many elements are in each vector?\n"))

            currentElement = 0
            VectorA = []
            VectorB = []
            while(currentElement < Elements):
                VectorA.append(float(input(f"\nElement {currentElement} for Vector A:")))
                currentElement += 1
            currentElement = 0

            while(currentElement < Elements):
                VectorB.append(float(input(f"\nElement {currentElement} for Vector B:")))
                currentElement += 1

            Magnitudes = []
            VaMag = magnitude.get_magnitude(VectorA)
            VbMag = magnitude.get_magnitude(VectorB)
            Magnitudes.append(VaMag)
            Magnitudes.append(VbMag)

            angle.solve_Angle(dot_product.solve_dot_product_2_vectors(VectorA, VectorB), Magnitudes)
        elif(choice == 5):
            TotalElements = int(input("How many elements are in each vector?\n"))
            elements = 0
            VectorA = []
            VectorB = []
            while(elements < TotalElements):
                VectorA.append(int(input(f"\nElement {elements} for Vector A:")))
                elements += 1
            elements = 0
            while(elements < TotalElements):
                VectorB.append(int(input(f"\nElement {elements} for Vector B:")))
                elements += 1
            Vector1, Vector2 = v_s.find_vs(VectorA, VectorB)
            v_s.check_answers(VectorA, VectorB, Vector1, Vector2)
        elif(choice == 6):
            VectorA = []
            VectorB = []
            while(len(VectorA) < 3):
                VectorA.append(int(input(f"Enter element {len(VectorA)} for Vector A: ")))
            while(len(VectorB) < 3):
                VectorB.append(int(input(f"Enter element {len(VectorB)} for Vector B: ")))
            OrthogonalVector = threeD_shortcut.get_orthogonal(VectorA, VectorB)
            threeD_shortcut.check_answer(VectorA, VectorB, OrthogonalVector)
        else:
            return
        







class Transformation():
    def run():

        choice = int(input("What do you want to do?\n1. Scale\n2. Skew/Shear\n3. Rotate\n4. Orthographic Projection\n5. Multiply Matrixes\n6. Do Matrix concatenation\n"))

        match choice:
            #!Case 1
            case 1:
                #&Get variables
                currentElement = 1
                Vector = []

                #& Matrix size then make matrix
                MatrixSize = int(input("\nWhat size Matrix do you want to scale: "))
                for VectorLength in range(MatrixSize*MatrixSize):
                    #&If choice is a multiple of 3
                    Vector.append(int(input(f"\nElement {currentElement} for Matrix: ")))

                #& Scale number and scale
                ScaleNumber = int(input("\nWhat do you want to scale the matrix by: "))
                ScaledVector = scale_matrix.scale(Vector, ScaleNumber, MatrixSize)

                #&Plot the matrix
                plot_matrix(make_vector_into_ArrayMatrix_Square(Vector, MatrixSize), make_vector_into_ArrayMatrix_Square(ScaledVector, MatrixSize))

            #!Case 2
            case 2:

                choice = int(input("Do you want to\n1. Construct a matrix\n2. Skew/Shear a matrix\n"))

                #& Construct a matrix
                if(choice == 1):
                    #&Get variables
                    SkewNumber1 = int(input("\nWhat do you want to first Skew/Shear the matrix by (k1): "))
                    SkewNumber2 = int(input("\nWhat do you want to first Skew/Shear the matrix by (k1): "))
                    MatrixSize = int(input("What size matrix do you want to construct\n1. 3x3\n2. 4x4\n"))

                    #& Construct matrix
                    if(MatrixSize == 1):
                        print(skew.consturct_3d_matrix(SkewNumber1, SkewNumber2))
                    else:
                        print(skew.consturct_4d_matrix(SkewNumber1, SkewNumber2))
                else:

                    currentElement = 1
                    Vector = []

                    #& Get Matrix size and elements
                    MatrixSize = int(input("\nWhat size matrix do you want to Skew/Shear: "))
                    for VectorLength in range(MatrixSize*MatrixSize):
                        Vector.append(int(input(f"\nElement {currentElement} for Matrix: ")))
                        currentElement += 1

                    #& Get Skew/Shear number
                    if(MatrixSize < 3):
                        SkewNumber = int(input("\nWhat do you want to Skew/Shear the matrix by (k): "))
                    elif(MatrixSize > 2):
                        SkewNumber1 = int(input("\nWhat do you want to first Skew/Shear the matrix by (k1): "))
                        SkewNumber2 = int(input("\nWhat do you want to second Skew/Shear the matrix by (k2): "))

                    #& make sure its either h or v
                    skewdir = ''
                    while skewdir not in ('h','v'):
                        skewdir = input("\nDo you want to skew/shear (h/v): ")


                    #&Make the vector into a matrix ([[1,2,3], [4,5,6]])
                    ArrayMatrix = make_vector_into_ArrayMatrix_Square(Vector, MatrixSize)

                    #& Only Skew/Shear if the size is 2,3 or 4
                    if(MatrixSize == 2):

                        #& Get Skew/Shear matrix, Plot it
                        if(skewdir == "h"):
                            SkewedMatrix = skew.twod_skew_horizonal(ArrayMatrix, SkewNumber)
                        else:
                            SkewedMatrix = skew.twod_skew_vertical(ArrayMatrix, SkewNumber)

                        plot_matrix(SkewedMatrix, ArrayMatrix)
                        return
                    
                    elif(MatrixSize == 3):

                        #&Get the 3x3 Skew/Shear formula
                        SkewMatrix = skew.consturct_3d_matrix(SkewNumber1, SkewNumber2)

                        #& Make the vector into a matrix
                        #& Nultiply the formula by the matrix to get the Skew/Sheared matrix
                        SkewedMatrixArray = mutiply_matrix.multiply_two_matrix(ArrayMatrix, SkewMatrix)
                        
                        plot_matrix(ArrayMatrix, SkewedMatrixArray)

                    elif(MatrixSize == 4):

                        #&Get the 4x4 matrix formula and return since you cant plot a 4d array
                        SkewedMatrix = skew.consturct_4d_matrix(SkewNumber1, SkewNumber2)
                        return mutiply_matrix.multiply_two_matrix(ArrayMatrix, SkewedMatrix)
                    
                    else:
                        print("Please choose 2,3 or 4")
                        return

            #!Case 3
            case 3:
                choice = int(input("Do you want to\n1. Construct a matrix\n2. Rotate a matrix\n"))

                #& Construct a matrix
                if(choice == 1):
                    #&Get variables
                    RotateNumber = int(input("\nWhat do you want to rotate the matrix by: "))
                    MatrixSize = int(input("What size matrix do you want to construct\n1. 3x3\n2. 4x4\n"))

                    #& Construct matrix
                    if(MatrixSize == 1):
                        print(clean_rotation_matrix(rotation.construct_3x3_matrix(RotateNumber)))
                    else:
                        print(clean_rotation_matrix(rotation.construct_4x4_matrix(RotateNumber)))
                else:
                    currentElement = 1
                    Vector = []

                    #& Get Matrix size and elements
                    MatrixSize = int(input("\nWhat size matrix do you want to rotate: "))
                    for VectorLength in range(MatrixSize*MatrixSize):
                        Vector.append(int(input(f"\nElement {currentElement} for Matrix: ")))
                        currentElement += 1

                    #& Get rotation number
                    RotateNumber = int(input("\nWhat do you want to rotate the matrix by: "))

                    #& Only rotate if the size is 2,3 or 4
                    if(MatrixSize == 2):
                        #& Get rotated matrix, Make the vector into a matrix ([[1,2,3], [4,5,6]]), Plot it
                        ArrayMatrix = make_vector_into_ArrayMatrix_Square(Vector, MatrixSize)
                        RotatedMatrix = rotation.twod_rotate(ArrayMatrix, RotateNumber)
                        plot_matrix(RotatedMatrix, ArrayMatrix)
                        return
                    elif(MatrixSize == 3):
                        #&Get the 3x3 rotation formula
                        RotationMatrix = rotation.construct_3x3_matrix(RotateNumber)
                        #& Make the vector into a matrix
                        ArrayMatrixVector = make_vector_into_ArrayMatrix_Square(Vector, MatrixSize)
                        #& Nultiply the formula by the matrix to get the rotated matrix
                        RotatedMatrixArray = mutiply_matrix.multiply_two_matrix(ArrayMatrixVector, RotationMatrix)
                        
                        plot_matrix(ArrayMatrixVector, RotatedMatrixArray)
                    elif(MatrixSize == 4):
                        #&Get the 4x4 matrix formula and return since you cant plot a 4d array
                        RotationMatrix = rotation.construct_4x4_matrix(RotateNumber)
                        return mutiply_matrix.multiply_two_matrix(Vector, RotationMatrix)
                    else:
                        print("Please choose 2,3 or 4")
                        return
                    
            #!Case 4
            case 4:
                choice = int(input("Do you want to\n1. Construct a Projection/Reflection\n2. Orthographicly Project/Reflect\n"))

                #& Construct a Projection/Reflection
                if(choice == 1):
                    
                    #&Get variables
                    MatrixSize = int(input("What size matrix do you want to construct\n1. 2x2\n2. 3x3\n"))
                    projection_or_reflection = ''
                    while projection_or_reflection.lower() not in ('p','r'):
                        projection_or_reflection = input("\nProjection or Reflection? (p/r): ")

                    #& 2x2
                    if(MatrixSize == 1):
                        #& Get x and y
                        xvalue = float(input("What is the x value: "))
                        yvalue = float(input("What is the y value: "))

                        #&Project or reflect
                        if(projection_or_reflection == "p"):
                            #&Project
                            print(orthographic_projection.construct_2x2_projection(xvalue, yvalue))
                        else:
                            #&Reflect
                            print(orthographic_projection.construct_2x2_reflection(xvalue, yvalue))

                    #& 3x3
                    else:
                        #& get x, y, z
                        xvalue = float(input("What is the x value: "))
                        yvalue = float(input("What is the y value: "))
                        zvalue = float(input("What is the z value: "))

                        #&Project or reflect
                        if(projection_or_reflection == "p"):
                            print(orthographic_projection.construct_3x3_projection(xvalue,yvalue,zvalue))
                        else:
                            print(orthographic_projection.construct_3x3_reflection(xvalue,yvalue,zvalue))

                #& Orthographicly Project/Reflect
                elif(choice == 2):
                    currentElement = 1
                    Vector = []

                    #& Get Matrix size and elements
                    MatrixSize = int(input("\nWhat size matrix do you want to project (2 or 3): "))
                    for VectorLength in range(MatrixSize*MatrixSize):
                        Vector.append(int(input(f"\nElement {currentElement} for Matrix: ")))
                        currentElement += 1

                    #&Make vector into [[1,2,3], [4,5,6]]
                    ArrayVector = make_vector_into_ArrayMatrix_Square(Vector, MatrixSize)

                    #& Get projection or reflection
                    projection_or_reflection = ''
                    while projection_or_reflection.lower() not in ('p','r'):
                        projection_or_reflection = input("\nProjection or Reflection? (p/r): ")

                    #& 2x2
                    if MatrixSize == 2:

                        #& Get horizonal or vertical
                        horizontal_or_vertical = ''
                        while horizontal_or_vertical.lower() not in ('h','v'):
                            horizontal_or_vertical = input("\nHorizontal or Vertical? (h/v): ")


                        #&Project horizontal or vertical
                        if(projection_or_reflection == "P"):
                            if(horizontal_or_vertical == "h"):
                                print(orthographic_projection.twod_project_horizonal(ArrayVector))
                            else:
                                print(orthographic_projection.twod_project_vertical(ArrayVector))
                        #&Reflect horizinal or vertical
                        else:
                            if(horizontal_or_vertical == "h"):
                                print(orthographic_projection.twod_project_horizonal_reflection(ArrayVector))
                            else:
                                print(orthographic_projection.twod_project_vertical_reflection(ArrayVector))
                    #& 3x3
                    elif MatrixSize == 3:
                        if(projection_or_reflection == "p"):
                            ortho_proj_formula = orthographic_projection.threed_projection_formula()
                            print(mutiply_matrix.multiply_two_matrix(ArrayVector, ortho_proj_formula))
                        else:
                            print("No 3d reflection formula")
            #!Case 5
            case 5:
                Vector1 = []
                Vector2 = []

                #& Matrix 1 dimensions
                rows1 = int(input("\nMatrix 1 rows: "))
                cols1 = int(input("Matrix 1 columns: "))

                #& Matrix 2 dimensions
                rows2 = int(input("\nMatrix 2 rows: "))
                cols2 = int(input("Matrix 2 columns: "))

                #& Check multiplication rule
                if cols1 != rows2:
                    print("\nCannot multiply these matrices.")
                    print("Matrix 1 columns must equal Matrix 2 rows.")
                    exit()

                #& Input Matrix 1 elements
                print("\nEnter Matrix 1 elements:")
                for i in range(rows1 * cols1):
                    element = (input(f"Element {i+1}: "))
                    if (element == "cos"):
                        Degree = int(input("What is the degree: "))
                        number = cos(radians(Degree))
                    elif(element == "sin"):
                        Degree = int(input("What is the degree: "))
                        number = sin(radians(Degree))
                    elif(element == "-sin"):
                        Degree = int(input("What is the degree: "))
                        number = -sin(radians(Degree))
                    else:
                        number = float(element)
                    Vector1.append(number)

                #& Input Matrix 2 elements
                print("\nEnter Matrix 2 elements:")
                for i in range(rows2 * cols2):
                    element = (input(f"Element {i+1}: "))
                    if (element == "cos"):
                        Degree = int(input("What is the degree: ")) 
                        number = cos(radians(Degree))
                    elif(element == "sin"):
                        Degree = int(input("What is the degree: "))
                        number = sin(radians(Degree))
                    elif(element == "-sin"):
                        Degree = int(input("What is the degree: "))
                        number = -sin(radians(Degree))
                    else:
                        number = float(element)
                    Vector2.append(number)

                #& Make the vectors into [[1,2,3], [4,5,6]]
                ArrayMatrix1 = make_vector_into_ArrayMatrix(Vector1, rows1, cols1)
                ArrayMatrix2 = make_vector_into_ArrayMatrix(Vector2, rows2, cols2)

                print(mutiply_matrix.multiply_two_matrix(ArrayMatrix1, ArrayMatrix2))

            #! Case 6
            case 6:

                #&Getting MartixSize and how many functions into 1
                MatrixSize = int(input("Whats the size of the Matrix?\n1. 2x2\n2. 3x3\n"))
                HowMany = int(input("How many multipliers?\n1. 2 ( R(S) )\n2. 3 ( (R(S(K))) )\n"))


                if HowMany == 1:
                    #& Get the 2 formulas
                    Factor1 = int(input("Whats first?\n1. Rotate\n2. Skew\n3. Project\n4. Reflect\n5. Scale\n"))
                    Factor2 = int(input("Whats second?\n1. Rotate\n2. Skew\n3. Project\n4. Reflect\n5. Scale\n"))

                    Formula1 = get_formula(Factor2, MatrixSize)
                    Formula2 = get_formula(Factor1, MatrixSize)


                    Vector1 = []

                    #& Matrix 1 dimensions
                    rows1 = int(input("\nMatrix rows: "))
                    cols1 = int(input("Matrix columns: "))

                    #& Input Matrix 1 elements
                    print("\nEnter Matrix 1 elements:")
                    for i in range(rows1 * cols1):
                        Vector1.append(int(input(f"Element {i+1}: ")))


                    #& make the vector into [[1,2,3], [4,5,6]]
                    ArrayMatrix = make_vector_into_ArrayMatrix(Vector1, rows1, cols1)

                    #& Combine the 2 functions together
                    Updated_Formula = mutiply_matrix.multiply_two_matrix(Formula1, Formula2)
                    print(f"\nMultiplied Formula ({Formula1} * {Formula2}): ", Updated_Formula)

                    #& Multiply the combined functions with the Orginal Vector
                    Final_Answer = mutiply_matrix.multiply_two_matrix(Updated_Formula, ArrayMatrix)


                    plot_matrix(ArrayMatrix, Updated_Formula)
                    print(Final_Answer)
                else:

                    #&Get the formulas
                    Factor1 = int(input("Whats first?\n1. Rotate\n2. Skew\n3. Project\n4. Reflect\n5. Scale\n"))
                    Factor2 = int(input("Whats second?\n1. Rotate\n2. Skew\n3. Project\n4. Reflect\n5. Scale\n"))
                    Factor3 = int(input("Whats second?\n1. Rotate\n2. Skew\n3. Project\n4. Reflect\n5. Scale\n"))

                    Formula1 = get_formula(Factor3, MatrixSize)
                    Formula2 = get_formula(Factor2, MatrixSize)
                    Formula3 = get_formula(Factor1, MatrixSize)


                    Vector1 = []

                    #& Matrix 1 dimensions
                    rows1 = int(input("\nMatrix rows: "))
                    cols1 = int(input("Matrix columns: "))

                    #& Input Matrix 1 elements
                    print("\nEnter Matrix 1 elements:")
                    for i in range(rows1 * cols1):
                        Vector1.append(int(input(f"Element {i+1}: ")))


                    #& Make the vector into [[1,2,3], [4,5,6]]
                    ArrayMatrix = make_vector_into_ArrayMatrix(Vector1, rows1, cols1)

                    #& Multiply the funcitions together
                    Updated_Formula = mutiply_matrix.multiply_two_matrix(Formula1, Formula2)
                    Updated_Formula2 = mutiply_matrix.multiply_two_matrix(Updated_Formula, Formula3)

                    print(f"\nMultiplied Formula Part 1 ({Formula1} * {Formula2}): ", Updated_Formula)
                    print(f"\nMultiplied Formula Part 2 ({Updated_Formula} * {Formula2}): ", Updated_Formula2)

                    #&Multiply final funtion with org vector
                    Final_Answer = mutiply_matrix.multiply_two_matrix(Updated_Formula2, ArrayMatrix)
                    plot_matrix(ArrayMatrix, Updated_Formula2)
                    print(Final_Answer)
                



def get_formula(Choice, Size):
    #& Rotate
    if(Choice == 1):
        #&Get rotation angle
        Rotateangle = int(input("\nWhat is the rotate angle?: "))

        #&Return based on what the size was
        if(Size == 1):
            return rotation.get_2d_rotate(Rotateangle)
        else:
            return rotation.construct_3x3_matrix(Rotateangle)
        
    #& Skew/Shear
    elif(Choice == 2):

        #&Get horizontal or vertica;
        skewdir = ''
        while skewdir not in ('h','v'):
            skewdir = input("\nDo you want to skew/shear (h/v): ")

        #& Do 2d or 3d based on what the size was
        if(Size == 1):

            #&Get k and do stuff based on if its horizonal or vertical
            SkewNumber = int(input("\nWhat do you want to Skew/Shear the matrix by (k): "))
            if(skewdir == "h"):
                return skew.get_2d_skew_horizontal(SkewNumber)
            else:
                return skew.get_2d_skew_vertical(SkewNumber)
        #& 3x3 matrix
        else:
            SkewNumber1 = int(input("\nWhat do you want to first Skew/Shear the matrix by (k1): "))
            SkewNumber2 = int(input("\nWhat do you want to second Skew/Shear the matrix by (k2): "))
            return skew.consturct_3d_matrix(SkewNumber1, SkewNumber2)
        
    #&Project
    elif(Choice == 3):
        #& based on what the size of the matrix was
        if(Size == 1):
            
            #& Get project horizontal or vertical
            proj = ''
            while proj not in ('h','v'):
                proj = input("\nDo you want to project (h/v): ")
            
            #&Project based on h or v
            if(proj == "h"):
                return orthographic_projection.get_2x2_Projection_horizontal()
            else:
                return orthographic_projection.get_2x2_Projection_vertical()
        #& Size is 3x3
        else:
            return orthographic_projection.threed_projection_formula()
        
    #&Reflect
    elif(Choice == 4):
        #& based on what the size of the matrix was
        if(Size == 1):

            #& See if it needs to reflect horizontal or vertical
            reflect = ''
            while reflect not in ('h','v'):
                reflect = input("\nDo you want to skew/shear (h/v): ")

            #& Reflect based on if its h or v
            if(reflect == "h"):
                return orthographic_projection.get_2x2_Reflection_horizontal()
            else:
                return orthographic_projection.get_2x2_Reflection_vertical()
        #& 3x3
        else:
            return orthographic_projection.threex3_reflection_formula()
    #& Scale
    elif(Choice == 5):

        ScaleFactor = int(input("\nWhat is the scale factor?: "))

        if(Size == 1):
            return scale_matrix.get_2d_Scale(ScaleFactor)
        if(Size == 2):
            return scale_matrix.get_3d_Scale(ScaleFactor)


    def clean_rotation_matrix(matrix):
        #&Somtimes python gives you 1.2246467991473532e-16 for a floting point error so this just goes through the matrix and replaces that with 0
        MatrixIndex = 0
        VectorIndex = 0
        for vector in matrix:
            for element in vector:
                if abs(element) < 1e-10:
                    matrix[MatrixIndex][VectorIndex] = 0
                VectorIndex += 1
            MatrixIndex += 1
            VectorIndex = 0
        return matrix

class EigenThings:
    def run():
        choice = int(input("What do you want to do?\n1. Get EigenVectors and Eigenvalues\n"))

        match choice:
            case 1:
                choice2 = int(input("What size matrix?\n1. 2x2\n"))
                match choice2:
                    case 1:
                        a = int(input("What is the first value?: "))
                        b = int(input("What is the second value?: "))
                        c = int(input("What is the third value?: "))
                        d = int(input("What is the fourth value?: "))

                        scale = int(input("Whas there a scale factor (lambda)?\n1. Yes\n2. No\n"))

                        if(scale == 1):
                            sclaeFactor = int(input("What is the scale value?: "))
                        else:
                            eigenthings.get_2x2_eigenvalues_and_eigenvectors([[a, b], [c, d]], 0)
