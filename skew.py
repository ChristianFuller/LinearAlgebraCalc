# | 1 k |  or | 1 0 |
# | 0 1 |     | k 1 |


def twod_skew_horizonal(ArrayofVectors, skew_number):
    SkewedArrayOfVectors = []

    #&Go though all of your vectors
    for vector in ArrayofVectors:
        x_value = vector[0]
        y_value = vector[1]

        #& [x, y] [1, k]
        new_x = x_value + (skew_number * y_value)
        #&[0, 1] [x, y]

        print("\n======== Horizontal SKEW ========")
        print(f"{x_value} + ({skew_number} * {y_value}) == {new_x}")
        print(f"[{new_x}, {y_value}]")

        SkewedArrayOfVectors.append([new_x, y_value])

    return SkewedArrayOfVectors

def twod_skew_vertical(ArrayofVectors, skew_number):
    SkewedArrayOfVectors = []

    #&Go though all of your vectors
    for vector in ArrayofVectors:
        x_value = vector[0]
        y_value = vector[1]
        #& [x, y] [1, 0] == x_value
        #&[x, y] [k, 1]
        new_y = y_value + (skew_number * x_value)

        print("\n======== Vertical SKEW ========")
        print(f"{x_value} + ({skew_number} * {y_value}) == {x_value}")
        print(f"[{x_value}, {y_value}]")

        SkewedArrayOfVectors.append([x_value, new_y])

    return SkewedArrayOfVectors




# | 1 0 k1 |  | 1 k1 0 |  | 1 0 0  |
# | 0 1 k2 |  | 0 1 0  |  | k1 1 0 |
# | 0 0 1  |  | 0 k2 1 |  | k2 0 1 |

def consturct_3d_matrix(k1,k2):
    choice = int(input("Do you want to skew the: \n1. X\n2. Y\n3. Z\n"))
    if(choice == 1):
        return[
            [1, 0, k1],
            [0, 1, k2],
            [0, 0, 1]
        ]
    if(choice == 2):
        return[
            [1, k1, 0],
            [0,1,0],
            [0,k2,1]
        ]
    if(choice == 3):
        return[
            [1,0,0],
            [k1,1,0],
            [k1,0,1]
        ]

def consturct_4d_matrix(k1,k2):
    choice = int(input("Do you want to skew the: \n1. X\n2. Y\n3. Z\n"))
    if(choice == 1):
        return[
            [1, 0, k1,0],
            [0, 1, k2,0],
            [0, 0, 1,0],
            [0,0,0,1]
        ]
    if(choice == 2):
        return[
            [1, k1, 0,0],
            [0,1,0,0],
            [0,k2,1,0],
            [0,0,0,1]
        ]
    if(choice == 3):
        return[
            [1,0,0,0],
            [k1,1,0,0],
            [k1,0,1,0],
            [0,0,0,1]
        ]
    
def get_2d_skew_horizontal(k):
    return [[1,k], [0,1]]

def get_2d_skew_vertical(k):
    return [[1,0], [k,1]]