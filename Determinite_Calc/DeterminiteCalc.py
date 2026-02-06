from . import Determinite
from . import Inverse

def run():
    choice = input("Choose Detrminite size\n1 for 2x2\n2 for 3x3\n3 for 4x4\n4 for finding inverse\n5. Go back\n")

    if choice == "1":
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))
        d = int(input("Enter the value of d: "))
        Determinite.two_by_two_determinant(a, b, c, d)
    elif choice == "2":
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))
        d = int(input("Enter the value of d: "))
        e = int(input("Enter the value of e: "))
        f = int(input("Enter the value of f: "))
        g = int(input("Enter the value of g: "))
        h = int(input("Enter the value of h: "))
        i = int(input("Enter the value of i: "))
        answer1 = int(input("What is the answer to the first equation: "))
        answer2 = int(input("What is the answer to the second equation: "))
        answer3 = int(input("What is the answer to the third equation: "))
        Determinite.three_by_three_determinant(a, b, c, d, e, f, g, h, i, answer1, answer2, answer3)
    elif choice == "3":
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))
        d = int(input("Enter the value of d: "))
        e = int(input("Enter the value of e: "))
        f = int(input("Enter the value of f: "))
        g = int(input("Enter the value of g: "))
        h = int(input("Enter the value of h: "))
        i = int(input("Enter the value of i: "))
        j = int(input("Enter the value of j: "))
        k = int(input("Enter the value of k: "))
        l = int(input("Enter the value of l: "))
        m = int(input("Enter the value of m: "))
        n = int(input("Enter the value of n: "))
        o = int(input("Enter the value of o: "))
        p = int(input("Enter the value of p: "))
        answer1 = int(input("What is the answer to the first equation: "))
        answer2 = int(input("What is the answer to the second equation: "))
        answer3 = int(input("What is the answer to the third equation: "))
        answer4 = int(input("What is the answer to the fourth equation: "))
        Determinite.four_by_four_determinant(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,answer1,answer2,answer3,answer4)
    elif choice == "4":
        inverse_choice = input("Choose the size of the matrix you want to find the inverse of\n1 for 2x2:\n2 for 3x3: ")
        if inverse_choice == "1":
            Inverse.inverse(inverse_choice)
        elif inverse_choice == "2":
            Inverse.inverse(inverse_choice)
        else:
            print("Inverse for that size is not yet implemented.")
    else:
        return