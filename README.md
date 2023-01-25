A basic realization of Sea Battle game in Python with primitive AI.
=====

Project description
----------
The game is built as a final project for completing a course 'Kind kind Python OOP' on Stepik website. The project meets all requirements of the technical task and has the following funcionality:
1. Two game zones are generated at the start  (please refer to GameManager file): one for a player and one for AI.
2. AI makes the first move, which can mean either a missed shot(displayed as int 3 on the respective game zone cell), damaging a ship(as int 4 on the game zone) or wiping a ship out (wiped ship and contiguous cells have value of integer 2). In case of the first event the move ends and the player makes his move by entering two ints in a sinle row through a whitespace. In case of the second and the third events AI continues to make moves untill he misses or wipes out all player's ship. The same for player's move.

System requirements
----------
* Python 3.10
* Works on Linux, Windows, macOS, BSD

Stek
----------
* Python 3.8


Project installation
----------

1. Clone repository to your machine:
```bash
git clone 

cd Sea Battle
```
2. Run game manager

