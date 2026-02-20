from math import cos, sin, radians

def twod_rotate(ArrayOfVectors, angle):
    #&Turn the angle into radians becuase cos is based off radians in python 
    degAngle = angle
    angle = radians(angle)
    TransformedArrayOfVectors = []

    #&Go though all of your vectors
    for vector in ArrayOfVectors:
        x_value = vector[0]
        y_value = vector[1]

        #&[cos, -sin ] [x, y]
        new_x = x_value * cos(angle) - y_value * sin(angle)
        #&[sin, cos] [x, y]
        new_y = x_value * sin(angle) + y_value * cos(angle)

        print("\n======== ROTATION ========")
        print(f"{x_value} * cos({degAngle}) - {y_value} * sin({degAngle}) = {new_x}")
        print(f"{x_value} * sin({degAngle}) + {y_value} * cos({degAngle}) = {new_y}\n")

        TransformedArrayOfVectors.append([new_x, new_y])

    return TransformedArrayOfVectors




def construct_3x3_matrix(angle):
    choice = int(input("What axis do you want to rotate by: \n1. X\n2. Y\n3. Z\n"))
    angle = radians(angle)
    if choice == 1:
        return [
            [1,0,0],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle)]
        ]
    elif choice == 2:
        return [
            [cos(angle),0,sin(angle)],
            [0, 1, 0],
            [-sin(angle), 0, cos(angle)]
        ]
    elif choice == 3:
        return [
            [cos(angle),-sin(angle),0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1]
        ]

def construct_4x4_matrix(angle):
    choice = int(input("What axis do you want to rotate by: \n1. X\n2. Y\n3. Z\n"))
    angle = radians(angle)
    if choice == 1:
        return [
            [1,0,0,0],
            [0, cos(angle), -sin(angle),0],
            [0, sin(angle), cos(angle),0],
            [0,0,0,1]
        ]
    elif choice == 2:
        return [
            [cos(angle),0,sin(angle),0],
            [0, 1, 0,0],
            [-sin(angle), 0, cos(angle),0],
            [0,0,0,1]
        ]
    elif choice == 3:
        return [
            [cos(angle),-sin(angle),0,0],
            [sin(angle), cos(angle), 0,0],
            [0, 0, 1,0],
            [0,0,0,1]
        ]
    

    
def get_2d_rotate(angle):
    angle = radians(angle)
    return [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]