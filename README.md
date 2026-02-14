# connect-4
Connect 4 game programmed in Python.<br>
Game was developed by Melina Fellner and Martin Matzer.

## How to install python package connect4
1. Open the terminal
2. Navigate to the root directory of this repository
3. There are two options where you can install the python package connect4. Run one of the following commands to install the python package:
```bash
# Option A: install into a configured python enviroment
pip install .

# Option B: install into system python
/usr/local/bin/python3 -m pip install .
```

## How to run the game
1. Open main.py file in root directory of this repository
2. Execute main.py file in terminal with one of the following commands depending on the option you picked above while installing the package:
```bash
# Option A — use python enviroment (matches where pip installs)
python main.py

# Option B — install into system python, then run with it

/usr/local/bin/python3 main.py
```
3. Follow the game instructions inside the terminal

## How to run unit tests

The project uses **unittest**. The package lives in `src/`, so Python must see that folder when importing `connect4`.

### Option 1: Command line (from project root) when package was not installed

```bash
# Run one test file
PYTHONPATH=src python -m unittest tests.test_game_board -v

# Run one test class
PYTHONPATH=src python -m unittest tests.test_game_board.TestWinCheck -v

# Run one test method
PYTHONPATH=src python -m unittest tests.test_game_board.TestWinCheck.test_horizontal_win_red -v
```

### Option 2: After package installation (no PYTHONPATH needed)

```bash
pip install .
python -m unittest discover -v -s tests -p "test_*.py"
```
