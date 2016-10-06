import argparse


def new_parser():
    parser = argparse.ArgumentParser(
        description="Config file manager",
    )

    subparsers = parser.add_subparsers(
        dest='subcommand',
        help='Available rce subcommands'
    )

    # List subcommand
    subparsers.add_parser(
        'list',
        help='list aliases'
    )

    # Search subcommand
    search_parser = subparsers.add_parser(
        'search',
        help='search aliases'
    )
    search_parser.add_argument(
        'alias',
        help='alias to search for'
    )

    # TODO: Implement 'add' subcommand

    # TODO: Implement 'edit' subcommand

    # TODO: Implement 'mv' (rename) subcommand

    # Help subcommand
    subparsers.add_parser(
        'help',
        help='show this help message',
    )

    return parser