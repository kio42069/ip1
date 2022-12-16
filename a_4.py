from math import log
e = 2.71828
a = int(input("Enter starting time: "))
b = int(input("Enter ending time: "))
integral = 0

def func(i):                                         #The function to be integrated
    a = 2000*(log((140000/(140000-(2100*i))),e))-(9.8*i)
    return a


#for i in range(4*a,4*int((b))):                      #Multiplying start and stop value by 4 since step value required
#    integral += ((func(i)+func(i+0.25))/2)*0.25      #is 0.25 but range can't do that, then diving final integral
								                     #by 4 to reduce integral to correct integral
                             
while a<b:
    integral += (func(a)+func(a+0.25))/2*0.25 
    a += 0.25
print(f"The total distance covered is : {integral}")
