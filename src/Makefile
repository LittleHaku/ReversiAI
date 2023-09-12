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
clean_coverage:
	$(COVERAGE_COMMAND) erase

.PHONY: test_all coverage clean_coverage
