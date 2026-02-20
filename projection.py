import magnitude, dot_product
from math import sqrt

def get_projection(VectorA, VectorB):

    A_or_B = input("What is the proj of a and b?\n1.Proj_a(b)\n2.Proj_b(a)\n")
    dp = dot_product.solve_dot_product_2_vectors(VectorA, VectorB)
    if(A_or_B == '1'):

        print(f"\n-------------------- Projection of B onto A --------------------")
        print(f"Proj_{VectorA[0]}({VectorA[1]})")

        #X value
        print(f"\n-----X Value-----")
        print(f"\n(Dot Product / Magnitude of A Squared) * VectorA_x")
        projx = (dp)/(magnitude.get_magnitude(VectorA)**2) * VectorA[0]

        #Print steps for X value
        print(f"{VectorA[0]} * {VectorB[0]} + {VectorA[1]} * {VectorB[1]} / ({VectorA[0]}^2 + {VectorA[1]}^2) * {VectorA[0]}")
        print(f"{VectorA[0]*VectorB[0]} + {VectorA[1]*VectorB[1]} / ({VectorA[0]*VectorA[0]} + {VectorA[1]*VectorA[1]}) * {VectorA[0]}")
        print(f"{(VectorA[0]*VectorB[0] + VectorA[1]*VectorB[1])} / ({VectorA[0]*VectorA[0] + VectorA[1]*VectorA[1]}) * {VectorA[0]}")
        print(f"{(VectorA[0]*VectorB[0] + VectorA[1]*VectorB[1])/(VectorA[0]*VectorA[0] + VectorA[1]*VectorA[1])} * {VectorA[0]}")
        print(f"{projx}")

        #Y value
        print(f"\n-----Y Value-----")
        print(f"\n(Dot Product / Magnitude of A Squared) * VectorA_y")
        projy = (dp)/(magnitude.get_magnitude(VectorA)**2) * VectorA[1]

        #Print steps for Y value
        print(f"{VectorA[0]} * {VectorB[0]} + {VectorA[1]} * {VectorB[1]} / ({VectorA[0]}^2 + {VectorA[1]}^2) * {VectorA[1]}")
        print(f"{VectorA[0]*VectorB[0]} + {VectorA[1]*VectorB[1]} / ({VectorA[0]*VectorA[0]} + {VectorA[1]*VectorA[1]}) * {VectorA[1]}")
        print(f"{(VectorA[0]*VectorB[0] + VectorA[1]*VectorB[1])} / ({VectorA[0]*VectorA[0] + VectorA[1]*VectorA[1]}) * {VectorA[1]}")
        print(f"{(VectorA[0]*VectorB[0] + VectorA[1]*VectorB[1])/(VectorA[0]*VectorA[0] + VectorA[1]*VectorA[1])} * {VectorA[1]}")
        print(f"{projy}")

        print(f"X: {projx}, Y: {projy}")
        
        #Finding B2
        print(f"\n----- Finding B2 -----")
        b2 = (VectorB[0] - projx) + (VectorB[1] - projy)
        print(f"B2 = ({VectorB[0]} - {projx}) + ({VectorB[1]} - {projy})")
        print(f"B2 = {VectorB[0] - projx} + {VectorB[1] - projy}")
        print(f"B2 = {b2}")
        return projx, projy, b2
    elif(A_or_B == '2'):
        print(f"\n-------------------- Projection of A onto B --------------------")
        print(f"Proj_{VectorB[0]}({VectorB[1]})")

        #X value
        print(f"\n-----X Value-----")
        print(f"\n(Dot Product / Magnitude of B Squared) * VectorB_x")
        projx = (dp)/(magnitude.get_magnitude(VectorB)**2) * VectorB[0]

        #Print steps for X value
        print(f"{VectorA[0]} * {VectorB[0]} + {VectorA[1]} * {VectorB[1]} / ({VectorB[0]}^2 + {VectorB[1]}^2) * {VectorB[0]}")
        print(f"{VectorA[0]*VectorB[0]} + {VectorA[1]*VectorB[1]} / ({VectorB[0]*VectorB[0]} + {VectorB[1]*VectorB[1]}) * {VectorB[0]}")
        print(f"{(VectorA[0]*VectorB[0] + VectorA[1]*VectorB[1])} / ({VectorB[0]*VectorB[0] + VectorB[1]*VectorB[1]}) * {VectorB[0]}")
        print(f"{(VectorA[0]*VectorB[0] + VectorA[1]*VectorB[1])/(VectorB[0]*VectorB[0] + VectorB[1]*VectorB[1])} * {VectorB[0]}")
        print(f"{projx}")

        #Y value
        print(f"\n-----Y Value-----")
        print(f"\n(Dot Product / Magnitude of B Squared) * VectorB_y")
        projy = (dp)/(magnitude.get_magnitude(VectorB)**2) * VectorB[1]

        #Print steps for Y value
        print(f"{VectorA[0]} * {VectorB[0]} + {VectorA[1]} * {VectorB[1]} / ({VectorB[0]}^2 + {VectorB[1]}^2) * {VectorB[1]}")
        print(f"{VectorA[0]*VectorB[0]} + {VectorA[1]*VectorB[1]} / ({VectorB[0]*VectorB[0]} + {VectorB[1]*VectorB[1]}) * {VectorB[1]}")
        print(f"{(VectorA[0]*VectorB[0] + VectorA[1]*VectorB[1])} / ({VectorB[0]*VectorB[0] + VectorB[1]*VectorB[1]}) * {VectorB[1]}")
        print(f"{(VectorA[0]*VectorB[0] + VectorA[1]*VectorB[1])/(VectorB[0]*VectorB[0] + VectorB[1]*VectorB[1])} * {VectorB[1]}")
        print(f"{projy}")

        print(f"X: {projx}, Y: {projy}")
        
        #Finding A2
        print(f"\n----- Finding A2 -----")
        a2 = (VectorB[0] - projx) + (VectorB[1] - projy)
        print(f"B2 = ({VectorB[0]} - {projx}) + ({VectorB[1]} - {projy})")
        print(f"B2 = {VectorB[0] - projx} + {VectorB[1] - projy}")
        print(f"B2 = {a2}")
        return projx, projy, a2
