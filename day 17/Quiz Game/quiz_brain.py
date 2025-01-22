# TODO: Asking the questions

# TODO: Check if answer was correct

# TODO: Check if we are at the end of the quiz



class QuizBrain:
    
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        
        
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
        
        return user_answer
        
        
        