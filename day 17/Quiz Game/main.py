#!/usr/bin/env python

# Import local and external libraries
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Credits
__author__ = "Thijs Moens"
__copyright__ = "Copyright 2025, Thijs Moens"
__credits__ = ["Thijs Moens"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Thijs Moens"
__email__ = "thijsmoens@email.com"
__status__ = "Production"

# Create an empty list for all the questions and answers
question_bank = []

# Iterate over the data
for question in question_data:
    
    # Assign dict to new variables
    question_text = question['question']
    question_answer = question['correct_answer']
    
    # Instanciate object
    question_and_answer = Question(question_text, question_answer)
    
    # Assign to the empty list
    question_bank.append(question_and_answer)
    
    
# Initiate a new quiz
quiz = QuizBrain(question_bank)

# Show questions as long as there is one
while quiz.still_has_questions():
    
    quiz.next_question()
    

quiz.print_endscreen()