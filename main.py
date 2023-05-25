class Event:
    def __init__(self, name: str, date: int, importance:int, key_word:list[str] = None):
        self.name = name
        self.importance = importance
        self.date = date
        self.key_word = key_word

    @classmethod
    def from_string(cls, string: str, split_chartacter: str = ";"):
        name, date, key_word, importance = string.split(split_chartacter)
        return cls(name, int(date), int(importance), key_word.split(","))

def read_file(path:str = "sec4data.csv") -> list[Event]:
    with open(path, "r") as file:
        return file.readlines()
def load_from_file(path:str = "sec4data.csv"):
    return [Event.from_string(line) for line in read_file(path)]
def main():
    from chronological_question import ask_all_chronological_question
    from key_word_quiz import ask_all_question
    from score import Score
    score = Score()
    events = load_from_file()
    for event in events:
        print(event.key_word)
    ask_all_question(events, score)
    ask_all_chronological_question(events, number_of_event=2, score = score)


if __name__ == '__main__':
    main()