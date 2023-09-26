import html
class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.quiz_length = 0
        self.current_question=None
    def next_question(self):

        self.current_question = self.question_list[self.question_number]
        self.question_number+=1
        q_text = html.unescape(self.current_question.text)
        return f"{self.question_number}: {q_text}"

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            return True


    def print_score(self):
        print(f"Your score = {self.score} / {self.x}")

    def win_or_lose(self):
        return self.score > self.x/2

    def increment_score(self):
        if self.check_answer():
            return self.score+1