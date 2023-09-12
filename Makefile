# Define variables
PYTHON = python3
TEST_MODULES = tests.test_reversi
COVERAGE_COMMAND = coverage
COVERAGE_OMIT = "tests/*"

# Define targets

# Play a game of Reversi
play:
	$(PYTHON) -m reversi

# Execute all tests
test_all:
	$(PYTHON) -m unittest $(TEST_MODULES)

# Generate code coverage report
coverage:
	rm -f .coverage
	$(COVERAGE_COMMAND) run -m unittest $(TEST_MODULES)
	$(COVERAGE_COMMAND) report -m --omit=$(COVERAGE_OMIT)
	$(COVERAGE_COMMAND) html --omit=$(COVERAGE_OMIT)

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
