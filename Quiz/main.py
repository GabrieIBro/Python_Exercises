import random as rd
import data


class Game:
    def __init__(self):
        self.question = ""
        self.answer = ""
        self.index = 0
        self.correct = 1
        self.counter = 0
        self.victories = 0

    def get_question(self):
        """Get random question from list"""
        self.question = rd.choice(data.questions)
        self.index = data.questions.index(self.question)
        print(self.question["text"])

    def user_answer(self):
        """User input"""
        self.answer = str(input("Answer:")).strip().capitalize()

        while True:
            if self.answer == "True" or self.answer == "False":
                return
            else:
                print('INVALID ANSWER!')
                game.user_answer()

    def answer_verification(self):
        if self.answer == data.questions[self.index]["answer"]:
            print("Your answer is correct!\n")
            data.questions.pop(self.index)
            self.correct = 1
            return self.correct

        else:
            print("Your answer is wrong!\n")
            data.questions.pop(self.index)
            self.correct = 0
            return self.correct

    def score(self):
        self.counter += 1
        self.victories += self.correct
        if len(data.questions) == 0:
            print(f"Your score is ({self.victories}/{self.counter})")


game = Game()

while len(data.questions) > 0:
    game.get_question()
    game.user_answer()
    game.answer_verification()
    game.score()
