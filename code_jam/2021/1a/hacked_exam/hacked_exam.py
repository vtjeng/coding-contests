#!/usr/bin/env python3


import sys

from fractions import Fraction
import operator as op
from functools import reduce
from collections import Counter

# courtesy https://stackoverflow.com/a/14981125/1404966
def eprint(*args, **kwargs):
    pass
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
        # students are indexed 1 through 3
        score = dict()  # Dict[int, int]
        answer = dict()  # Dict[int, List[bool]]
        for i, solution in enumerate(solutions):
            answer[i + 1], score[i + 1] = solution

        # Stores the student in the minority for each problem
        # None if all the students agreed
        minority_student_for_problem = []

        for z1, z2, z3 in zip(*[answer[i] for i in [1, 2, 3]]):
            if z1 == z2:
                if z2 == z3:
                    minority_student_for_problem.append(None)
                else:
                    minority_student_for_problem.append(3)
            elif z1 == z3:
                minority_student_for_problem.append(2)
            else:
                minority_student_for_problem.append(1)

        # We tally the number of times each student was in the minority.
        msc = Counter(minority_student_for_problem)

        count_weighted_probability = Counter()
        num_total_configurations = 0

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
            if not all(0 <= minority_wrong_count[i] <= msc[i] for i in [1, 2, 3]):
                continue
            num_possible_choices = prod(
                ncr(msc[i], minority_wrong_count[i]) for i in msc
            )
            for minority_student, v in minority_wrong_count.items():
                if v != 0:
                    count_weighted_probability[
                        minority_student
                    ] += num_possible_choices * Fraction(v, msc[minority_student])
            num_total_configurations += num_possible_choices

        # the probability that the majority choice is correct for a given problem,
        # indexed by the minority student for that problem
        probability_correct = {
            k: 0
            if count_weighted_probability[k] == 0
            else count_weighted_probability[k] / num_total_configurations
            for k in msc
        }

        # the expected value when choosing the most likely option for each problem
        # (either the majority choice if the probability that is is correct
        # is no lesser than 0.5, or the minority choice otherwise)
        expected_value = sum(
            max(v, 1 - v) * msc[minority_student]
            for minority_student, v in probability_correct.items()
        )

        # we also construct the best answer itself, iterating over each of the problems
        best_answer = []
        for i, ms in enumerate(minority_student_for_problem):
            if ms == None:
                majority_choice = answer[1][i]
            else:
                majority_choice = not answer[ms][i]
            if probability_correct[ms] < 0.5:
                # flip if probabiliy correct is bad
                best_answer.append(not majority_choice)
            else:
                best_answer.append(majority_choice)

        return best_answer, expected_value


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
    best_score = Fraction(best_score, 1)
    best_score_str = (
        f"{best_score}/1" if best_score.denominator == 1 else f"{best_score}"
    )
    r = f"{deconvert(best_answer)} {best_score_str}"
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
