def main():
    sel = input("(1, SYNTHETIC) (2, LONG)=")
    if sel == "1":
        coeffs = list(map(float, input("P COEFF (csv)=").split(",")))
        a = -float(input("A (root x+A=0,P/(x+A))="))
        quot = [coeffs[0]]
        rem = 0
        for i in range(1, len(coeffs)):
            rem = a * quot[-1]
            quot.append(coeffs[i] + rem)
        remainder = quot.pop()
        print("Poly^" + str(len(coeffs) - 2) + "=", quot)
        print("Rmd. (+R/(x+A))=" + str(remainder))
    elif sel == "2":
        print("P(x)=P/A")
        p = list(map(float, input("P COEFF (csv)=").split(",")))
        a = list(map(float, input("A COEFF (csv)=").split(",")))
        a_n, p_n = len(a) - 1, len(p) - 1
        if not (p_n >= a_n > 0):
            print("Requirement failed: P^n>=A^n>0")
            return
        quotient = []
        remainder = p[:]
        for i in range(p_n - a_n + 1):
            lead_coeff = remainder[i] / a[0]
            quotient.append(lead_coeff)
            for j in range(len(a)):
                remainder[i + j] -= lead_coeff * a[j]
        remainder = [r for r in remainder if not abs(r) < 0.01]
        print("Poly^" + str(p_n - a_n) + ".=" + str(quotient))
        print("Rmd^" + str(len(remainder) - 1) + " (+R/A)=" + str(remainder if remainder else 0))

main()