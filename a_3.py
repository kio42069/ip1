x0,y0 = map(int,input("Enter x0 y0 separated with a space: ").split())        #Initial coordinates
vertical = 0
horizontal = 0
total_dist = 0
while True:
	a = int(input("Enter distance: "))
	if a > 0:
		if a <=25:                            #If distances are > 0 then appending them to the variables...
			vertical += a
		elif a <=50:
			vertical -= a
		elif a <= 75:
			horizontal += a
		else:
			horizontal -= a
		total_dist += a
	else:break                                    #else breaking out of infinite loop

answer = (vertical**2 + horizontal**2)**0.5  #Final output using pythagoras theorem

print(f"Final coordinates are : {x0+horizontal},{y0+vertical}\nTotal distance travelled is : {total_dist}\nStraight line distane between the two points is : {answer}")
