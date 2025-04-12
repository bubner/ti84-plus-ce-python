from math import asin, sin, acos, sqrt, cos, radians, degrees, pi

def sine_rule_solve_angle(opposite_side, angle, side):
    return asin(side * sin(angle) / opposite_side)

def sine_rule_solve_side(opposite_side, angle, target_angle):
    return opposite_side * sin(target_angle) / sin(angle)

def cosine_rule_solve_angle(a, b, c):
    return acos((a**2 + b**2 - c**2) / (2 * a * b))

def cosine_rule_solve_side(a, b, C):
    return sqrt(a**2 + b**2 - 2 * a * b * cos(C))

def ssa(known_side, known_angle, other_side, known_side_label, other_side_label, third_side_label):
    other_angle_1 = sine_rule_solve_angle(known_side, known_angle, other_side)
    if other_angle_1 is None:
        print("SSA invalid.")
        return None
    other_angle_2 = pi - other_angle_1
    third_angle_1 = pi - known_angle - other_angle_1
    third_angle_2 = pi - known_angle - other_angle_2
    third_side_1 = sine_rule_solve_side(known_side, known_angle, third_angle_1)
    third_side_2 = sine_rule_solve_side(known_side, known_angle, third_angle_2)
    print("Triangle(1,angsum=" + str(round(degrees(abs(known_angle) + abs(other_angle_1) + abs(third_angle_1)), 1)) + "/180.0°):")
    print(known_side_label.upper() + "=" + str(round(degrees(known_angle), 2)) + "°, " +
          other_side_label.upper() + "=" + str(round(degrees(other_angle_1), 2)) + "°, " +
          third_side_label.upper() + "=" + str(round(degrees(third_angle_1), 2)) + "°")
    print(known_side_label + "=" + str(round(known_side, 2)) + ", " +
          other_side_label + "=" + str(round(other_side, 2)) + ", " +
          third_side_label + "=" + str(round(third_side_1, 2)))
    print("Triangle(2,angsum=" + str(round(degrees(abs(known_angle) + abs(other_angle_2) + abs(third_angle_2)), 1)) + "/180.0°):")
    print(known_side_label.upper() + "=" + str(round(degrees(known_angle), 2)) + "°, " +
          other_side_label.upper() + "=" + str(round(degrees(other_angle_2), 2)) + "°, " +
          third_side_label.upper() + "=" + str(round(degrees(third_angle_2), 2)) + "°")
    print(known_side_label + "=" + str(round(known_side, 2)) + ", " +
          other_side_label + "=" + str(round(other_side, 2)) + ", " +
          third_side_label + "=" + str(round(third_side_2, 2)))
    return True

def solve_triangle(triangle):
    if sum(x is not None for x in triangle) < 3:
        print("Triangle invalid.")
        return
    a = triangle[0]
    A = radians(triangle[1]) if triangle[1] else None
    b = triangle[2]
    B = radians(triangle[3]) if triangle[3] else None
    c = triangle[4]
    C = radians(triangle[5]) if triangle[5] else None
    # SSS (all sides)
    if a and b and c:
        print("SSS triangle.")
        A = cosine_rule_solve_angle(b, c, a)
        B = cosine_rule_solve_angle(a, c, b)
        C = pi - A - B
    # SAS (two sides and included angle)
    elif a and b and C:
        print("SAS(abC) triangle.")
        c = cosine_rule_solve_side(a, b, C)
        A = cosine_rule_solve_angle(b, c, a)
        B = pi - A - C
    elif a and c and B:
        print("SAS(acB) triangle.")
        b = cosine_rule_solve_side(a, c, B)
        A = cosine_rule_solve_angle(c, b, a)
        C = pi - A - B
    elif b and c and A:
        print("SAS(bcA) triangle.")
        a = cosine_rule_solve_side(b, c, A)
        B = cosine_rule_solve_angle(c, a, b)
        C = pi - A - B 
    # SSA (ambiguous)
    elif a and b and A:
        print("SSA(abA) triangle.")
        if ssa(a, A, b, "a", "b", "c"):
            return
    elif b and c and B:
        print("SSA(bcB) triangle.")
        if ssa(b, B, c, "b", "c", "a"):
            return
    elif c and a and C:
        print("SSA(caC) triangle.")
        if ssa(c, C, a, "c", "a", "b"):
            return
    elif a and b and B:
        print("SSA(abB) triangle.")
        if ssa(b, B, a, "b", "a", "c"):
            return
    elif b and c and C:
        print("SSA(bcC) triangle.")
        if ssa(c, C, b, "c", "b", "a"):
            return
    elif c and a and A:
        print("SSA(caA) triangle.")
        if ssa(a, A, c, "a", "c", "b"):
            return
    # Can be ASA or AAS, but this is the last case so we try anyways
    else:
        print("ASA/AAS triangle.")
        if not A:
            A = pi - B - C
        elif not B:
            B = pi - A - C
        elif not C:
            C = pi - A - B
        if a:
            b = sine_rule_solve_side(a, A, B)
            c = sine_rule_solve_side(a, A, C)
        elif b:
            a = sine_rule_solve_side(b, B, A)
            c = sine_rule_solve_side(b, B, C)
        elif c:
            a = sine_rule_solve_side(c, C, A)
            b = sine_rule_solve_side(c, C, B)
    print("Triangle(angsum=" + str(round(degrees(abs(A) + abs(B) + abs(C)), 1)) + "/180.0°):")
    print("A=" + str(round(degrees(A), 2)) + "°, B=" + str(round(degrees(B), 2)) + "°, C=" + str(round(degrees(C), 2)) + "°")
    print("a=" + str(round(a, 2)) + ", b=" + str(round(b, 2)) + ", c=" + str(round(c, 2)))

def main():
    triangle = [
        input("Side a: "),
        input("Angle A°: "),
        input("Side b: "),
        input("Angle B°: "),
        input("Side c: "),
        input("Angle C°: ")
    ]
    solve_triangle(list(map(lambda x: float(x) if x else None, triangle)))

main()