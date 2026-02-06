from fractions import Fraction

intx = 1

def two_by_two_determinant(a, b, c, d):
    print(f"({a} * {d}) - ({b} * {c})")
    determinant = (a * d) - (b * c)
    print("The determinant is: ", determinant, "\n")
    return determinant

def three_by_three_determinant(a, b, c, d, e, f, g, h, i, answer1, answer2, answer3):
    #using diagonal method
    print("Finding Determinant: ")
    print(f"(({a} * {e} * {i}) + ({b} * {f} * {g}) + ({c} * {d} * {h}))  - (({b} * {d} * {i}) + ({a} * {f} * {h}) + ({c} * {e} * {g}))")
    da = ((a * e * i) + (b * f * g) + (c * d * h))  - ((b * d * i) + (a * f * h) + (c * e * g))
    if da == 0:
        print("\nThe determinant is 0, no solution.")
        return
    print(f"\n Determinant found: {da}")
    print("\nDoing diagonal Method...")
    dx = ((answer1 * e * i) + (b * f * answer3) + (c * answer2 * h))  - ((b * answer2 * i) + (answer1 * f * h) + (c * e * answer3))
    dy = ((a * answer2 * i) + (answer1 * f * g) + (c * d * answer3))  - ((answer1 * d * i) + (a * f * answer3) + (c * answer2 * g))
    dz = ((a * e * answer3) + (b * answer2 * g) + (answer1 * d * h))  - ((b * d * answer3) + (a * answer2 * h) + (answer1 * e * g))
    print(f"\ndx = (({answer1} * {e} * {i}) + ({b} * {f} * {answer3}) + ({c} * {answer2} * {h})) - (({b} * {answer2} * {i}) + ({answer1} * {f} * {h}) + ({c} * {e} * {answer3})) == {dx}")
    print(f"\ndy = (({a} * {answer2} * {i}) + ({answer1} * {f} * {g}) + ({c} * {d} * {answer3})) - (({answer1} * {d} * {i}) + ({a} * {f} * {answer3}) + ({c} * {answer2} * {g})) == {dy}")
    print(f"\ndz = (({a} * {e} * {answer3}) + ({b} * {answer2} * {g}) + ({answer1} * {d} * {h})) - (({b} * {d} * {answer3}) + ({a} * {answer2} * {h}) + ({answer1} * {e} * {g})) == {dz}")
    print("\nFinding X, Y, Z")
    print(f"\nX = {dx} / {da}")
    print(f"\nY = {dy} / {da}")
    print(f"\nZ = {dz} / {da}")
    x = dx / da
    y = dy / da
    z = dz / da
    fractionx = Fraction(x).limit_denominator()
    fractiony = Fraction(y).limit_denominator()
    fractionz = Fraction(z).limit_denominator()
    print("\nX, Y, Z: ", x, f"({fractionx}),", y, f"({fractiony}),", z, f"({fractionz})")
    return [da, x, y, z]

def three_by_three_determinite_equation(a, b, c, d, e, f, g, h, i):
    #a b c
    #d e f
    #g h i
        print(f'''\nEquation:
                    a * |{e} {f}| - b * |{d} {f}| + c * |{d} {e}|
                        |{h} {i}|       |{g} {i}|       |{g} {h}|
                ''')
        d1 = a * ((e * i) - (f * h))
        d2 = -b * ((d * i) - (f * g))
        d3 = c * ((d * h) - (e * g))
        determinant = d1 + d2 + d3
        print(intx, ". The 3x3 determinant is: ", determinant)
        return determinant

def four_by_four_determinant(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,answer1,answer2,answer3,answer4):
    global intx
    #use equasion to get the determinant of 4x4 matrix
    # |a b c d|
    # |e f g h| |e f | //       |f g h| |f g| //       |e g h| |e g| //        |e f h| |e f| //        |e f g| |e f|
    # |i j k l| |i j | // a ->  |j k l| |j k| // b ->  |i k l| |i k| // c ->   |i j l| |i j| // -> d   |i j k| |i j|
    # |m n o p| |m n | //       |n o p| |n o|  //      |m o p| |m o| //        |m n p| |m n| //        |m n o| |m n|
    # 1 2 3 4 , 0 5 6 7, 2 4 6 7, 3 6 7 8

    # Org Determinite
    d1 = a * three_by_three_determinite_equation(f, g, h, j, k, l, n, o, p)
    d2 = -b * three_by_three_determinite_equation(e, g, h, i, k, l, m, o, p)
    d3 = c * three_by_three_determinite_equation(e, f, h, i, j, l, m, n, p)
    d4 = -d * three_by_three_determinite_equation(e, f, g, i, j, k, m, n, o)
    determinite = d1 + d2 + d3 + d4

    intx = intx + 1

    # Answers of the equations
    dx1 = answer1 * three_by_three_determinite_equation(f, g, h, j, k, l, n, o, p)
    dx2 = -b * three_by_three_determinite_equation(answer2, g, h, answer3, k, l, answer4, o, p)
    dx3 = c * three_by_three_determinite_equation(answer2, f, h, answer3, j, l, answer4, n, p)
    dx4 = -d * three_by_three_determinite_equation(answer2, f, g, answer3, j, k, answer4, n, o)
    determinant_x = dx1 + dx2 + dx3 + dx4

    intx = intx + 1

    dy1 = a * three_by_three_determinite_equation(answer2, g, h, answer3, k, l, answer4, o, p)
    dy2 = -answer1 * three_by_three_determinite_equation(e, g, h, i, k, l, m, o, p)
    dy3 = c * three_by_three_determinite_equation(e, answer2, h, i, answer3, l, m, answer4, p)
    dy4 = -d * three_by_three_determinite_equation(e, answer2, g, i, answer3, k, m, answer4, o)
    determinante_y = dy1 + dy2 + dy3 + dy4

    intx = intx + 1

    dz1 = a * three_by_three_determinite_equation(f, answer2, h, j, answer3, l, n, answer4, p)
    dz2 = -b * three_by_three_determinite_equation(e, answer2, h, i, answer3, l, m, answer4, p)
    dz3 = answer1 * three_by_three_determinite_equation(e, f, h, i, j, l, m, n, p)
    dz4 = -d * three_by_three_determinite_equation(e, f, answer2, i, j, answer3, m, n, answer4)
    determinante_z = dz1 + dz2 + dz3 + dz4

    intx = intx + 1

    dw1 = a * three_by_three_determinite_equation(f, g, answer2, j, k, answer3, n, o, answer4)
    dw2 = -b * three_by_three_determinite_equation(e, g, answer2, i, k, answer3, m, o, answer4)
    dw3 = c * three_by_three_determinite_equation(e, f, answer2, i, j, answer3, m, n, answer4)
    dw4 = -answer1 * three_by_three_determinite_equation(e, f, g, i, j, k, m, n, o)
    determinate_w = dw1 + dw2 + dw3 + dw4

    x = determinant_x / determinite
    y = determinante_y / determinite
    z = determinante_z / determinite
    w = determinate_w / determinite

    Fractionx = Fraction(x).limit_denominator()
    Fractiony = Fraction(y).limit_denominator()
    Fractionz = Fraction(z).limit_denominator()
    Fractionw = Fraction(w).limit_denominator()

    print("\n----The 4x4 determinant is: ", determinite, "----")
    print("X, Y, Z, W: ", x, f"({Fractionx}),", y, f"({Fractiony}),", z, f"({Fractionz}),", w, f"({Fractionw})")