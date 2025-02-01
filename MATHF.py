from math import sqrt


def factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)


def fib(n):
    a = 1
    b = 1
    fib_seq = [a, b]
    for _ in range(n - 2):
        a, b = b, a + b
        fib_seq.append(b)
    return fib_seq


def pascal_row(n):
    return pascal(n)[n - 1]


def pascal(n):
    def factorial(num):
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

    def binomial_coefficient(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))

    triangle = []
    for i in range(n + 1):
        row = [binomial_coefficient(i, k) for k in range(i + 1)]
        triangle.append(row)
    return triangle


def binomial_expansion(n):
    triangle = pascal(n)
    terms = []
    for k in range(n + 1):
        coef = triangle[n][k]
        if coef == 1 and (n - k > 0 or k > 0):
            term = ""
        else:
            term = str(coef)
        if n - k > 0:
            term += "a" + (("^" + str(n - k)) if (n - k) > 1 else "")
        if k > 0:
            term += "b" + (("^" + str(k)) if k > 1 else "")
        terms.append(term)
    return " + ".join(terms)


def solve_quadratic(a, b, c):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def stringify_fraction(n, d):
        g = gcd(abs(n), abs(d))
        n //= g
        d //= g
        if d == 1:
            return str(n)
        return str(n) + "/" + str(d)

    def simplify_radical(a, d):
        h = 1
        j = 1
        while j * j <= a:
            if a % (j * j) == 0:
                h = j
            j += 1
        remaining = a // (h * h)
        fraction_str = stringify_fraction(h, d)
        if remaining == 1:
            return fraction_str
        if fraction_str == "1":
            return "\u00B1sqrt(" + str(remaining) + ")"
        return "\u00B1(" + fraction_str + ")sqrt(" + str(remaining) + ")"

    def is_perfect_square(n):
        i = 0
        while i * i < n:
            i += 1
        return i * i == n

    two_a = 2 * a
    eq_str = "\nSolving: "
    if a != 1:
        eq_str += str(a)
    eq_str += "x²"
    eq_str += "+" if b >= 0 else "-"
    if abs(b) != 1:
        eq_str += str(abs(b))
    eq_str += "x"
    eq_str += "+" if c >= 0 else "-"
    eq_str += str(abs(c)) + "=0"
    print(eq_str)
    if a == 0:
        print("a cannot equal 0.")
        return
    disc = b * b - 4 * a * c
    abs_disc = abs(disc)
    e = sqrt(abs_disc)
    is_sq = is_perfect_square(abs_disc)
    if abs(disc) < 1e-10:
        print("Disc.=0, repeated root at:\nx=" + stringify_fraction(-b, two_a))
        print("in decimal:")
        print("x=" + str(-b / two_a))
    elif disc < 0:
        print("Disc.=" + str(disc) + ", two complex roots.")
        if is_sq:
            frac = stringify_fraction(int(e), two_a)
            real_part = stringify_fraction(-b, two_a)
            im_part = frac if frac != "1" else ""
            print("Complex perfect square, rational parts at:")
            print("x=" + real_part + "+" + im_part + "i")
            print("x=" + real_part + "-" + im_part + "i")
            print("in decimal:")
            print("x=" + str(-b / two_a) + "\u00B1" + str(e / two_a) + "i")
        else:
            radical = simplify_radical(abs_disc, two_a)
            print("Complex radical roots at:")
            print("x=" + stringify_fraction(-b, two_a) + radical + "i")
            print("in decimal:")
            print("x=" + str(-b / two_a) + "\u00B1" + str(e / two_a) + "i")
    else:
        print("Disc.=" + str(disc) + ", two real roots.")
        if is_sq:
            plus = stringify_fraction(-b + int(e), two_a)
            minus = stringify_fraction(-b - int(e), two_a)
            print("Real perfect square, rational roots at:")
            print("x=" + plus)
            print("x=" + minus)
            print("in decimal:")
            print("x=" + str((-b + e) / two_a))
            print("x=" + str((-b - e) / two_a))
        else:
            radical = simplify_radical(disc, two_a)
            print("Real radical roots at:")
            print("x=" + stringify_fraction(-b, two_a) + radical)
            print("in decimal:")
            print("x=" + str((-b + e) / two_a))
            print("x=" + str((-b - e) / two_a))
