class Score:
    def __init__(self, start=0):
        self.score = start
        self.lenght = 0

    def __add__(self, other):
        self.score += other
        self.lenght += 1
        return self

    @property
    def pourcentage(self):
        if self.lenght == 0:
            return 0
        return self.score / self.lenght * 100

    def __str__(self):
        return f"Score(%): {self.pourcentage}%\n" \
               f"Score(/): {self.score}/{self.lenght}"

    def on_good_answer(self) -> None:
        print("Good answer")
        self += 1

    def on_wrong_answer(self, correct_answer:str = None) -> None:
        print("Wrong answer")
        if correct_answer is not None:
            print(f"The correct answer was: {correct_answer}")
        self += 0
