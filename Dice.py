

import random

loop_control = "Yes"

Min_num = int(raw_input("Enter the min number on the dice: "))
Max_num = int(raw_input("Enter the Max number on the dice: "))

def print_rand():
	return random.randrange(Min_num, Max_num)

while loop_control == "Yes":
	print print_rand()
	loop_control = raw_input("Do you want to continue? Yes or No: ")
	
	


	

