# Import local and external libraries
import os

class QuizBrain:
    
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        
        
    def still_has_questions(self):
        
        # Get the total number of questions
        self.total_number_of_questions = len(self.question_list)
        
        # Check if the user is at the last question
        if self.total_number_of_questions <= self.question_number:
            return False
        else:
            return True        
        
    def next_question(self):
        
        ask_the_question = self.question_list[self.question_number]
        
        # Set the first question to 1
        self.question_number += 1
        
        user_answer = input(f"Q.{self.question_number} {ask_the_question.text} True/False?: ")
        
        self.check_answer(user_answer, ask_the_question.answer )    
    

    def check_answer(self, user_answer, question_answer):
        
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("You got it right!")
            
        else:
            print("That's wrong.")
            
        print(f"The correct answer is {question_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
        
        
    def print_endscreen(self):
        # Clear the screen
        os.system('cls||clear')   
        
        # Print final score
        print("That's it. You've completed the quiz.")
        print(f"Your final score was {self.score}/{self.question_number}")
        