# https://en.wikipedia.org/wiki/List_of_trigonometric_identities
def main():
    print(
        "1. COMMON\n2. REFLECTIONS\n3. PERIODIC\n4. ANGLE SUM\n5. MULTI-ANGLE\n6. HALF-ANGLE\n7. POWER REDUCTION\n8. PROD TO SUM"
    )
    sel = input("CHOOSE CATEGORY: ")
    if sel == "1":
        print(
            "sin²(x)+cos²(x)=1\n1+cot²(x)=csc²(x)\n1+tan²(x)=sec²(x)\nsec²(x)+csc²(x)=sec²(x)csc²(x)\ncsc(x)=1/sin(x)\nsec(x)=1/cos(x)\ncot(x)=1/tan(x)"
        )
    elif sel == "2":
        print(
            "sin(-x)=-sin(x)\ncos(-x)=cos(x)\ntan(-x)=-tan(x)\ncsc(-x)=-csc(x)\nsec(-x)=sec(x)\ncot(-x)=-cot(x)\nsin(pi/2-x)=cos(x)\ncos(pi/2-x)=sin(x)\ntan(pi/2-x)=cot(x)\ncsc(pi/2-x)=sec(x)\nsec(pi/2-x)=csc(x)\ncot(pi/2-x)=tan(x)\nsin(pi-x)=sin(x)\ncos(pi-x)=-cos(x)\ntan(pi-x)=-tan(x)\ncsc(pi-x)=csc(x)\nsec(pi-x)=-sec(x)\ncot(pi-x)=-cot(x)\nsin(3pi/2-x)=-cos(x)\ncos(3pi/2-x)=-sin(x)\ntan(3pi/2-x)=cot(x)\ncsc(3pi/2-x)=-sec(x)\nsec(3pi/2-x)=-csc(x)\ncot(3pi/2-x)=tan(x)"
        )
    elif sel == "3":
        print(
            "f(x+2pik)=f(x), tan&cot->2k\nsin(x±pi/2)=±cos(x)\ncos(x±pi/2)=±°sin(x)\ncsc(x±pi/2)=±sec(x)\nsec(x±pi/2)=±°csc(x)\ntan(x±pi/4)=(tan(x)±1)/(1±°tan(x))\ncot(x±pi/4)=(cot(x)±°1)/(1±cot(x))\nsin(x+pi)=-sin(x)\ncos(x+pi)=-cos(x)\ncsc(x+pi)=-csc(x)\nsec(x+pi)=-sec(x)\ntan(x+pi)=tan(x)\ncot(x+pi)=cot(x)"
        )
    elif sel == "4":
        print(
            "sin(A±B)=sin(A)cos(B)±cos(A)sin(B)\ncos(A±B)=cos(A)cos(B)±°sin(A)sin(B)\ntan(A±B)=(tan(A)±tan(B))/(1±°tan(A)tan(B))\ncsc(A±B)=(sec(A)sec(B)csc(A)csc(B))/(sec(A)csc(B)±csc(A)sec(B))\nsec(A±B)=(sec(A)sec(B)csc(A)csc(B))/(csc(A)csc(B)±°sec(A)sec(B))\ncot(A±B)=(cot(A)cot(B)±°1)/(cot(B)±cot(A))\narcsin(x)±arcsin(y)=arcsin(xsqrt(1-y²)±ysqrt(1-x²))\narccos(x)±arccos(y)=arccos(xy±°sqrt((1-x²)(1-y²)))\narctan(x)±arctan(y)=arctan((x±y)/(1±°xy))\narccot(x)±arccot(y)=arccot((xy±1)/(y±x))"
        )
    elif sel == "5":
        print(
            "cos(nx)+isin(nx)=(cos(x)+isin(x))^n\nsin(2x)=2sin(x)cos(x)=(sin(x)+cos(x))²-1=(2tan(x))/(1+tan²(x))\ncos(2x)=cos²(x)-sin²(x)=2cos²(x)-1=1-2sin²(x)=(1-tan²(x))/(1+tan²(x))\ntan(2x)=(2tan(x))/(1-tan²(x))\ncot(2x)=(cot²(x)-1)/(2cot(x))=(1-tan²(x))/(2tan(x))\nsec(2x)=(sec²(x))/(2-sec²(x))=(1+tan²(x))/(1-tan²(x))\ncsc(2x)=(sec(x)csc(x))/2=(1+tan²(x))/(2tan(x))\nsin(3x)=3sin(x)-4sin³(x)=4sin(x)sin(pi/3-x)sin(pi/3+x)\ncos(3x)=4cos³(x)-3cos(x)=4cos(x)cos(pi/3-x)cos(pi/3+x)\ntan(3x)=(3tan(x)-tan³(x))/(1-3tan²(x))=tan(x)tan(pi/3-x)tan(pi/3+x)\ncot(3x)=(3cot(x)-cot³(x))/(1-3cot²(x))\nsec(3x)=sec³(x)/(4-3sec²(x))\ncsc(3x)=csc³(x)/(3csc²(x)-4)"
        )
    elif sel == "6":
        print(
            "sin(x/2)=sgn(sin(x/2))sqrt((1-cos(x))/2)\ncos(x/2)=sgn(cos(x/2))sqrt((1+cos(x))/2)\ntan(x/2)=(1-cos(x))/sin(x)=sin(x)/(1+cos(x))=csc(x)-cot(x)=tan(x)/(1+sec(x))\ntan(x/2)=sgn(sin(x))sqrt((1-cos(x))/(1+cos(x)))=(-1+sgn(cos(x))sqrt(1+tan²(x)))/tan(x)\ncot(x/2)=(1+cos(x))/sin(x)=sin(x)/(1-cos(x))=csc(x)+cot(x)=sgn(sin(x))sqrt((1+cos(x))/(1-cos(x)))\nsec(x/2)=sgn(cos(x/2))sqrt(2/(1+cos(x)))\ncsc(x/2)=sgn(sin(x/2))sqrt(2/(1-cos(x)))\ntan((a±x)/2)=(sin(a)±sin(x))/(cos(a)+cos(x))\ntan(x/2+pi/4)=sec(x)+tan(x)\nsqrt((1-sin(x))/(1+sin(x)))=|(1-tan(x/2))|/|(1+tan(x/2))|"
        )
    elif sel == "7":
        print(
            "sin²(x)=(1-cos(2x))/2\ncos²(x)=(1+cos(2x))/2\nsin²(x)cos²(x)=(1-cos(4x))/8\nsin³(x)=(3sin(x)-sin(3x))/4\ncos³(x)=(3cos(x)+cos(3x))/4\nsin³(x)cos³(x)=(3sin(2x)-sin(6x))/32\nsin^4(x)=(3-4cos(2x)+cos(4x))/8\ncos^4(x)=(3+4cos(2x)+cos(4x))/8\nsin^4(x)cos^4(x)=(3-4cos(4x)+cos(8x))/128\nsin^5(x)=(10sin(x)-5sin(3x)+sin(5x))/16\ncos^5(x)=(10cos(x)+5cos(3x)+cos(5x))/16\nsin^5(x)cos^5(x)=(10sin(2x)-5sin(6x)+sin(10x))/512"
        )
    elif sel == "8":
        print(
            "cos(A)*cos(B)=(1/2)*(cos(A-B)+cos(A+B))\nsin(A)*sin(B)=(1/2)*(cos(A-B)-cos(A+B))\nsin(A)*cos(B)=(1/2)*(sin(A+B)+sin(A-B))\ncos(A)*sin(B)=(1/2)*(sin(A+B)-sin(A-B))\ntan(A)*tan(B)=(cos(A-B)-cos(A+B))/(cos(A-B)+cos(A+B))\ntan(A)*cot(B)=(sin(A+B)+sin(A-B))/(sin(A+B)-sin(A-B))\nsin(A)±sin(B)=2sin((A±B)/2)cos((A∓B)/2)\ncos(A)+cos(B)=2cos((A+B)/2)cos((A-B)/2)\ncos(A)-cos(B)=-2sin((A+B)/2)sin((A-B)/2)\ntan(A)±tan(B)=sin(A±B)/(cos(A)*cos(B))"
        )


main()
