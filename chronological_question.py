from random import shuffle
from itertools import combinations
from main import Event
from score import Score
def ask_chronological_question(events:[Event]) -> list[int]:
    return [int(input(f"Enter the number of the event {index}: "))
            for index in range(1, len(events) + 1)]
def compute_answer(events: list[Event]) -> list[int]:
    date_to_index = {event.date: index for index, event in enumerate(events, start=1)}
    return [date_to_index[date] for date in sorted(date_to_index.keys())]

def create_question(events: [Event]) -> str:
    return f"Place the following events in chronological order:\n" + \
           "\n".join([f"{index}-{event.name}" for index, event in enumerate(events, start=1)])
def ask_all_chronological_question(events: list[Event], number_of_event = 2, score = Score()) -> None:
    question = create_cobination_of_question(events, number_of_event)
    for events in question:
        print(create_question(events))
        user_answer = ask_chronological_question(events)
        correct_answer(events, user_answer, score)
        print(score)

def correct_answer(events: [Event], user_answer: list[int], score:Score) -> None:
    good_answer = compute_answer(events)
    if is_good_answer(user_answer, good_answer):
        score.on_good_answer()
    else:
        score.on_wrong_answer()
def create_cobination_of_question(events: [Event], number_of_event:int) -> list[list[Event]]:
    questions = list(combinations(events, number_of_event))
    shuffle(questions)
    return questions
def is_good_answer(user_answer:[int], computer_answer:[int]) -> bool:
    return user_answer == computer_answer
