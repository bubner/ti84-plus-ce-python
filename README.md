# ti84-plus-ce-python

A small collection of Python programs and files to run/stored on the TI-84 Plus CE Python graphing calculator.

To install, drag and drop the desired Python scripts onto the calculator using the TI Connect CE software.

## Programs

### MATHF
A collection of general math functions.

To use, run the program and select the desired function from the *vars* menu.

| Function | Description |
| --- | --- |
| `factors(n)` | Returns a list of factors of `n`. |
| `fib(n)` | Returns the Fibonacci sequence up to `n`. |
| `pascal_row(n)` | Returns the `n`th row of Pascal's triangle. |
| `pascal(n)` | Returns Pascal's triangle up to `n` rows. |
| `binomial_expansion(n)` | Returns the symbolic binomial expansion of `(a + b)^n`. |
| `solve_quadratic(a, b, c)` | Returns the real or complex solutions to the quadratic equation `ax^2 + bx + c = 0`. |
| `fraction(n, d)` | Returns the fraction `n/d` in simplest form. |
| `radical(a, d)` | Returns the simplest form of a radical expression `sqrt(a)/d`. |
| `dot3(a1, a2, a3, b1, b2, b3)` | Computes the dot product of 3D vectors `(a1, a2, a3)` and `(b1, b2, b3)`. |
| `cross3(a1, a2, a3, b1, b2, b3)` | Computes the cross product vector of 3D vectors `(a1, a2, a3)` and `(b1, b2, b3)`. |
| `hypot(a, b, c, ...)` | Computes the Euclidean norm of n-dimensional coordinates (`sqrt(a^2+b^2+c^2+...)`). |

### POLYDIV
Performs synthetic or long polynomial division.

To use, run the program and select the desired division method with *1* or *2*.
Enter the coefficients (including the constant term) of the dividend and divisor polynomials when prompted.

### TRIANGLE
Solves triangle lengths and angles with the cosine and sine rules.

To use, input the known properties of the triangle when prompted. The program will return the possible solutions.

### TRIGREF
Collection of trigonometric identities in comments.

To use, open the program editor and view the comments for the desired identity.

### CALCREF
Collection of common differentiation and integration rules in comments.

To use, open the program editor and view the comments for the desired rule.

### UNITCIRC
Unit circle of length 1 with display and angle/position lookup.

To use, run the program and cycle through the angles with the *left (<)* and *right (>)* keys. The program will display the corresponding angle and position.
You can also use the number buttons *1*, *2*, *3*, *4*, *6*, *7*, *8*, *9* to "jump" to a quadrant quickly.
To exit, use *2nd* + *quit* or *clear*.
