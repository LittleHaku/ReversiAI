# Testing

## What is being tested

The tests for this project are in the `test_reversi.py` file. These tests have been made using the `unittest` library. The tests are divided into two classes:

- **TestReversiGame**: Tests the game logic, the board and the pieces.
- **TestReversiGameAI**: Tests the AI, the heuristics and the minimax with alphabeta pruning.
- The GUI has been manually tested.

## Installation

- Clone the repositoryTestReversiGameAI
- Install poetry with

    ```bash
    make install_poetry
    ```

    or

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

## Unit tests

To execute the unit testings:

```bash
make test
```

## See coverage

To see the coverage:

```bash
make coverage
```

## Checkstyle

- Being at the root of the project
- Run

    ```bash
    make lint
    ```
