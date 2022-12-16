month_required = int(input("Enter number of months when you want to buy laptop: "))

cost = int(input("Enter cost of laptop: "))                 #Input cost for laptop required
allowance = 20000
saving_fraction = 0.1
rate = 0.5
savings = 0
months = 0
while True:
	months = 0
	while True:
		if savings >= cost:
			break
		months += 1                                             #Increasing month by one and total savings
		savings += allowance * saving_fraction                  #every time if savings < cost of laptop
		savings += savings * rate / 100                         #And breaking out of loop when laptop can be afforded
	if months <= month_required:
		break
	saving_fraction += 0.1
	savings = 0


#print(f"You need to change your savings fraction to {saving_fraction}") if saving_fraction <= 1 else print("Lol ur broke ass can't buy that")

print(f"You need to change your savings fraction to {saving_fraction}") if saving_fraction <= 1 else print(f"You can't buy your laptop of that cost in {month_required} months even if you spend nothing")


