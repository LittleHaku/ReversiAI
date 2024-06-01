# ReversiAI

[![CI](https://github.com/LittleHaku/ReversiAI/actions/workflows/main.yml/badge.svg)](https://github.com/LittleHaku/ReversiAI/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/LittleHaku/ReversiAI/graph/badge.svg?token=5BP77HLZEI)](https://codecov.io/gh/LittleHaku/ReversiAI)

## Brief Description

A Reversi game with an AI implementation that uses minimax with alphabeta pruning and different heuristics to play.

Made for the course TKT20010 at the University of Helsinki.

The project test coverage can be checked at the top of the readme where it says `codecov`

### Key Features

- **AI Opponent:** Face off against an AI adversary with advanced decision-making capabilities.
- **Comprehensive Testing:** Thorough test coverage ensures robustness and reliability.
- **Extensive Documentation:** Detailed documentation provides insights into project specifications, implementation details, and gameplay instructions.

## Documentation

- [Project Specification](documentation/project_specification.md): Details regarding project description, data sctructures, etc.
- [Manual/Instructions](documentation/how_to_play.md): How to install and run the game, how to play Reversi/Othello and modify the difficulty.
- [Testing](documentation/testing.md): What is being tested, and how to replicate the tests.
- [Implementation](documentation/implementation.md): How the project was implemented and other details.

## Weekly Reports

Track the progress and development of the project through weekly reports:

- [Hours Worked](documentation/hours_worked.md)
- [Week 1](documentation/weekly_reports/week1.md)
- [Week 2](documentation/weekly_reports/week2.md)
- [Week 3](documentation/weekly_reports/week3.md)
- [Week 4](documentation/weekly_reports/week4.md)
- [Week 5](documentation/weekly_reports/week5.md)
- [Week 6](documentation/weekly_reports/week6.md)

## Instructions

You can check a more detailed version in the [Manual/Instructions](documentation/how_to_play.md).

1. Clone the repo and then access the directory
```bash
git clone https://github.com/LittleHaku/ReversiAI/
```
2. Install poetry, skip if you already have it
```bash
make install_poetry
```
or 
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
3. Install dependencies
```bash
make dependencies
```
4. Run the game
```bash
make play
```

