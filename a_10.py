#Taking inputs of coeffecients for the cubic polynomial
#According to example given in question
# a = 1 , b = -10.5 , c = 34.5 , d = -35

a = float(input("Enter coefficient of x^3: "))
b = float(input("Enter coefficient of x^2: "))
c = float(input("Enter coefficiet of x: "))
d = float(input("Enter constant term: "))

x0 = float(input("Enter your guess: "))
x1 = 0
temp = x0
a_dash = a*3
b_dash = b*2
c_dash = c


#Constructing the f(x) polynomial using a,b,c and d
def func(x):
    return a*x**3 + b*x**2 + c*x + d

#Constructing the derivative polyomial f'(x) using pre-requisite calculus knowledge
def func_dash(x):
    return a_dash*x**2 + b_dash*x + c

#Newton-Raphson algorithm
def check(x0,x1):
	for i in range(100):
	    x1 = x0 - (func(x0)/func_dash(x0))
	    x0 = x1
	return x1


#If slope converges nearly to 0, given guess is a root
print(f"Nearest root to the given number is : {round(check(x0,x1),2)}")


# If you need to check if a given input is a root or not, uncomment the below lines of code

# =============================================================================
# if func(x0) == 0 or abs(check(x0,x1)-temp) <= 0.1:
#     print(f"It is highly probable that {temp} is a root of the function {a}x^3+{b}x^2+{c}x+d.")
# else:
#     print(f"It is impossible that {temp} is a root of the function {a}x^3+{b}x^2+{c}x+{d}")
# =============================================================================
