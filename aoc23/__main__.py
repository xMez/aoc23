import argparse
import logging

from aoc23 import d01

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("challenge", type=str, choices=["d01"])
    parser.add_argument("file_path", type=str)
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()

    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(args.verbose, len(levels) - 1)]
    logging.basicConfig(level=level)

    challenge: str = args.challenge
    path: str = args.file_path
    match challenge:
        case "d01":
            d01.main(path)
        case _:
            pass


if __name__ == "__main__":
    main()
