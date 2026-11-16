# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Bagorsari/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Bagorsari/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4 KB of Python, written for the make.fun bounty "Build the strongest chess engine in 4 KB of Python".

`main.py` (3,741 bytes) is a self-contained engine: 0x88 board, negamax with alpha-beta, quiescence search, transposition table, iterative deepening on a fixed node budget, and a tapered piece-square evaluation. It speaks the make.fun agent protocol (`MAKEFUN_ENV_URL`) and plays a full game as either colour. Python 3.13 standard library only, no network calls, no randomness — fully deterministic.

Practice trial (kit `practice/trial-0`): Elo 1191 and 1364 across two trials (mean 1,277, above the 1,154 final bar).

## Run it

```sh
MAKEFUN_ENV_URL=<game-server-url> python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=2t0236rq&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
