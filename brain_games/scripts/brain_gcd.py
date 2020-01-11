#!/usr/bin/env python3
from brain_games.games.gcd import RULE, game_logic
from brain_games.engine import game_engine


def main():
    game_engine(RULE, game_logic)


if __name__ == '__main__':
    main()
