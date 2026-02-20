from math import acos, degrees, pi

def solve_Angle(dot_product, ArrayOfMagnitudes):


    print("\n-------------------- ANGLE --------------------")
    print(f"Dot product: {dot_product}\n")
    print(f"Magnitudes: {ArrayOfMagnitudes}\n")
    print(f"CosInverse(theta) = dot_product / (Magnitudes multiplied then added together)")
    TotalValue = 0
    # Get the total of all of the magnitudes multiplied together
    for i in range(len(ArrayOfMagnitudes)):
        #If first magnitude
        if(i == 0):
            TotalValue = ArrayOfMagnitudes[i]
        #Else, multiply the next magnitude
        else:
            print(f"{TotalValue} * {ArrayOfMagnitudes[i]} = {TotalValue * ArrayOfMagnitudes[i]}")
            TotalValue = TotalValue * ArrayOfMagnitudes[i]

    #Get the fraction for cox_inv(theta)
    print(f"{dot_product} / {TotalValue}")
    print(f"OR {dot_product} / sqrt{int(TotalValue**2)}")
    cos_angle = dot_product / TotalValue
    cos_angle = max(-1, min(1, cos_angle))

    #Get the Angle
    print(f"cos[inverse]({dot_product} / {TotalValue})")
    angle_deg = degrees(acos(cos_angle))
    print(f"Angle: {angle_deg} degrees\n")
    return angle_deg