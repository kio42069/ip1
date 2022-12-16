cost = int(input("Enter cost of laptop: "))                 #Input cost for laptop required
allowance = int(input("Enter allowance: "))                 #Example is 20000
saving_fraction = float(input("Enter saving fraction: "))   #Example is 0.1
rate = float(input("Enter rate of interest: "))             #Example is 0.5%
savings = 0
months = 0
while cost > savings:
	months += 1                                             #Increasing month by one and total savings
	savings += allowance * saving_fraction                  #every time if savings < cost of laptop
	savings += savings * rate / 100                         #And breaking out of loop when laptop can be afforded
print(f"You need to wait for {months} months and amount of savings left at the end is {savings-cost}")
