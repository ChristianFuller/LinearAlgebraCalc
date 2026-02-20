import magnitude, dot_product

def get_orthogonal(VectorA, VectorB):
    print(f"\n-------------------- Orthoginal Vector --------------------")
    print(f"Original Vector: <{VectorA[0]}, {VectorA[1]}, {VectorA[2]}>")
    print(f"Direction Vector: <{VectorB[0]}, {VectorB[1]}, {VectorB[2]}>")

    print(f"\nUsing the cross product to find the orthoginal vector:\n")
    print(f"|i     j     k |\n|{VectorA[0]}   {VectorA[1]}   {VectorA[2]}|\n|{VectorB[0]}   {VectorB[1]}   {VectorB[2]}|")

    #Cofactor Explansion
    print(f"\nCalculating the determinant:\n")
    print(f"i({VectorA[1]}*{VectorB[2]} - {VectorA[2]}*{VectorB[1]}) - j({VectorA[0]}*{VectorB[2]} - {VectorA[2]}*{VectorB[0]}) + k({VectorA[0]}*{VectorB[1]} - {VectorA[1]}*{VectorB[0]})")
    print(f"i({(VectorA[1]*VectorB[2])} - {(VectorA[2]*VectorB[1])}) - j({(VectorA[0]*VectorB[2])} - {(VectorA[2]*VectorB[0])}) + k({(VectorA[0]*VectorB[1])} - {(VectorA[1]*VectorB[0])})")

    #Calculate i, j, k values
    i = VectorA[1]*VectorB[2] - VectorA[2]*VectorB[1]
    j = -( VectorA[0]*VectorB[2] - VectorA[2]*VectorB[0])
    k = VectorA[0]*VectorB [1] - VectorA [1]* VectorB [0]
    print(f"Orthoginal Vector: <{i}, {j}, {k}>")

    print(f"\n-----Finding the Area-----\n")
    print(f"\nArea = |orthoginal vector|\n")
    print(f"Area = |<{i}, {j}, {k}>|")
    area = round(magnitude.get_magnitude([i, j, k]), 2)
    print(f"\nArea of the parallelogram formed by <{VectorA[0]}, {VectorA[1]}, {VectorA[2]}> and <{VectorB[0]}, {VectorB[1]}, {VectorB[2]}> is: {area}")
    return [i, j, k]

def check_answer(VectorA, VectorB, OrthogonalVector):
    print(f"\n-------------------- CHECKING ANSWER --------------------")
    print(f"Checking if <{VectorA[0]}, {VectorA[1]}, {VectorA[2]}> · <{OrthogonalVector[0]}, {OrthogonalVector[1]}, {OrthogonalVector[2]}> = 0")

    #The dot product is zero if the vectors are orthogonal
    dp_VectorA = dot_product.solve_dot_product_2_vectors(VectorA, OrthogonalVector)
    dp_VectorB = dot_product.solve_dot_product_2_vectors(VectorB, OrthogonalVector)
    
    #Check if both are 0
    if(dp_VectorA == 0 and dp_VectorB == 0):
        print("The orthoginal vector is correct!")
    else:
        print("The orthoginal vector is incorrect.")