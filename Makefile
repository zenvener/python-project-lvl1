install:
	 poetry install

brain-games:
	 poetry run brain-games
	 poetry run brain-even
	 poetry run brain-calc

build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


lint:
	poetry run flake8 brain_games


