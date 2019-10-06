# library imports
import os
import string
from difflib import SequenceMatcher

# build command
# pyinstaller -F -i (iconfile) (pythonfile)

# helper functions

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def calculate_similarity(response, solution):
	similarity = similar(response,solution)
	if similarity < 0.25:
		print("You're pretty far off")
	if similarity > 0.25 and similarity < 0.50:
		print("You got some things right")
	if similarity > 0.50 and similarity < 0.75:
		print("You got more than half right")
	if similarity > 0.75 and similarity <0.90:
		print("You are very close")
	if similarity > 0.90:
		print("You are so close you can smell the answer")

def computer_solver(solution):
	possible_characters_list = list(string.printable)
	computer_solution = ""
	for word in solution.split():
		for c in word:
			if c in possible_characters_list:
				computer_solution+=c
				print("Computer found: "+c)
				print("Solution so far: "+computer_solution)
				if computer_solution == solution:
					print("Computer found the word: "+ solution)
					return computer_solution
			else:
				print("Unknown characters have been used")
				return False

# defining variables
solution_found = False
computer_done = False
exit_responses = ["yes","y"]

# getting 1st player input
solution = input("Enter a string: ")
tip = input("Enter a tip: ")

# clearing screen
os.system('cls')

# getting word length and number of words
words_len = len(solution.replace(" ",""))
words = len(solution.split()) 

# let player 2 start guessing correct answers
while solution_found != True:
	print("The string is "+str(words_len)+" letters long and contains "+str(words)+" words.")
	print("Tip: "+tip.capitalize())
	response = input("Your answer is: ")
	if response.replace(" ","") == solution.replace(" ",""):
		print ("Congrats, you found the string !")
		solution_found = True
		input("Press any key to exit.")
	else:
		print ("Wrong !")
		calculate_similarity(response,solution)

		exit = input("Give up and let the computer solve it ? (Answer Yes or Y) - Press enter to try again ! \n")
		if exit.lower() in exit_responses:
			print("You gave up.")
			print("Computer is solving it...")
			computer_solution = computer_solver(solution)
			if computer_solution == solution:
				computer_done = True

		if computer_done:
			print("The string was: "+computer_solution)
			solution_found = True;
			input("Press any key to exit.")