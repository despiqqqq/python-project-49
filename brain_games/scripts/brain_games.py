#!/usr/bin/env python3


from brain_games.scripts.cli import ask_name_user


def welcome():
    print('Welcome to the Brain Games!')


def main():
    welcome()
    ask_name_user()


if __name__ == '__main__':
    main()
    