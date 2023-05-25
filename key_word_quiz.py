from main import Event
from score import Score


def is_good_answer(user_answer: [str], key_word: [str]) -> bool:
    print(f"kew word list: {key_word}")
    for word in key_word:
        print(f"key word search: {word}")
        print(f"user answer: {user_answer}")
        print(f"Is correct: {word in user_answer}")
        if word in user_answer:
            return True
    return False


def correct_answer(events: Event, user_answer: str, score: Score) -> None:
    if is_good_answer(user_answer, events.key_word):
        score.on_good_answer()
    else:
        score.on_wrong_answer()


def ask_question(event: Event, score: Score) -> None:
    print(f"Question: what is {event.name}?")
    user_answer = input("Enter your answer: ")
    correct_answer(event, user_answer, score)


def ask_all_question(events: [Event], score: Score) -> None:
    for event in events:
        ask_question(event, score)
        print(score)
