import logging
import math
from typing import TextIO

import regex as re

limits = {"r": 12, "g": 13, "b": 14}
pattern = r"\d+ [r|g|b]"


def solve_p1(file: TextIO) -> int:
    sum = 0
    for line in file:
        game_str, cube_str = line.split(":")
        game = int(game_str.split(" ")[1].strip())
        rounds = cube_str.strip().split(";")
        try:
            for round in rounds:
                cubes: list[str] = re.findall(pattern, round)
                for cube in cubes:
                    v, k = cube.split(" ")
                    if limits[k] < int(v):
                        raise StopIteration
            logging.debug(game)
            sum += game
        except StopIteration:
            pass
    return sum


def solve_p2(file: TextIO) -> int:
    sum = 0
    for line in file:
        _, cube_str = line.split(":")
        rounds = cube_str.strip().split(";")
        count = {"r": 0, "g": 0, "b": 0}
        for round in rounds:
            cubes: list[str] = re.findall(pattern, round)
            for cube in cubes:
                v, k = cube.split(" ")
                count[k] = int(v) if int(v) > count[k] else count[k]
        sum += math.prod(count.values())
    return sum


def solve(file: TextIO) -> int:
    return solve_p2(file)
