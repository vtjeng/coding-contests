#!/usr/bin/env python3


def get_best_answer_and_score(solutions):
    return sorted(solutions, key=lambda x: x[1], reverse=True)[0]


best_answer, best_score = get_best_answer_and_score(
    [([True, True, False], 2), ([False, False, True], 1)]
)
print(best_answer, best_score)

