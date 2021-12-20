

import random
import operator
from operator import add, sub, mul, truediv

vals = {'1' : "Addition", "2": "Subtraction", "3": "Multiplication", "4": "Divsion"}
opvals = {'1' : "+", "2": "-", "3": "x", "4": "/"}
ops = {'1' : add, "2": sub, "3": mul, "4": truediv}
score_overall  = {'1' : 0, "2": 0, "3": 0, "4": 0}


class Driver:

	def __init__(self, name):
		self.name = name
		self.operation = None
	#	self.vals = ['1', "2", "3", "4"]
	#	self.dict = {'1' : "Addition", "2": "Subtraction", "3": "Multiplication", "4": "Divsion"}
		self.valid = False
		self.reply = False
		self.rounds =1
		self.detailed_rounds = {'1' : 0, "2": 0, "3": 0, "4": 0}


	
	def drive(self):

		operation = self.choose_operation()
		q = Questions(self.name , operation)
		s = Score(self.name)
		for i in range(10):
			val = q.random_questions(operation)
			s.score_keeping(val)
		s.print_round_score()
		self.replay()

	def choose_operation(self):
		self.valid = False
		while self.valid == False:
			operation = input("Which operation would you like to practice? Press 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division: ")
			if operation in vals.keys():
				self.valid = True
				print("You selected: " + vals[operation] + ". It's time to practice!")
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
		self.reply = False
		questions_wrong_sum = 0
		while self.reply == False:
			repl = input("Do you want to replay? Type 'yes' to continue or 'no' to exit the game    ")
			if repl in ["yes", "no"]:
				self.reply = True
				if repl == "yes":
					self.rounds +=1
					self.drive()
				else:
					print('You played ' + str(self.rounds) + " rounds!")
					print('Here is a breakdown of your score')

					for item in score_overall:
						questions_wrong_sum += score_overall[item]
						print("For " + vals[item] + ", you missed " + str(score_overall[item]) + " questions out of " + str(self.detailed_rounds[item] * 10))
					


					print("In total, you got " + str(questions_wrong_sum) + " out of " + str(self.rounds * 10)+ " total questions")
					return
			else:
				print("You didn't select a valid option. Try Again!")

	



class Questions:
	def __init__(self, name, operation):
	#	self.ops = {'1' : add, "2": sub, "3": mul, "4": truediv}
	#	self.opvals = {'1' : "+", "2": "-", "3": "x", "4": "/"}
		self.operation = operation

	def random_questions(self, operation ):
		v = False;
		input_int = False
		while v == False:

			one = random.randint(5, 10)
			two = random.randint(1, one-1)

			
			if (operation == "4" and one//two == one/two) or operation in ["1", "2", "3"]:
				v = True
				while input_int == False:
					prompt = input("What is the result of " + str(one) + " " + str(opvals[operation]) + " " + str(two) + "?                    ")
				
					if prompt.isnumeric():
						input_int = True
						if int(prompt) == ops[operation](one, two):
							return True
						else:
							return [False, one, two, operation]
					else:
						print("You did not enter a number. Try Again")



class Score:
	def __init__(self, name):
		self.name = name
		self.score = 0
		self.questions_wrong_list = []
		self.questions_wrong_answers_list = []

	def score_keeping(self, answer):
		if answer == True:
			self.score +=1
		else:
			self.print_questions_wrong(answer)

	def print_round_score(self):
		print("Your score was " + str(self.score) + " out of 10!")
		print("The Questions you missed with the correct answers were: ")

		score_overall[operation] += len(self.questions_wrong_list)
		
		for i in range(len(self.questions_wrong_list)):
			print(str(self.questions_wrong_list[i]) + " = " + str(self.questions_wrong_answers_list[i]))


	def print_questions_wrong(self, answer):
		one = answer[1]
		two = answer[2]
		operation = answer[3]

		self.questions_wrong_list.append(str(one) + " " + str(opvals[operation]) + " " + str(two))
		self.questions_wrong_answers_list.append( ops[operation](one, two))
		
		




if __name__ == "__main__":
	d = Driver("varsha")
	d.drive()



