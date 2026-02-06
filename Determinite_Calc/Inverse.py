from . import Determinite
from fractions import Fraction

def inverse(choice):
    # 1 = 2x2, 2 = 3x3
    if choice == "1":
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        c = int(input("Enter the value of c: "))
        d = int(input("Enter the value of d: "))
        x = int(input("Enter the value of x (answer to first equation): "))
        y = int(input("Enter the value of y (answer to second equation): "))
        determinant = Determinite.two_by_two_determinant(a, b, c, d)

        if determinant == 0:
            print("The determinant is 0, no inverse exists.")
            return
        
        Co = [d, -c, -b, a]
        print("\nThe cofactor matrix is: ")
        print(Co[0], Co[1])
        print(Co[2], Co[3])

        ctranspose = [Co[0], Co[2], Co[1], Co[3]]
        print("\nThe cofactor matrix transposed is: ")
        print(ctranspose[0], ctranspose[1])
        print(ctranspose[2], ctranspose[3])

        print("\nFraction into C-Transpose: ")
        adjugate_divided = 1/determinant
        print("1 /", determinant, " * C-Transpose")
        answer = [adjugate_divided * ctranspose[0], adjugate_divided * ctranspose[1], adjugate_divided * ctranspose[2], adjugate_divided * ctranspose[3]]
        print('\nAnswer: ')
        print(answer[0], answer[1])
        print(answer[2], answer[3])
        print("\nChecking answer")
        print("\nOriginal Matrix: ")
        print(a, b)
        print(c, d)
        print("\nInverse Matrix: ")
        print(answer[0], answer[1])
        print(answer[2], answer[3])
        print("\nMultiplying them together: ")
        answerCheck = [a * answer[0] + b * answer[2], a * answer[1] + b * answer[3], c * answer[0] + d * answer[2], c * answer[1] + d * answer[3]]
        if(answerCheck[0] == 1 and answerCheck[1] == 0 and answerCheck[2] == 0 and answerCheck[3] == 1):
            print("\nThe answer is correct, the product is the identity matrix.")
            print(a * answer[0] + b * answer[2], a * answer[1] + b * answer[3])
            print(c * answer[0] + d * answer[2], c * answer[1] + d * answer[3])

            # a b X Y X * a + y * c + a * b + y * d
            # c d

            print("\n X and Y values:")
            X = answer[0] * x + answer[1] * y
            Y = answer[2] * x + answer[3] * y
            print("x =", X)
            print("y =", Y)
        else:
            print("The answer is incorrect, the product is not the identity matrix.")
            print(a * answer[0] + b * answer[2], a * answer[1] + b * answer[3])
            print(c * answer[0] + d * answer[2], c * answer[1] + d * answer[3])
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
        x = int(input("Enter the value of x (answer to first equation): "))
        y = int(input("Enter the value of y (answer to second equation): "))
        z = int(input("Enter the value of z (answer to third equation): "))
        determinant = Determinite.three_by_three_determinite_equation(a, b, c, d, e, f, g, h, i)
        if determinant == 0:
            print("The determinant is 0, no inverse exists.")
            return

        Co = [Determinite.two_by_two_determinant(e, f, h, i),
            -Determinite.two_by_two_determinant(d, f, g, i),
            Determinite.two_by_two_determinant(d, e, g, h),
            -Determinite.two_by_two_determinant(b, c, h, i), 
            Determinite.two_by_two_determinant(a, c, g, i), 
            -Determinite.two_by_two_determinant(a, b, g, h), 
            Determinite.two_by_two_determinant(b, c, e, f), 
            -Determinite.two_by_two_determinant(a, c, d, f), 
            Determinite.two_by_two_determinant(a, b, d, e)]
        print("\nThe cofactor matrix is: ")
        print(Co[0], Co[1], Co[2])
        print(Co[3], Co[4], Co[5])
        print(Co[6], Co[7], Co[8])

        ctranspose = [Co[0], Co[3], Co[6], Co[1], Co[4], Co[7], Co[2], Co[5], Co[8]]
        print("\nThe cofactor matrix transposed is: ")
        print(ctranspose[0], ctranspose[1], ctranspose[2])
        print(ctranspose[3], ctranspose[4], ctranspose[5])
        print(ctranspose[6], ctranspose[7], ctranspose[8])

        answer = [ctranspose[0] / determinant, ctranspose[1] / determinant, ctranspose[2] / determinant,
                ctranspose[3] / determinant, ctranspose[4] / determinant, ctranspose[5] / determinant,
                ctranspose[6] / determinant, ctranspose[7] / determinant, ctranspose[8] / determinant]
        print("\nChecking answer...")
        print("\nOriginal Matrix: ")
        print(a, b, c)
        print(d, e, f)
        print(g, h, i)
        ans1 = Fraction(answer[0]).limit_denominator()
        ans2 = Fraction(answer[1]).limit_denominator()
        ans3 = Fraction(answer[2]).limit_denominator()
        ans4 = Fraction(answer[3]).limit_denominator()
        ans5 = Fraction(answer[4]).limit_denominator()
        ans6 = Fraction(answer[5]).limit_denominator()
        ans7 = Fraction(answer[6]).limit_denominator()
        ans8 = Fraction(answer[7]).limit_denominator()
        ans9 = Fraction(answer[8]).limit_denominator()

        print("\nFractioned Inverse Matrix: ")
        print(ans1, ans2, ans3)
        print(ans4, ans5, ans6)
        print(ans7, ans8, ans9)
        print("\nMultiplying them together: ")
        # 0 1 2 | a b c |  0 * a + 1 * d + 2 * g, 0 * b + 1 * e + 2 * h, 0 * c + 1 * f + 2 * i 
        # 3 4 5 | d e f |  3 * a ++ 4 * d ++ 5 * g,,,, 3 * b ++ 4 * e ++ 5 * h,,,, 3 * c ++ 4 * f ++ 5 * i
        # 6 7 8 | g h i |  6 * a ++ 7 * d ++ 8 * g,,,, 6 * b ++ 7 * e ++ 8 * h,,,, 6 * c ++ 7 * f ++ 8 * i
        #2, 1, -1, 1, -3, 2, 3, 2, 1

        answerCheck = [a * ans1 + d * ans2 + g * ans3, 
                    b * ans1 + e * ans2 + h * ans3,
                    c * ans1 + f * ans2 + i * ans3,
                    a * ans4 + d * ans5 + g * ans6,
                    b * ans4 + e * ans5 + h * ans6,
                    c * ans4 + f * ans5 + i * ans6,
                    a * ans7 + d * ans8 + g * ans9,
                    b * ans7 + e * ans8 + h * ans9,
                    c * ans7 + f * ans8 + i * ans9]
    

        print(answerCheck[0], answerCheck[1], answerCheck[2])
        print(answerCheck[3], answerCheck[4], answerCheck[5])
        print(answerCheck[6], answerCheck[7], answerCheck[8])

        if(answerCheck[0] == 1 
        and answerCheck[1] == 0 
        and answerCheck[2] == 0
        and answerCheck[3] == 0
        and answerCheck[4] == 1
        and answerCheck[5] == 0
        and answerCheck[6] == 0
        and answerCheck[7] == 0
        and answerCheck[8] == 1):
            print("\nInverse is correct!")

            X = ans1 * x + ans2 * y + ans3 * z
            Y = ans4 * x + ans5 * y + ans6 * z
            Z = ans7 * x + ans8 * y + ans9 * z
            print("\n---- X, Y and Z values: ", X, Y, Z, "----\n")
        else:
            print("\nInverse is wrong")