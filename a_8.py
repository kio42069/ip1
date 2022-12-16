main_pop_list = eval(input("Enter population as a list: "))
years = int(input("Enter number of years to calculate total population after: "))
rate = []
x = 2.5
cur_pop = 0
count = 1
for i in range(len(main_pop_list)):             # Creating a list to contain the rate of population increments
    rate.append(x)
    x = round(x - 0.4,1)

def copies(a,b):                                # function to copy elements from one list to another, since
    for i in a:                                 # list.copy() isn't allowed
        b += [i]

def totalPopCalc(pop_list,r,time):              # function to calculate total population
    for j in range(time):                       # given the current population, rates and
        for i in range(len(pop_list)):          # number of years as parameters
            pop_list[i] += pop_list[i]*(r[i]/100)
        for i in range(len(r)):
            r[i] = r[i] - 0.1
    return pop_list

def maxYears(pop_list,r):                      # function to calculate the peak population
    global count
    previous = sum(totalPopCalc(pop_list,r,1))
    while True:
        new = sum(totalPopCalc(pop_list,r,1))
        if previous >= new:                    # uses the last year's population and compares it wth current year's
            return previous,count
        else:
            count += 1
            previous = new

temp1 = []
temp2 = []

copies(main_pop_list,temp1)
copies(rate,temp2)
t = maxYears(main_pop_list,rate)
main_pop_list = temp1.copy()
rate = temp2.copy()
print(f"Current world population is : {int(sum(totalPopCalc(main_pop_list,rate,years)))} million")
print(f"Maximum population is : {int(t[0])} million")
print(f"Years required to reach maximum population is : {int(t[1])} years")
