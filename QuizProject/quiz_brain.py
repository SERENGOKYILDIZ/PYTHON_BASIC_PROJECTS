class QuizBrain:
    def __init__(self, list):
        self.questionNumber = 0
        self.questionList = list
        self.score=0

    def next_question(self):
        current_question = self.questionList[self.questionNumber]
        self.questionNumber += 1
        answer = input(f"Q.{self.questionNumber}) {current_question.text} (True/False)")
        self.Check_Answer(answer, current_question.answer)

    def Still_has_questions(self):
        return self.questionNumber < len(self.questionList)


    def Check_Answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Dogru !! :)")
            self.score += 1
        else:
            print("Yanlis !! :(")
        print(f"Cevap: {correct_answer}")
        print(f"Durum: {self.score}/{self.questionNumber}")
        print("\n")