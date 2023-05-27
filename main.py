from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for n in question_data:
    text = n["text"]
    answer = n["answer"]
    my_question = Question(text, answer)
    question_bank.append(my_question)

quiz = QuizBrain(question_bank)

again = True
while again:
    quiz.nex_question()

    still_has = quiz.still_has_questions()
    if not still_has:
        again = False
    print(f"Your final score was: {quiz.score}")

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
