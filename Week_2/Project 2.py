# First install the numpy library by typing "pip install numpy" or "py -m pip install numpy" in your cmd
# The numpy library can solve roots of equations with the .root() attribute / function
# Numpy can tell if an eqn is quadratic or quartic and so on based off the amount of elements in the list you're solving for,
# This is because the minimum amount of variables for all these equations specify the format as in for instance a quadratic eqn having two variables with the coefficient of X² (making 4 variables in total) can most definitely be simplified into one main value with the coefficient of X² putting it back to 3 variables

import numpy

print("You have been requested to develop a program to algorithm and Python code to find the root of a Cubic Equation: Ax³ + Bx² + Cx + D = 0, the roots of a Quartic Equation, and the roots of a quadratic equation. \nShould you choose to accomplish the mission, write a Python program that requests and asks the user what operation to perform.")
print("\nWhich of these operations would you like me to perform Type the number beside it to select? \n1 - Cubic Equation: Ax³ + Bx² + Cx + D = 0 \n2 - Quartic Equation: Ax⁴ + Bx³ + Cx² + Dx + E = 0\n3 - Quadratic Equation: Ax² + Bx + C = 0")

userinput = int(input("Input your value here"))



if userinput == 1:
    cubic_coefficients = []
    cubic_a = float(input("Enter your coefficient of A: "))
    cubic_b = float(input("Enter your coefficient of B: "))
    cubic_c = float(input("Enter your coefficient of C: "))
    cubic_d = float(input("Enter your coefficient of D: "))
    cubic_coefficients.append(cubic_a)
    cubic_coefficients.append(cubic_b)
    cubic_coefficients.append(cubic_c)
    cubic_coefficients.append(cubic_d)

    print("The roots are: ", numpy.roots(cubic_coefficients))
elif userinput == 2:
    quartic_coefficients = []
    quartic_a = float(input("Enter your coefficient of A: "))
    quartic_b = float(input("Enter your coefficient of B: "))
    quartic_c = float(input("Enter your coefficient of C: "))
    quartic_d = float(input("Enter your coefficient of D: "))
    quartic_e = float(input("Enter your coefficient of E: "))
    quartic_coefficients.append(quartic_a)
    quartic_coefficients.append(quartic_b)
    quartic_coefficients.append(quartic_c)
    quartic_coefficients.append(quartic_d)
    quartic_coefficients.append(quartic_e)

    print("The roots are: ", numpy.roots(quartic_coefficients))
elif userinput ==3:
    quadratic_coefficients = []
    quadratic_a = float(input("Enter your coefficient of A: "))
    quadratic_b = float(input("Enter your coefficient of B: "))
    quadratic_c = float(input("Enter your coefficient of C: "))
    quadratic_coefficients.append(quadratic_a)
    quadratic_coefficients.append(quadratic_b)
    quadratic_coefficients.append(quadratic_c)

    print("The roots are: ", numpy.roots(quadratic_coefficients))
else:
    print("Your Input is invalid")