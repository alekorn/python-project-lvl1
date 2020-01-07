#!/usr/bin/env python3
from brain_games.cli import greet
from brain_games.even_game import game_logic


def main():
    greet()
    game_logic()


if __name__ == '__main__':
    main()
