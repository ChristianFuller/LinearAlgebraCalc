import magnitude, dot_product
from math import acos

def find_vs(VectorA, VectorB):
    print("\n-------------------- VECTORS --------------------")
    print(f"Finding V1")
    dp1 = dot_product.solve_dot_product_2_vectors(VectorA, VectorB)
    dp2 = dot_product.solve_dot_product_2_vectors(VectorB, VectorB)
    print(f"{round(dp1 / dp2, 2)}<{VectorB}>")
    
    #Get V1
    # Dot Product of A and B / Dot Product of B and B
    v1_scaler = round((dot_product.solve_dot_product_2_vectors(VectorA, VectorB)/(dot_product.solve_dot_product_2_vectors(VectorB, VectorB))), 2)
    print(f"Scaler: {v1_scaler}")

    # Multiply v1 by VectorB to get x and y of V1
    print(f"\nFinding V1")
    V1 = []
    for i in range(len(VectorB)):
        print(f"{v1_scaler} * {VectorB[i]}")
        V1.append(round(v1_scaler * VectorB[i], 2))
    print("V1: ", V1)

    #Get V2
    print(f"\nFinding V2\n{VectorA} - {V1}")
    #V2 = v - v1
    V2 = []
    for i in range(len(VectorA)):
        V2.append(round(VectorA[i] - V1[i], 2))

    print(f'Vector 2: {V2}')
    return V1, V2


def check_answers(VectorA, VectorB, V1, V2):

    print("\n-------------------- CHECKING ANSWERS --------------------")
    print(f'''\nChecking (v = v1 + v2)\n
        V1 + V2 = Original Vector
        <{V1} + {V2} = {VectorA}>
        ''')
    #Check if v = v1 + v2
    Check = 0
    for i in range(len(VectorA)):
        if(VectorA[i] == round(V1[i] + V2[i]), 2):
            Check += 1
    if(Check == len(VectorA)):
        print("The answers are correct!")
    else:
        print("The answers are incorrect.")
    
    #Check if v2 is perpendicular to w (v2 · w = 0)
    print(f'''\nChecking (v2 x w = 0)\n
        <{V2[0]}, {V2[1]}> x <{VectorB[0]}, {VectorB[1]}> = 0
        {(V2[0] * VectorB[0]) + (V2[1] * VectorB[1])} = 0\n
        ''')
    
    #v2 · w = 0
    if(dot_product.solve_dot_product_2_vectors(V2, VectorB) == 0):
        print("The answers are perpendicular!")
    else:
        print("The answers are not perpendicular.")
    
    #Check if v1 is parallel to w (v1 · w / (|v1||w|) = 0)
    print("\nChecking (v1 · w / (|v1||w|) = 0)")

    #Get magnitudes and dot product
    #Check if dp / |v1| x |w| = 0
    v1mag = magnitude.get_magnitude(V1)
    wmag = magnitude.get_magnitude(VectorB)

    # 1/mag (vector)
    product1 = 0
    for i in range(len(V1)):
        print(f"\nV1 values: {(1 / v1mag) * V1[i]}")
        product1 += (1 / v1mag) * V1[i]
    product2 = 0
    for i in range(len(VectorB)):
        print(f"\nW Values: {(1/wmag) * VectorB[i]}")
        product2 += (1/wmag) * VectorB[i]
    print(f"Does {product1} == {product2}")
    if(round(product1, 5) == round(product2, 5)):
        print("The answers are parallel!")
    else:
        print("The answers are not parallel.")