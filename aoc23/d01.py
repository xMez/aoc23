import logging
import regex as re


num_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
pattern = "(" + r"\d|" + r"|".join(num_map.keys()) + ")"

def get_sum(path: str) -> int:
    sum = 0
    with open(path) as file:
        for line in file:
            numbers = re.findall(pattern, line, overlapped=True)
            logging.debug(numbers)
            logging.debug(f"LINE: {line[:-1]}")
            logging.debug(f"NUMS: {numbers[0]}, {numbers[-1]}")
            if numbers[0] in num_map.keys():
                sum += 10 * num_map[numbers[0]]
            else:
                sum += 10 * int(numbers[0])
            if numbers[-1] in num_map.keys():
                sum += num_map[numbers[-1]]
            else:
                sum += int(numbers[-1])
    return sum


def main(path: str) -> None:
    print(get_sum(path))
