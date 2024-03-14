import argparse
from tenloc.say_my_name import say_my_name
from tenloc.metronome import metronome


def setup(argv) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="This is a Python 3 project.")
    parser.add_argument("--all", action='store_true',
                        help="Run all 'ten lines of code' examples.")
    parser.add_argument("-v", "--verbose",  action="store_true",
                        help="Enable verbose logging.")
    parser.add_argument('examples', type=str, nargs='*')
    return parser.parse_args(argv)


def run(args: argparse.Namespace, testing: bool = False) -> None:
    if args.all:
        say_my_name()
    elif args.examples:
        if 'say_my_name' in args.examples:
            say_my_name()
        if 'metronome' in args.examples:
            metronome(2, testing)
    else:
        print('Please specify an example, or --all')
