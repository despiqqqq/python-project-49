#!/usr/bin/env python3

from brain_games.scripts.cli import welcome_user as welcome_user


def main():
    name = welcome_user()
    return name


if __name__ == '__main__':
    main()
