

def scale(Vector, ScaleNumber, HowManyRowsorColumns):

    RotatedElements = []
    ArrayOfTransformedVectors = []
    print("------- Scale -------")

    # 1 2 3 4 
    # 5 6 7 8
    # 9 8 7 6
    # 5 4 3 2


    #& Go through the vecctor
    vectorIndex = 0
    #&Add one so its the size + 1 (Diagonal)
    Size = HowManyRowsorColumns + 1
    #&Go through Vector
    for element in Vector:
        #&Diagonal Points
        if(vectorIndex == 0):
            #& Multiply
            print(f"Vector: {Vector}")
            print(f"Multiplication: {element} * {ScaleNumber}")
            RotatedElements.append(element * ScaleNumber)
        elif(vectorIndex == Size):
            #&Keep the diagonal
            Size += HowManyRowsorColumns + 1
            print(f"Vector: {Vector}")
            print(f"Multiplication: {element} * {ScaleNumber}")
            RotatedElements.append(element * ScaleNumber)
        else:
            RotatedElements.append(element)
        vectorIndex += 1
    return RotatedElements