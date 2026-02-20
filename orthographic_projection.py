import magnitude

# | 1 0 | or | 0 0 |
# | 0 0 |    | 0 1 |

#&Reflection

# | 1 0  | or | -1 0 |
# | 0 -1 |    | 0  1 |


projectedArrayOfVectors = []

#!Regular projetion
def twod_project_horizonal(ArrayofVectors):
    return project(0,0,0,1, ArrayofVectors)

def twod_project_vertical(ArrayofVectors):
    return project(1,0,0,0, ArrayofVectors)

#!reflection
def twod_project_vertical_reflection(ArrayofVectors):
    return project(1,0,0,-1, ArrayofVectors)

def twod_project_horizontal_reflection(ArrayofVectors):
    return project(-1,0,0,1, ArrayofVectors)

#!Project for dry code
def project(a,b,c,d, ArrayofVectors):
    print(f"------ Projection ------")
    #&Go through Vectors and multiply them to the projection
    for vector in ArrayofVectors:
        print(f"({vector[0]} * {a}) + ({vector[1]} * {b}), ({vector[0]} * {c}) + ({vector[1]} * {d})")
        projectedArrayOfVectors.append([(vector[0] * a) + (vector[1] * b), (vector[0] * c) + (vector[1] * d)])
    return projectedArrayOfVectors

def threed_projection_formula():
    choice = int(input("Do you want to project the: \n1. X\n2. Y\n3. Z\n"))
    if(choice == 1):
        return[
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    if(choice == 2):
        return[
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]
    if(choice == 3):
        return[
            [0,0,0],
            [0,1,0],
            [0,0,1]
        ]

#!3DProject
def construct_2x2_projection(x,y):
    #&Make sure [x,y,z] is a unit vector 
    x,y = normalize(x,y)
    #&Return the 
    print(f"(1 - ({x} * {x}), -({x} * {y}), -({x} * {y}), 1 - ({y} * {y})")
    return [
    [round(1 - (x * x), 3), round(-(x * y), 3)],
    [round(-(x * y), 3), round(1 - (y * y), 3)]
]

#!3DProject
def construct_2x2_reflection(x,y):
    #&Make sure [x,y,z] is a unit vector 
    x,y = normalize(x,y)
    print(f"1 - (2 * ({x} * {x})), -(2 * ({x} * {y})), -(2 * ({x} * {y})), 1 - (2 * ({y} * {y}))")
    #&Return the 
    return [
    [round(1 - (2 * (x * x)), 3), round(-(2 * (x * y)), 3)],
    [round(-(2 * (x * y)), 3), round(1 - (2 * (y * y)), 3)]
]


#!3DProject
def construct_3x3_projection(x,y,z):
    #&Make sure [x,y,z] is a unit vector 
    x,y,z = normalize(x,y,z)
    print(f"1 - ({x} * {x}), -({x} * {y}), -({x} * {z}), "
      f"-({x} * {y}), 1 - ({y} * {y}), -({y} * {z}), "
      f"-({x} * {z}), -({y} * {z}), 1 - ({z} * {z})")
    return [
    [round(1 - (x * x), 3), round(-(x * y), 3), round(-(x * z), 3)],
    [round(-(x * y), 3), round(1 - (y * y), 3), round(-(y * z), 3)],
    [round(-(x * z), 3), round(-(y * z), 3), round(1 - (z * z), 3)]
]

def construct_3x3_reflection(x,y,z):
    #&Make sure [x,y,z] is a unit vector 
    x,y,z = normalize(x,y,z)
    print(f"1 - (2 * ({x} * {x})), -(2 * ({x} * {y})), -(2 * ({x} * {z})), "
      f"-(2 * ({x} * {y})), 1 - (2 * ({y} * {y})), -(2 * ({y} * {z})), "
      f"-(2 * ({x} * {z})), -(2 * ({y} * {z})), 1 - (2 * ({z} * {z}))")
    return [
    [round(1 - (2 * (x * x)), 3), round(-(2 * (x * y)), 3), round(-(2 * (x * z)), 3)],
    [round(-(2 * (x * y)), 3), round(1 - (2 * (y * y)), 3), round(-(2 * (y * z)), 3)],
    [round(-(2 * (x * z)), 3), round(-(2 * (y * z)), 3), round(1 - (2 * (z * z)), 3)]
]


def normalize(x, y, z=None):
    
    #& Get magnitude to devide
    if(z == None):
        mag = magnitude.get_magnitude([x,y])
    else:
        mag = magnitude.get_magnitude([x,y,z])
    
    if mag == 0:
        raise ValueError("Zero vector not allowed.")
    
    #&Normalize to unit vector
    x = x / mag
    y = y / mag
    if(z != None):
        z = z / mag
        return x, y, z
    else:
        return x,y

def get_2x2_Projection_horizontal():
    return [[0,0], [0,1]]
def get_2x2_Projection_vertical():
    return [[1,0], [0,0]]

def get_2x2_Reflection_vertical():
    return [[1,0], [0,-1]]
def get_2x2_Reflection_horizontal():
    return [[-1,0], [0,1]]