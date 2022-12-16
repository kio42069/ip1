a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))
d = float(input("Enter d : "))

#if the powers of e are the same, then the equations would intersect too:
#so we are just comparing for the powers of e to make the compilation faster

def demand(p):                                            #Demand function
    return (a - b * p)
def supply(p):                                            #Supply function
    return (c + d * p)

x = None       #A flag to check if output has been sent or not
m = int(input("Enter starting value for checking: "))
n = int(input("Enter ending value for checking: "))
try:
	i = m
	while i <= n:
		if abs(demand(i)-supply(i)) <= 0.001:             #Checking difference between outputs of the two
			x = i                                         #functions, since equality for floats doesn't
			break                                         #hold in Python.
		i += 0.005
except ValueError:
    print("Please enter valid range of values.")          #Error handling
    x = "placeholder"
except OverflowError:
    print("Overflowed. Please try a smaller range of values")
    x = "placeholder"

if x == None:
    print("Equillibrium not found in the given range.")
elif type(x) == float:
    print(f"Equillibrium found at value : {x}")
