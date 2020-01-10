#!/usr/bin/env python3
from brain_games.games.gcd import rule, game_question
from brain_games.engine import game_engine


def main():
    game_engine(rule, game_question)


if __name__ == '__main__':
    main()
