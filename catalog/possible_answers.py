from .forms import AnswerForm
import random

POSSIBLE_ANSWERS = (('c4', 'c#4', 'd4', 'd#4', 'e4', 'f4', 'f#4', 'g4', 'g#4', 'a4', 'a#4', 'b4'),
                    ('major', 'minor'),
                    ())

ANSWERS_QUANTITY = 4


def create_form(task_type, correct_answer):
    possible_answers = list(POSSIBLE_ANSWERS[task_type])
    result_answers = []
    if task_type == 1:
        result_answers.append([correct_answer, correct_answer])
        index = random.randint(0, len(possible_answers))
        possible_answers.remove(correct_answer)
        result_answers.insert(index, [possible_answers[0], possible_answers[0]])
        form = AnswerForm(result_answers)
    else:
        possible_answers.remove(correct_answer)
        for i in range(ANSWERS_QUANTITY - 1):
            index = random.randint(0, len(possible_answers) - 1)
            result_answers.append([possible_answers[index], possible_answers[index]])
            possible_answers.pop(index)
        index = random.randint(0, len(result_answers) - 1)
        result_answers.insert(index, [correct_answer, correct_answer])
        form = AnswerForm(result_answers)
    return form
