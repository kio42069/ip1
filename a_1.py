a = input("Enter number: ")
if len(a) == 1:            #Incase of single digit input converting it for computational purposes
    a = "0"+a              #Example => 8 is converted to 08

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

def special(n):            #Function to return answer for special numbers from 11-19
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

if tens(a[0]) == None:     #If number < 20
    if a[0] != '1':        #If Number is < 10
        print(f"{a[1]} is {ones(a[1])}")
    else:                  #If Number is 10 to 19
        print(f"{a} is {special(a)}")
else:                      #If number >= 20
    if a[1] != 1:
        print(f"{a} is {tens(a[0])} {ones(a[1])}")
