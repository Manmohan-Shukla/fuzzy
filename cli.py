import argparse
from fuzzy import  DEFAULT_DURATION , DEFAULT_LIMIT ,VALID_DURATION
def main():
        parser = argparse .ArgumentParser()
        parser.add_argument("-d",
                            "--duration",
                            type=str,
                            choices=VALID_DURATION,
                            default=DEFAULT_DURATION
                            )
        parser.add_argument("-l",
                            "--limit",
                            type=int,
                            default=DEFAULT_LIMIT)
        parser.add_argument(
        "-c", "--calendar", action="store_true", help="Use calendar-based date ranges"
        )

        args = parser.parse_args()
        duration= args.duration
        limit=args.limit
