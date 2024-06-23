lint:
	cd app; poetry run ruff check . ; poetry run mypy .

format:
	cd app; poetry run ruff format .

run:
	cd app; poetry run python3 run.py

%:
	@: