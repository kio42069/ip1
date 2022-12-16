M = int(input("Enter the value of M: "))

#Eq 1 ==> y = (400 - 8x) / 2
#Eq 2 ==> y = 120 - 2x

#Optimise this before M : 90x + 25y
#Optimise this after M : 100x + 30y

cornerPoints = []

def f1(x):                      #Equation 1
	return (400 - 8*x) // 2
def f2(x):                      #Equation 2
	return (120 - 2*x)
def f1inv(y):                   #Equation 1's inverse
	return (400 - 2 * y) // 8
def f2inv(y):                   #Equation 2's inverse
	return (120 - y) // 2


for x in range(min(f1inv(0),f2inv(0))+1):      #Looping x from 0 to the minimum of where the two lines intersect x axis

	y1 = f1(x)
	y2 = f2(x)

	if x == 0 or min(f1(x),f2(x)) == 0 or y1 == y2:     #If lines intersect each other or the axes, we get a corner point


#Various conditions giving different profits based on user input of M
		if x > M and min(f1(x),f2(x)) > M:
			temp_prof = 100 * (x-M) + 90 * M + 30 * (min(f1(x),f2(x))-M) + 25 * M
		elif x <= M and min(f1(x),f2(x)) > M:
			temp_prof = 90 * x + 30 * (min(f1(x),f2(x)) - M) + 25 * M
		elif x > M and min(f1(x),f2(x)) <= M:
			temp_prof = 100 * (x-M) + 90 * M + 25 * min(f1(x),f2(x))
		else:
			temp_prof = 90 * x + 25 * min(f1(x),f2(x))


	#Storing the profit and x,y coordinates of corner point
		cornerPoints.append([x,min(f1(x),f2(x)),temp_prof])

max_profit = 0
max_tables = 0
max_chairs = 0
for i in range(len(cornerPoints)):        #checking for max profit
	if max_profit < cornerPoints[i][2]:
		max_tables = cornerPoints[i][0]
		max_chairs = cornerPoints[i][1]
		max_profit = cornerPoints[i][2]

print(f"Number of chairs : {max_chairs}")
print(f"Number of tables : {max_tables}")
print(f"Maximum profit : {max_profit}")
