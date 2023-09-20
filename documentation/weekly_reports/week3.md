# Week 3 Report

## What I've done this week

I've made an AI that plays randomly, it's not very good but it's a start since I didn't know very well how to handle the different turns of each player.
Now I've upgraded it to a minimax algorithm (without alphabeta prunning yet) that uses a trivial heuristic that just counts the pieces.

## State of program

The program now has an AI that is able to play, it is easy to beat but it's interesting to play against it, it's just a greedy AI.

## Learned this week

- I've learned how to implement a minimax with a simple heuristic.
- I've learned how to manage turns between an AI and a human in a two player game.

## Difficulties I encountered

- I've had a few difficulties with the turns since I didn't know how to make the AI just play in its turn and not in the human's turn, but solved it soon.
- I also had problems with the minimax, not because of the theory since I know how it works but because I didn't know how to make it so that it didn't modify the current game, I started trying to make copies of the current state of the game and complicating myself until I just realized I could just start a new game instance and play there, so I did that and it worked.

## Next week

- I will implement alphabeta prunning.
- I will make better heuristics, with different weights (i already have them noted down).
- I may try to implement a menu, but the main focus it's on the AI.
