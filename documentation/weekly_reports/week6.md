# Week 6 Report

## What I've done this week

- I've implemented iterative deepening to the minimax so instead of having a fixed depth it will keep searching until the time is up
- Implemented a exception in the minimax that will be raised if the time is up so it doesnt keep searching
- I have implemented a cache that will store the best move and its evaluation based on the current board, player and depth

## State of program

The program is done, the AI has a cache and iterative deepening so in one second it searches until depth 5 on average, that paired with a set of heuristics whose weights change depending on the phase (early, mid and late game) leaves us with a pretty hard AI to beat.

## Learned this week

- How to implement iterative deepening for a minimax
- How to raise an exception so that the time for the search is exactly what it is specified
- How to implement a cache for the minimax

## Difficulties I encountered

- It was quite difficult for me to make the cache, I ended up implement the simplest version because the one that Hannu recommended me I was unable to make it.

## Next week

- Finish all the documentation
- Finnish all the tests for a 100% coverage
