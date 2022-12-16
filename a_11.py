
def spinner():
	print("Spinning...")
	print("Spinning...")
	print("Spinning...")
	print(f"Your fidget spinner spun {random.randint(1,100)} times")
	print("Exiting to main menu...")
	print()

def madlibs():
	a = input("Enter an adjective: ")
	b = input("Enter an adejctive: : ")
	c = input("Enter a bird: ")
	d = input("Enter a room in a house: ")
	e = input("Enter a verb in past tense: ")
	f = input("Enter a verb: ")
	g = input("Enter a relative's name: ")
	h = input("Enter a noun: ")
	i = input("Enter a liquid: ")
	j = input("Enter a verb ending in -ing: ")
	k = input("Enter a part of the body(plural): ")
	l = input("Enter a plural noun: ")
	m = input("Enter a verb ending in -ing: ")
	n = input("Enter a noun: ")
	print(f"It was a {a}, cold November day. I woke up to the {b} smell of {c} roasting in the {d} downstairs. I {e} down the stairs to see if I could help {f} the dinner. My mom said, \"See if {g} needs a fresh {h}.\" So I carried a tray of glasses full of {i} into the {j} room. When I got there, I couldn't believe my {k}! There were {l} {m} on the {n}!")
	print("Exiting to main menu...")

def numbergame():
	a = ord(input("Enter any key to continue: "))
	computer = a//10
	tries = 5
	print("You will get 5 tries to guess a number chosen by the computer")
	while True:
		if tries == 0:
			print("Game over")
			break
		tries -= 1
		user = int(input("Enter a number from 1 to 10: "))
		if user == computer:
			print("You won!")
			break
		elif user < computer:
			print(f"Your guess was too low, try again. {tries} tries remaining")
		elif user > computer:
			print(f"Your guess was too high, try again. {tries} tries remaining")
	print("Exiting to main menu...")
	print()

def decision():
	print("Welcome to decision maker! Ever had a situation where needed to choose between two options and wanted to toss a coin but didn't have any? This is for you! Take your time, and press any key when you want to know what your coin says...")
	x = input()
	print("The coin says : Heads") if ord(x) % 2 == 0 else print("The coin says : Tails")
	print("Exiting to main menu is 5 seconds...")
	print()

while True:
	print("Welcome to the ultimate game machine!\nChoose an option\n1. Virtual fidget spinner\n2. Mad Libs game\n3. Number Guesser\n4. Decision maker\nIf you want to quit, enter 0")
	a = int(input())
	if a == 1:
		spinner()
	elif a == 2:
		madlibs()
	elif a == 3:
		numbergame()
	elif a == 4:
		decision()
	elif a == 0:
		print("Hope you had a fun time, and have a good day! Exiting game...")
		print()
	break
