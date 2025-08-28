from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(self.window, text="Score: 0", foreground="white", background=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 18, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(self.window, image=true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(self.window, image=false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.configure(background="white")

        if self.quiz.still_has_questions():
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(self.question_text, text=f"You've completed the quiz.\nYour final score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.configure(state="disabled")
            self.false_button.configure(state="disabled")


    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(background="green")
        else:
            self.canvas.configure(background="red")

        self.window.after(1000, self.get_next_question)

