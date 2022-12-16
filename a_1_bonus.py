a = str (int(input("Enter number: ")))

def ones(n):               #Function which returns digit for ones place
    if n == '1':
        return "one"
    elif n == '2':
        return "two"
    elif n == '3':
        return "three"
    elif n == '4':
        return "four"
    elif n == '5':
        return "five"
    elif n == '6':
        return "six"
    elif n == '7':
        return "seven"
    elif n == '8':
        return "eight"
    elif n == '9':
        return "nine"
    elif n == '0':
        return ""

def tens(n):               #Function which return digit for tens place
    if n == '2':
        return "twenty"
    elif n == '3':
        return "thirty"
    elif n == '4':
        return "forty"
    elif n == '5':
        return "fifty"
    elif n == '6':
        return "sixty"
    elif n == '7':
        return "seventy"
    elif n == '8':
        return "eighty"
    elif n == '9':
        return "ninety"
    else:
        return None

def special_10(n):            #Function to return answer for special numbers from 11-19
    if n == '10':
        return "ten"
    elif n == '11':
        return "eleven"
    elif n == '12':
        return "twelve"
    elif n == '13':
        return "thirteen"
    elif n == '14':
        return "fourteen"
    elif n == '15':
        return "fifteen"
    elif n == '16':
        return "sixteen"
    elif n == '17':
        return "seventeen"
    elif n == '18':
        return "eighteen"
    elif n == '19':
        return "nineteen"

def regular(n):
    if n == '2':
        return "twenty"
    elif n == '3':
        return "thirty"
    elif n == '4':
        return "forty"
    elif n == '5':
        return "fifty"
    elif n == '6':
        return "sixty"
    elif n == '7':
        return "seventy"
    elif n == '8':
        return "eighty"
    elif n == '9':
        return "ninety"
    else:
        return ""

#a = 23,45,46,234
if len(a) == 1:
	print(ones(a))

elif len(a) == 2:
	if a[0] == '1':
		print(special_10(a))
	else:
		print(tens(a[0])+" "+ones(a[1]))

elif len(a) == 3:
	print(ones(a[0])+" hundred",end = " ")
	if a[1] == '1':
		print(special_10(a[1:]))
	else:
		if regular(a[1]) != '':
			print(regular(a[1])+" "+ones(a[2]))
		else:
			print(ones(a[2]))

elif len(a) == 4:
	print(ones(a[0])+" thousand",end = " ")
	if ones(a[1]) != "":
		print(ones(a[1])+" hundred",end = " ")
		if a[2] == '1':
			print(special_10(a[2:]))
		else:
			if regular(a[2]) != '':
				print(regular(a[2])+" "+ones(a[3]))
			else:
				print(ones(a[3]))
	else:
		if a[2] == '1':
			print(special_10(a[2:]))
		else:
			if regular(a[2]) != '':
				print(regular(a[2])+" "+ones(a[3]))
			else:
				print(ones(a[3]))

elif len(a) == 5:
	if a[0] == '1':
		print(special_10(a[:2])+" thousand", end = " ")
	else:
		print(tens(a[0])+" "+ones(a[1])+" thousand", end = " ")
	if ones(a[2]) != "":
		print(ones(a[2])+" hundred",end = " ")
		if a[3] == '1':
			print(special_10(a[3:]))
		else:
			if regular(a[3]) != '':
				print(regular(a[3])+" "+ones(a[4]))
			else:
				print(ones(a[4]))
	else:
		if a[3] == '1':
			print(special_10(a[3:]))
		else:
			if regular(a[3]) != '':
				print(regular(a[3])+" "+ones(a[4]))
			else:
				print(ones(a[4]))

elif len(a) == 6:
	print(ones(a[0])+" lakhs", end = " ")
	if a[1] == '1':
		print(special_10(a[1:3])+" thousand", end = " ")
	else:
		print(tens(a[1])+" "+ones(a[2])+" thousand", end = " ")
	if ones(a[3]) != "":
		print(ones(a[3])+" hundred",end = " ")
		if a[4] == '1':
			print(special_10(a[4:]))
		else:
			if regular(a[4]) != '':
				print(regular(a[4])+" "+ones(a[5]))
			else:
				print(ones(a[5]))
	else:
		if a[4] == '1':
			print(special_10(a[4:]))
		else:
			if regular(a[4]) != '':
				print(regular(a[4])+" "+ones(a[5]))
			else:
				print(ones(a[5]))

elif len(a) == 7:
	if a[0] == '1':
		print(special_10(a[:2])+" lakhs", end = " ")
	else:
		print(tens(a[0])+" "+ones(a[1])+" lakhs", end = " ")
	if a[2] == '1':
		print(special_10(a[2:4])+" thousand", end = " ")
	else:
		print(tens(a[2])+" "+ones(a[3])+" thousand", end = " ")
	if ones(a[4]) != "":
		print(ones(a[4])+" hundred",end = " ")
		if a[5] == '1':
			print(special_10(a[5:]))
		else:
			if regular(a[5]) != '':
				print(regular(a[5])+" "+ones(a[6]))
			else:
				print(ones(a[6]))
	else:
		if a[5] == '1':
			print(special_10(a[5:]))
		else:
			if regular(a[5]) != '':
				print(regular(a[5])+" "+ones(a[6]))
			else:
				print(ones(a[6]))

elif len(a) == 8:
	print(ones(a[0])+" crores",end = " ")
	a = a[1:]
	if a[0] == '1':
		print(special_10(a[:2])+" lakhs", end = " ")
	else:
		print(tens(a[0])+" "+ones(a[1])+" lakhs", end = " ")
	if a[2] == '1':
		print(special_10(a[2:4])+" thousand", end = " ")
	else:
		print(tens(a[2])+" "+ones(a[3])+" thousand", end = " ")
	if ones(a[4]) != "":
		print(ones(a[4])+" hundred",end = " ")
		if a[5] == '1':
			print(special_10(a[5:]))
		else:
			if regular(a[5]) != '':
				print(regular(a[5])+" "+ones(a[6]))
			else:
				print(ones(a[6]))
	else:
		if a[5] == '1':
			print(special_10(a[5:]))
		else:
			if regular(a[5]) != '':
				print(regular(a[5])+" "+ones(a[6]))
			else:
				print(ones(a[6]))
