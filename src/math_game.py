
import random
import operator
from operator import add, sub, mul, truediv


"""global variables to be accessed by all classes about the operations"""
operation_words = {'1' : "Addition", "2": "Subtraction", "3": "Multiplication", "4": "Divsion"}
operation_symbols = {'1' : "+", "2": "-", "3": "x", "4": "/"}
operation_function = {'1' : add, "2": sub, "3": mul, "4": truediv}
score_overall  = {'1' : 0, "2": 0, "3": 0, "4": 0}

class Driver:
	"""Performs play options of the game"""
	def __init__(self):
		self.operation = None
		self.valid = False
		self.reply = False
		self.rounds = 1
		self.detailed_rounds = {'1' : 0, "2": 0, "3": 0, "4": 0}

	def drive(self):

		operation = self.choose_operation()
		q = Questions(operation)
		s = Score()
		for i in range(10):
			val = q.random_questions(operation, i+1)
			s.score_keeping(val)
		s.print_round_score()
		self.replay()

	def choose_operation(self):
		"""user inputs which operation they want to practice"""

		self.valid = False
		while self.valid == False:
			operation = input("Which operation would you like to practice? Press 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division: ")
			if operation in operation_words.keys():
				self.valid = True
				print("You selected: " + operation_words[operation] + ". It's time to practice!")
				self.detailed_rounds[operation] +=1


				return operation
	
			else:
				print("You didn't select a valid option. Try Again!")
			'''
			if operation in self.vals:
				self.valid = True
				op_val = ""
				if operation == "1":
					op_val = "Addition"
				if operation == "2" :
					op_val = "Subtraction"
				if operation == "3":
					op_val = "Multiplication"
				if operation == "4":
					op_val = "Division"
				print("You selected: " + op_val + ". It's time to practice!")
			else:
				print("You didn't select a valid option. Try Again!")
					'''
	def replay(self):

		"""if user wants to replay their game or if not, displays the final score"""

		self.reply = False
		
		while self.reply == False:
			repl = input("Do you want to replay? Type 'yes' to continue or 'no' to exit the game    ")
			if repl in ["yes", "no"]:
				self.reply = True
				if repl == "yes":
					self.rounds +=1
					self.drive()
				else:
					self.end_game(self.rounds, )
					
			else:
				print("You didn't select a valid option. Try Again!")

	
	def end_game(self, rounds):
		questions_wrong_sum = 0
		print('You played ' + str(rounds) + " rounds!")
		print('Here is a breakdown of your score')

		for item in score_overall:
			questions_wrong_sum += score_overall[item]
			print("For " + operation_words[item] + ", you missed " + str(score_overall[item]) + " questions out of " + str(self.detailed_rounds[item] * 10))
		
		print("In total, you got " + str(questions_wrong_sum) + " out of " + str(rounds * 10)+ " total questions")
		return



class Questions:

	"""class where the questions are created """

	def __init__(self, operation):
	#	self.ops = {'1' : add, "2": sub, "3": mul, "4": truediv}
	#	self.opvals = {'1' : "+", "2": "-", "3": "x", "4": "/"}
		self.operation = operation

	def random_questions(self, operation, num ):

		"""generates random questions from random numbers """

		v = False;
		input_int = False
		while v == False:

			one = random.randint(5, 20)
			two = random.randint(1, one-1)

			
			if (operation == "4" and one//two == one/two) or operation in ["1", "2", "3"]:
				v = True
				while input_int == False:
					prompt = input(str(num) +  ") What is the result of " + str(one) + " " + str(operation_symbols[operation]) + " " + str(two) + "?                    ")
				
					if prompt.isnumeric():
						input_int = True
						if int(prompt) == operation_function[operation](one, two):
							return True
						else:
							return [False, one, two, operation]
					else:
						print("You did not enter a number. Try Again")



class Score:

	"""score class"""

	def __init__(self):

		self.score = 0
		self.questions_wrong_list = []
		self.questions_wrong_answers_list = []

	def score_keeping(self, answer):
		"""adds up the scores if right"""

		if answer == True:
			self.score +=1
		else:
			self.adds_questions_wrong(answer)

	def print_round_score(self):
		"""prints the wrong questions below the round score"""

		print("Your score was " + str(self.score) + " out of 10!")
		print("The Questions you missed with the correct answers were: ")

		
		
		for i in range(len(self.questions_wrong_list)):
			print(str(self.questions_wrong_list[i]) + " = " + str(self.questions_wrong_answers_list[i]))


	def adds_questions_wrong(self, answer):
		"""adds wrong questions into a list """


		one = answer[1]
		two = answer[2]
		operation = answer[3]

		self.questions_wrong_list.append(str(one) + " " + str(operation_symbols[operation]) + " " + str(two))
		self.questions_wrong_answers_list.append( int(operation_function[operation](one, two)))
		
		score_overall[operation] += 1




if __name__ == "__main__":
	d = Driver()
	d.drive()



