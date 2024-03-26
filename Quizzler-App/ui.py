from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.scoreLb = Label(text="Score: 0")
        self.scoreLb.config(bg=THEME_COLOR, fg="white", font=("Ariel", 12))
        self.scoreLb.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.Quest_Lb = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Deneme soru",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        rightImage = PhotoImage(file="./images/true.png")
        wrongImage = PhotoImage(file="./images/false.png")

        self.rightBtn = Button(image=rightImage, highlightthickness=0, command=self.true_btn)
        self.rightBtn.grid(column=0, row=2)
        self.wrongBtn = Button(image=wrongImage, highlightthickness=0, command=self.false_btn)
        self.wrongBtn.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.Quest_Lb, text=q_text)
        else:
            self.canvas.itemconfig(self.Quest_Lb, text="Tum sorular bitti")

    def answer_btn(self, answer: str):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.scoreLb.config(text=f"Score: {self.quiz.score}")
        self.window.after(500, func=self.get_next_question)

    def true_btn(self):
        self.answer_btn("true")

    def false_btn(self):
        self.answer_btn("false")