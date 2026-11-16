# tiny-chess-01

A chess engine in 4 KB of Python, written for the make.fun bounty
"Build the strongest chess engine in 4 KB of Python".

`main.py` (4,092 bytes) is a self-contained engine: 0x88 board, negamax
with alpha-beta, quiescence search, transposition table, iterative
deepening on a fixed node budget, and a tapered piece-square evaluation.
It speaks the make.fun agent protocol (`MAKEFUN_ENV_URL`) and plays a
full game as either colour. Python 3.13 standard library only, no
network calls, no randomness — fully deterministic.

Practice trial (kit `practice/trial-0`): 2 wins, 1 draw, 3 losses,
Elo 1191 (above the 1154 final bar).
