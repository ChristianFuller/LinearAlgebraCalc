def get_magnitude(Vector):
    from math import sqrt
    BelowSqrt = []
    print("\n-------------------- MAGNITUDE --------------------")

    #Add the squares to array
    for i in range(len(Vector)):
        BelowSqrt.append(Vector[i] * Vector[i])
        print(f"\nElement {i}: {Vector[i]}^2 = {BelowSqrt[i]}")

    TotalUnderSqrt = 0
    #Go through array and sum the squares
    for i in BelowSqrt:
        TotalUnderSqrt += i
        print(f"\nAdding {i} to total under sqrt: {TotalUnderSqrt}")

    #Calculate Magnitude
    magnitude = sqrt(TotalUnderSqrt)
    print(f"\nMagnitude: sqrt({TotalUnderSqrt}) = {magnitude}")
    return magnitude