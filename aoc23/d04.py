import itertools
import logging
import math
from typing import TextIO

import regex as re

pattern = r"\d+"
copies = [1] * 1024


def solve_p1(file: TextIO) -> int:
    sum = 0
    for line in file:
        line = line.split(":")[1]
        game, win = line.split("|")
        numbers = set(re.findall(pattern, game))
        winning = set(re.findall(pattern, win))
        total = len(numbers.intersection(winning))
        logging.debug(f"Won {total} in game '{line.strip()}'")
        if total > 0:
            sum += pow(2, total - 1)
    return sum


def solve_p2(file: TextIO) -> int:
    sum = 0
    for index, line in enumerate(file):
        line = line.split(":")[1]
        game, win = line.split("|")
        numbers = set(re.findall(pattern, game))
        winning = set(re.findall(pattern, win))
        total = len(numbers.intersection(winning))
        if total > 0:
            for i in range(total):
                copies[index + i + 1] += copies[index]
        logging.debug(f"Got {copies[index]} cards in game '{line.strip()}'")
        sum += copies[index]
    return sum


def solve(file: TextIO) -> int:
    return solve_p2(file)
