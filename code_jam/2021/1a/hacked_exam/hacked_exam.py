#!/usr/bin/env python3


import sys

from fractions import Fraction
import operator as op
from functools import reduce
from collections import Counter

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def prod(iterable):
    return reduce(op.mul, iterable, 1)


def ncr(n, r):
    assert int(n) == n
    assert int(r) == r
    n = int(n)
    r = int(r)
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom  # or / in Python 2


def get_vals(s):
    return list(map(int, s.strip().split()))


def convert(s):
    # s contains T or F
    return [c == "T" for c in s]


def invert(bs):
    return [not (b) for b in bs]


def deconvert(s):
    return "".join(["T" if c else "F" for c in s])


def get_best_answer_and_score(solutions, num_questions):
    num_students = len(solutions)
    if num_students < 3:
        # just go with the better student
        return sorted(solutions, key=lambda x: x[1], reverse=True)[0]
    if num_students == 3:
        sol1, sol2, sol3 = sorted(solutions, key=lambda x: x[1], reverse=True)
        answer_1, score_1 = sol1
        answer_2, score_2 = sol2
        answer_3, score_3 = sol3

        score = dict()
        score[1] = score_1
        score[2] = score_2
        score[3] = score_3
        # None if all students agreed
        minority_student = []

        for z1, z2, z3 in zip(answer_1, answer_2, answer_3):
            if z1 == z2:
                if z2 == z3:
                    minority_student.append(None)
                else:
                    minority_student.append(3)
            elif z1 == z3:
                minority_student.append(2)
            else:
                minority_student.append(1)
        # good solutions within each type of problem
        msc = Counter(minority_student)

        numerator = Counter()
        num_total_configurations = 0

        eprint("")
        eprint(f"minority_student_count: {msc}")
        for x in range(0, msc[None] + 1):
            minority_wrong_count = Counter()
            minority_wrong_count[None] = x
            for i in [1, 2, 3]:
                minority_wrong_count[i] = (
                    sum(score.values())
                    - score[i]
                    - sum(msc.values())
                    + msc[None]
                    + msc[i]
                    - 2 * minority_wrong_count[None]
                ) // 2
            if any(minority_wrong_count[i] > msc[i] for i in [1, 2, 3]):
                continue
            eprint(minority_wrong_count)
            num_possible_choices = prod(
                ncr(msc[i], minority_wrong_count[i]) for i in msc
            )
            for minority_student, v in minority_wrong_count.items():
                numerator[minority_student] += num_possible_choices * v
            num_total_configurations += num_possible_choices

        probability_correct = {
            k: 0
            if numerator[k] == 0
            else Fraction(numerator[k], (msc[k] * num_total_configurations))
            for k in msc
        }
        majority_is_correct = {k: v >= 0.5 for k, v in probability_correct.items()}
        eprint(probability_correct)

        ev_numerator = 0
        for minority_student in msc:
            if majority_is_correct[minority_student]:
                ev_numerator += numerator[minority_student]
            else:
                ev_numerator += msc[minority_student] * num_total_configurations
                ev_numerator -= numerator[minority_student]

        eprint(ev_numerator)
        eprint(num_total_configurations)
        eprint(Fraction(ev_numerator, num_total_configurations))
        return sorted(solutions, key=lambda x: x[1], reverse=True)[0]


def process(solutions_raw, num_questions):
    solutions = []
    for solution_raw in solutions_raw:
        answer_raw, score_raw = solution_raw.split()
        answer = convert(answer_raw)
        score = int(score_raw)
        if score < num_questions / 2:
            answer = invert(answer)
            score = num_questions - score
        solutions.append((answer, score))
    best_answer, best_score = get_best_answer_and_score(solutions, num_questions)
    r = f"{deconvert(best_answer)} {best_score}/1"
    return r


if __name__ == "__main__":
    ## Comment out the appropriate option
    # Option A: Multiple lines per solution_raw
    num_solution_raws = int(input())
    for i in range(num_solution_raws):
        num_students, num_questions = get_vals(input())
        solution_raw = []
        for j in range(num_students):
            solution_raw.append(input())
        print(f"Case #{i+1}: {process(solution_raw, num_questions)}")
