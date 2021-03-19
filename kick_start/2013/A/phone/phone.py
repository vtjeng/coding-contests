#!/usr/bin/env python3

count_to_descr = {
    2: "double",
    3: "triple",
    4: "quadruple",
    5: "quintuple",
    6: "sextuple",
    7: "septuple",
    8: "octuple",
    9: "nonuple",
    10: "decuple",
}

digit_to_descr = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def get_digits_descr(digit, count):
    digit = int(digit)
    if count in count_to_descr:
        return f"{count_to_descr[count]} {digit_to_descr[digit]}"
    return " ".join([digit_to_descr[digit]] * count)


def get_block_descr(block: str):
    digit_count = None
    prev_digit = None
    digits_descrs = []
    for digit in block:
        if digit == prev_digit:
            digit_count += 1
        else:
            if prev_digit is not None:
                digits_descrs.append(get_digits_descr(prev_digit, digit_count))
            prev_digit = digit
            digit_count = 1
    digits_descrs.append(get_digits_descr(prev_digit, digit_count))
    return " ".join(digits_descrs)


def process(case: str):
    phone_number, block_desr = case.strip().split()
    block_sizes = list(map(int, block_desr.split("-")))
    block_start = 0
    block_descrs = []
    for block_size in block_sizes:
        block_descr = get_block_descr(
            phone_number[block_start : block_start + block_size]
        )
        block_descrs.append(block_descr)
        block_start += block_size
    return " ".join(block_descrs)


# Option B: Single line per case
num_cases = int(input())
for i in range(num_cases):
    print(f"Case #{i+1}: {process(input())}")
