
install:
	poetry install

brain-games:
	poetry run brain-games

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-prime:
	poetry run brain-prime

brain-progression:
	poetry run brain-progression
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
