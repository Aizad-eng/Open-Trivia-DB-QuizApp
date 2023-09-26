from data import collect_quiz_questions
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
question_bank = []


for question in collect_quiz_questions():
    question_text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(question_text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_interface = QuizInterface(quiz)


