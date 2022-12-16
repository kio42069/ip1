n = int(input("Enter n the number of roots: "))
x0 = int(input("Enter starting range: "))
x1 = int(input("Enter ending range: "))

roots = []

print("Enter coefficients starting form highest power to the constant.")

for i in range(n):
	roots.append(int(input("Enter coefficients: ")))
roots.append(int(input("Enter constant: ")))

def func(x):
	global n
	sums = 0
	for i in range(n,-1,-1):
		sums += roots[n-i]*(x**(i-1))
	return sums

def func_dash(x):
	global n
	sums = 0
	d = roots.copy()
	d.pop()
	for i in range(len(d)):
		d[i] *= n-i
	for i in range(n,0,-1):
		sums += d[n-i]*(x**(i-1))
	return sums

def check(x0,x1):
	for i in range(100):
	    x1 = x0 - (func(x0)/func_dash(x0))
	    x0 = x1
	return x1

root_list = []
for i in range(x0,x1):
	root_list += [check(x0, i)]
root_list = set(root_list)
