
install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install1:
	python3 -m pip install --user dist/*.whl

package-install:
	poetry build
	pip install --user dist/*.whl

lint: 
	poetry run flake8 brain_games

reinstall:
	pip install --user --force-reinstall dist/*.whl
