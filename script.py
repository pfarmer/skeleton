#!env python

import sys

import argparse
import logging


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='script.py'
    )
    parser.add_argument("-d", "--debug", help="Run in debug mode",
                        action="store_true")

    log_level = logging.INFO

    args = parser.parse_args()
    if args.debug:
        log_level = logging.DEBUG

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s %(levelname)s: %(name)s:%(lineno)s: %(message)s"
    )

    logging.debug('Running in debug mode')


if __name__ == '__main__':
    sys.exit(main())