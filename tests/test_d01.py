import io

from aoc23.d01 import solve


def test_solve_p1():
    input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
    """.strip()
    assert solve(io.StringIO(input)) == 142


def test_solve_p2():
    input = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
    """.strip()
    assert solve(io.StringIO(input)) == 281
