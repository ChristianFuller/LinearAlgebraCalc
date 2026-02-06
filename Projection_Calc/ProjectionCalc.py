from . import magnitude
from . import angle
from . import dot_product
from . import projection
from . import v_s
from . import threeD_shortcut

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
        VectorSize = int(input("How many elements are in the vector?\n"))
        elements = 0
        Vector = []
        while(elements < VectorSize):
            Vector.append(int(input(f"\nElement {elements} for Vector:")))
            elements += 1
        magnitude.get_magnitude(Vector)
    elif(choice == 3):
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
        dot_product.solve_dot_product_2_vectors(VectorA, VectorB)
    elif(choice == 4):
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