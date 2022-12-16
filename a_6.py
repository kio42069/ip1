n = int(input("Enter value: "))
for i in range(n-1,-1,-1):
    print("*"*(n-i)+" "*2*i+"*"*(n-i))
	#Printing the pattern, using a loop to control number of spaces and number of stars
