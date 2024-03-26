from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for letter in question_data:
    question_text = letter["text"]
    question_answer = letter["answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

Game = QuizBrain(question_bank)

while Game.Still_has_questions():
    Game.next_question()

print("Oyun bitti!")
print(f"Puan: {Game.score}/{Game.questionNumber}")