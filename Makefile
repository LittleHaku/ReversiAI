# Define variables
PYTHON = python3
TEST_MODULES = tests.test_reversi
COVERAGE_COMMAND = coverage
COVERAGE_OMIT = "tests/*"
POETRY = poetry

# Define targets

# Install poetry
install_poetry:
	curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
dependencies:
	$(POETRY) install

# Play a game of Reversi
play:
	$(POETRY) run python3 src/reversi/main.py

# Execute all tests
test:
	$(POETRY) run pytest -v

# Generate code coverage report
coverage:
	poetry run coverage run -m pytest
	poetry run coverage report -m

# Style check with flake8
flake8:
	$(POETRY) run flake8

# Clean up coverage data
clean_data_cov:
	$(COVERAGE_COMMAND) erase
	find . -name '.coverage' -exec rm -rf {} +

# Remove all generated files
clean_files_cov: clean_coverage
	rm -rf htmlcov

# Remove all __pycache__ directories
clean_pycache:
	find . -name '__pycache__' -exec rm -rf {} +

# Clean .pytest_cache at all levels
clean_pytest_cache:
	find . -name '.pytest_cache' -exec rm -rf {} +

# Clean all
clean: clean_data_cov clean_files_cov clean_pycache clean_pytest_cache

.PHONY: test_all coverage clean_coverage
