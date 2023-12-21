import argparse
import logging
import glob
from importlib import import_module
from pathlib import Path

module_path = Path(__file__).parent
CHALLENGES = [Path(path).stem for path in glob.glob(f"{module_path}/d*.py")]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("challenge", type=str, choices=CHALLENGES)
    parser.add_argument("file_path", type=str)
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()

    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(args.verbose, len(levels) - 1)]
    logging.basicConfig(level=level)

    challenge = args.challenge
    path = args.file_path

    module = import_module(f".{challenge}", __package__)
    func = getattr(module, "main")
    result = func(path)
    print(result)


if __name__ == "__main__":
    main()
