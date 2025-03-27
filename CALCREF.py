# STANDARD DIFF COMPOSITION
"""
f'(x)=lim_h->0 (f(x+h)-f(x))/h
d/dx f(x)g(x)=f(x)g'(x)+g(x)f'(x)
d/dx f(x)/g(x)=(g(x)f'(x)-f(x)g'(x))/(g(x))²
d/dx f(g(x))=f'(g(x))g'(x)
"""
# CORE DIFF RULES
"""
d/dx c=0
d/dx x^n=nx^(n-1)
d/dx a^x=ln(a)a^x,a>0
d/dx ln(x)=1/x,x>0
d/dx log_a(x)=1/(xln(a)),x>0,a>0
d/dx c*f(x)=c*d/dx f(x)
d/dx 1/x=-1/x²
d/dx sqrt(x)=1/(2sqrt(x))
"""
# TRIG DIFF
"""
d/dx sin(x)=cos(x)
d/dx cos(x)=-sin(x)
d/dx tan(x)=sec²(x)=1/cos²(x)=1+tan²(x)
d/dx arcsin(x)=1/sqrt(1-x²),-1<x<1
d/dx arccos(x)=-1/sqrt(1-x²),-1<x<1
d/dx arctan(x)=1/(1+x²)
d/dx csc(x)=-csc(x)cot(x)
d/dx sec(x)=sec(x)tan(x)
d/dx cot(x)=-csc²(x)
d/dx arccsc(x)=-1/(x*sqrt(x²-1))
d/dx arcsec(x)=1/(x*sqrt(x²-1))
d/dx arccot(x)=1/(1+x²)
"""
# CORE INT RULES
"""
int^a_b f'(x)dx=f(a)-f(b)
int x^n dx=1/(n+1) x^(n+1) +C,n!=1
int 1/x dx=ln|x|+C
int a^x dx=a^x/ln(a)+C
int |x| dx=1/2*x*|x|+C
int c dx=cx+C
"""
# TRIG INT
"""
int sin(x) dx=-cos(x)+C
int cos(x) dx=sin(x)+C
int tan(x) dx=-ln|cos(x)|+C=ln|sec(x)|+C
int sec(x) dx=ln|sec(x)+tan(x)|+C
int sec²(x) dx=tan(x)+C
int sec(x)tan(x) dx=sec(x)+C
int cot(x) dx=ln|sin(x)|+C
int csc(x) dx=-ln|csc(x)+cot(x)|+C
int csc²(x) dx=-cot(x)+C
int csc(x)cot(x) dx=-csc(x)+C
int 1/(a²+x²) dx=1/a arctan(x/a) +C
int 1/sqrt(a²-x²) dx=arcsin(x/a)+C
int 1/(x*sqrt(x²-a²)) dx=1/a arcsec(|x|/a) +C
"""