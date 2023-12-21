import logging
from typing import TextIO

import regex as re

limits = {"r": 12, "g": 13, "b": 14}
pattern = r"\d+ [r|g|b]"


def solve(file: TextIO) -> int:
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
