install:
		poetry install
run:
		poetry run brain-games
lint:
		poetry run flake8 brain_games
.PHONY: install run lint
