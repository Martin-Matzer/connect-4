# connect-4
Connect 4 game programmed in Python.<br>
Game was developed by Melina Fellner and Martin Matzer.

## How to install python package connect4
1. Open the command line or terminal
2. Navigate to the directory of this repository
3. Run the following command to install the python package

        pip install .

## How to run the game
1. Open main.py file
2. Execute main.py file
3. Open console and follow the ganme instructions

## How to run unit tests

The project uses **unittest** (not pytest). The package lives in `src/`, so Python must see that folder when importing `connect4`.

### Option 1: Command line (from project root)

```bash
# Run one test file
PYTHONPATH=src python -m unittest tests.test_game_board -v

# Run one test class
PYTHONPATH=src python -m unittest tests.test_game_board.TestWinCheck -v

# Run one test method
PYTHONPATH=src python -m unittest tests.test_game_board.TestWinCheck.test_horizontal_win_red -v
```

### Option 2: After editable install (no PYTHONPATH needed)

```bash
pip install -e .
python -m unittest discover -v -s tests -p "test_*.py"
```