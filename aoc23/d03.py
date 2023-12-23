import itertools
import logging
import math
from typing import TextIO

import regex as re

pattern = r"\d+"
part_pattern = r"\d+|\."
symbol_pattern = r"[@#$%^&*()_\-+={}[\]:;\"'<,>?/|]"


def solve_p1(file: TextIO) -> int:
    sum = 0
    matrix: list[str] = []
    for line in file:
        matrix.append(line)

    for index, line in enumerate(matrix):
        for num in re.finditer(pattern, line):
            part = ""
            start = num.start() - 1 if num.start() > 0 else 0
            end = num.end() + 1 if num.end() < len(line) else len(line)

            if index > 0:
                over = matrix[index - 1][start:end]
                part += over
            sides = matrix[index][start:end]
            part += sides
            try:
                under = matrix[index + 1][start:end]
                part += under
            except IndexError:
                pass

            part = re.sub(part_pattern, "", part).strip()

            if part:
                logging.debug(f"line: {index + 1}, part: {part}, num: {num}")
                sum += int(num.group(0))

    return sum


def solve_p2(file: TextIO) -> int:
    sum = 0

    matrix: list[str] = []
    for line in file:
        matrix.append(line)

    for index, line in enumerate(matrix):
        symbols = re.finditer(symbol_pattern, line)
        numbers = list(re.finditer(pattern, line))
        if index > 0:
            numbers += list(re.finditer(pattern, matrix[index - 1]))
        try:
            numbers += list(re.finditer(pattern, matrix[index + 1]))
        except IndexError:
            pass

        for symbol in symbols:
            parts: list[int] = []
            start = symbol.start() if symbol.start() + 1 > 0 else 0
            end = symbol.end() if symbol.end() < len(line) else len(line)

            for number in numbers:
                if number.start() <= end and number.end() >= start:
                    parts.append(int(number.group(0)))

            if len(parts) == 2:
                logging.debug(f"line: {index + 1}, part: {symbol}, num: {parts}")
                sum += math.prod(parts)

    return sum


def solve(file: TextIO) -> int:
    return solve_p2(file)
