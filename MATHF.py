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

    def stringify_fraction(a, b):
        g = gcd(abs(a), abs(b))
        c = a / g
        d = b / g
        return str(int(c)) + "/" + str(int(d)) if d != 1 else str(int(c))

    def simplify_radical(a, d):
        h = 1
        for j in range(1, a):
            if a / j**2 - int(a / j**2) == 0:
                h = j
        j = a / h**2
        if j == 1:
            return stringify_fraction(int(h), d)
        else:
            ify = stringify_fraction(int(h), d)
            return (
                "\u00B1"
                + ("(" + ify + ")" if ify != "1" else "")
                + "sqrt("
                + str(int(j))
                + ")"
            )

    print(
        "\nSolving: "
        + (str(a) if a != 1 else "")
        + "x²"
        + ("+" if b >= 0 else "-")
        + (str(abs(b)) if b != 1 else "")
        + "x"
        + ("+" if c >= 0 else "-")
        + str(abs(c))
        + "=0"
    )
    if a == 0:
        print("a cannot equal 0.")
        return
    disc = b * b - 4 * a * c
    e = sqrt(abs(disc))
    f = e - int(e)
    if disc == 0:
        print(
            "Disc.=0, repeated root at x="
            + stringify_fraction(-b, 2 * a),
        )
    if disc < 0:
        print("Disc.=" + str(disc) + ", two complex roots.")
        if f == 0:
            print("Complex perfect square, rational parts at:")
            ify = stringify_fraction(int(e), 2 * a)
            print(
                "x="
                + stringify_fraction(-b, 2 * a)
                + "+"
                + (ify if ify != "1" else "")
                + "i"
            )
            print(
                "x="
                + stringify_fraction(-b, 2 * a)
                + "-"
                + (ify if ify != "1" else "")
                + "i"
            )
        else:
            ify = simplify_radical(abs(disc), 2 * a)
            print("Complex radical roots at:")
            print(
                "x="
                + stringify_fraction(-b, 2 * a)
                + (ify if ify != "1" else "")
                + "i"
            )
    if disc > 0:
        print("Disc.=" + str(disc) + ", two real roots.")
        if f == 0:
            print("Real perfect square, rational roots at:")
            print("x=" + stringify_fraction(-b + int(e), 2 * a))
            print("x=" + stringify_fraction(-b - int(e), 2 * a))
        else:
            print("Real radical roots at:")
            print(
                "x="
                + stringify_fraction(-b, 2 * a)
                + simplify_radical(disc, 2 * a)
            )
