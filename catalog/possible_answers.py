from .forms import AnswerForm
import random

POSSIBLE_ANSWERS = (('c4', 'c#4', 'd4', 'd#4', 'e4', 'f4', 'f#4', 'g4', 'g#4', 'a4', 'a#4', 'b4'),
                    ('major', 'minor'),
                    ())

ANSWERS_QUANTITY = 4


def create_form(task_type, correct_answer):
    possible_answers = list(POSSIBLE_ANSWERS[task_type])
    result_answers = []
    possible_answers.remove(correct_answer)
    for i in range(ANSWERS_QUANTITY - 1):
        index = random.randint(0, len(possible_answers) - 1)
        result_answers.append([i, possible_answers[index]])
        possible_answers.pop(index)
    index = random.randint(0, len(result_answers) - 1)
    result_answers.insert(index, [index, correct_answer])
    for i in range(index + 1, ANSWERS_QUANTITY):
        result_answers[i][0] += 1
    form = AnswerForm(result_answers)
    return form
