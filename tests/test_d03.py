import io

from aoc23.d03 import solve_p1, solve_p2


def test_solve_p1():
    input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
    """.strip()
    assert solve_p1(io.StringIO(input)) == 4361


def test_solve_p2():
    input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
    """.strip()
    assert solve_p2(io.StringIO(input)) == 467835
