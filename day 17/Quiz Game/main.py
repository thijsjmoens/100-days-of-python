from question_model import Question
from data import question_data



for question, answer in question_data:
    
    question = Question(question["text"], answer["answer"])
    
    print(question)

# Create a question bank with a list of questions and answers
# question_bank = [
#     Question("What is your name?", question_data.get("name")),
#     Question("What is your age?", question_data.get("age")),
# ]