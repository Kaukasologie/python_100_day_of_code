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
        self.canvas = Canvas(self.window, width=500, height=300, background="white")

        self.question_text = self.canvas.create_text(
            250,
            150,
            width= 480,
            justify="left",
            fill=THEME_COLOR,
            font=("Arial", 18, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.title_text = self.canvas.create_text(
            250,
            50,
            width=480,
            justify="center",
            fill=THEME_COLOR,
            font=("Arial", 18, "bold")
        )


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
        self.score_label.configure(text=f"Score: {self.quiz.score}")
        self.true_button.configure(state="active")
        self.false_button.configure(state="active")

        if self.quiz.still_has_questions():
            q_text, q_category = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
            self.canvas.itemconfigure(self.title_text, text=f"Question: {self.quiz.question_number} from {len(self.quiz.question_list)}.\n"
                                                               f"Category: '{q_category}'.")
        else:
            self.canvas.itemconfigure(self.question_text, text=f"You've completed the quiz.\n\nYour scored {self.quiz.score} points out of {self.quiz.question_number} possible.")
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
        self.true_button.configure(state="disabled")
        self.false_button.configure(state="disabled")
        self.window.after(1000, self.get_next_question)

