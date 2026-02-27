from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    q_text = item['question']
    q_answer = item['correct_answer']

    quiz = Question(q_text,q_answer)
    question_bank.append(quiz)

new_question = QuizBrain(question_bank)

while new_question.still_has_question():
    new_question.next_question()
print(f"\nYou have completed the Quiz \n Your final score was: {new_question.score}/{new_question.question_number}")