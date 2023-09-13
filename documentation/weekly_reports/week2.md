# Week 2 Report

## What I've done this week

I've started coding the game with a GUI using tkinter, the game is already ready to play but doesn't have an AI yet.

I have also made unit tests for the game implementation as well as for the GUI.

I added codecov so that the coverage of the tests can be seen publicly.

Apart from that I also checked with flake8 to see that the code is properly styled.

I have made the manual for the rules of the game and how to execut it and also how to execute the tests.

Lastly I have also implemented Poetry so that the project and its packages can be managed easily and with the help of a makefile the game and the tests can be executed super intuitively.

## State of program

The program has already a playeable game with a GUI although it doesn't have an AI.

## Learned this week

- I've learned how to properly structure a python project to manage its packages and dependencies.
- I've learned how to use Poetry and how to use codecov.
- I've learned how to make unit tests for a program with a GUI.

## Difficulties I encountered

- I had difficulties with Poetry since it was the first time I've used it, and still I'm not completely sure if I have set it up properly, I guess so because works in my computer and also with the GitHub actions.
- I had difficulties setting up codecov, first because I had never used it neither the GitHub actions, and second because once I managed to make it work I finished the tests and found out that the test with a GUI couldn't be executed in the GitHub actions so I had to find a way to do it and ended up using xvfb.
- Having a 100% coverage because of the if __name__ == "__main__" which I can't manage to test it.

## Next week

- I will add a menu to choose to play against an AI or with another human, and maybe AI vs AI.
- I may add a help option that will show you where you can place a piece.
- I will make the minimax algorithm with alphabeta pruning and some basic heuristic.
- I will also document all the code I write.
