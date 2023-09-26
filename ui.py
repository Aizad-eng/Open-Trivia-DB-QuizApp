import time
from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=100, pady=100)
        self.score_label = Label(text = f"Score: 0", fg="White", bg =THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=400, height=250, bg="White")
        self.question_text = self.canvas.create_text(200, 125,text="Some question text",fill=THEME_COLOR, font=("Arial", 18, "normal"), anchor="center", width=390)

        self.canvas.grid(row=1, column=0, columnspan=2)

        true_image = PhotoImage(file=r"C:\Users\dxuxa\PycharmProjects\GUI-Quiz-app\right.png")
        self.true_button= Button(image=true_image, highlightthickness=0, command=self.true_answer, highlightcolor=THEME_COLOR, borderwidth=0, bg=THEME_COLOR)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file=r"C:\Users\dxuxa\PycharmProjects\GUI-Quiz-app\wrong.png")
        self.false_button = Button(bg=THEME_COLOR,image=false_image, highlightthickness=0, command=self.false_answer, highlightcolor=THEME_COLOR, borderwidth=0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="White")
            self.canvas.itemconfig(self.question_text, text="You have reached to the end of quiz")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)
            messagebox.showinfo(title="Oops", message="No more questions")

    def true_answer(self):
        is_right = self.quiz.check_answer("True",self.quiz.current_question.answer)

        self.score_label.config(text =f"Score: {self.quiz.score}")
        self.give_feedback(is_right)
    def false_answer(self):
        is_false = self.quiz.check_answer("False",self.quiz.current_question.answer)
        self.give_feedback(is_false)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="Green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_question)