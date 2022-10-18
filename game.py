#setup (imports)
import time

#setup (commands)
y_n = ["yes", "no"]
directions = ["left", "right", "forward", "backward", "use"]
items = ["inventory"]
location = ["map"]

#setup (directon vars)
l = 0
r = 0
f = 0
b = 0

#setup (item vars)
k = 0

#credits
print("Copyright © 2021 by KiloBite\n██╗   ██╗      ██████╗ ██████╗  ██████╗\n██║   ██║      ██╔══██╗██╔══██╗██╔════╝ \n██║   ██║█████╗██████╔╝██████╔╝██║  ███╗\n╚██╗ ██╔╝╚════╝██╔══██╗██╔═══╝ ██║   ██║\n ╚████╔╝       ██║  ██║██║     ╚██████╔╝\n  ╚═══╝        ╚═╝  ╚═╝╚═╝      ╚═════╝")

#start
usr = input("What is your name?\n► ")
print("Hello, " + usr + ", you are viewing a preview version, so certain things are subject to change")

#adventure start
response = ""
while response not in y_n:
    response = input("Would you like to start an adventure? (yes/no)\n► ")
    if response == "yes":
        print("\nGreat! Lets get you caught up.\n")
    elif response == "no":
        print("Goodbye, " + usr + ".")
        time.sleep(2)
        quit()
    else: 
        print("I didn't understand that.\n")

#chunk 1
response = ""
print("You are stuck in a small shipping facillity. To the right of you is a key, and behind you is a wall.")
while response not in directions:
    response = input("What would you like to do? (left/right/forward/backward/use)\n► ")
    if response == "left":
        print("\nYou move left.\n")
        l = 1
    elif response == "right":
        print("\nYou move to your right.\n")
        r = 1
    elif response == "forward":
        print("\nYou move forward.\n")
        f = 1
    elif response == "backward":
        print("\nYou cannot move back right now.\n")
        response = ""
    elif response == "use":
    	print("\nNothing to use.\n")
    	response = ""
    else:
        print("\nI didn't understand that.\n")

#chunk 2
response = ""
while response not in directions:
##what happens next
	if l == 1:
		print ("There is a wall to the left of you, behind you, and in front of you.\n")
	if r == 1:
		print("There is a wall behind you and to the right of you. There is also a key below you\n")
	if f == 1:
		print("There is a wall to the left of you, and there is a door in front of you.\n")
	response = input("What would you like to do? (left/right/forward/backward/use)\n► ")
##l variable
	if response == "left" and l == 1:
		print("\nYou cannot move left.\n")
		response = ""
##r variable
	if response == "right" and r == 1:
		print("\nYou cannot move right.\n")
		response = ""
	elif response == "backward" and r == 1:
		print("\nYou cannot move back.\n")
		response = ""
	elif response == "forward" and r == 1:
		print("\nYou move forward.\n")
		f = 1
	elif response == "use" and r == 1:
		print("\nYou pickup a key.\n")
		k = 1
##f variable
	elif response == "left" and f == 1:
		print("\nYou cannot move left.\n")
		response = ""
	elif response == "right" and f == 1:
		print("\nYou move right.\n")
		r = 1
	elif response == "forward" and f == 1:
		print("\nYou may not move forward as there is a door.\n")
		response = ""
	elif response == "backward" and f == 1:
		print("\nYou move backward\n")
		f = 0
	elif response == "use" and f == 1:
		print("\nYou try to open the door. It appears to be locked.")
		response =""
	elif response == "use" and f == 1 and k ==1:
		print("\nYou unlock the door and open it.\n")
##d variable

##bottom of the barrel
	else:
		print("\nI didn't understand that\n")

#chunk 3
response = ""
while response not in directions:
###what happens next
	if r == 1 and k == 1:
		print("There is a wall behind you and to the right of you.\n")
	response = input("What would you like to do? (left/right/forward/backward/use)\n► ")
