"""
Connect 4 Game Package

This package contains the game logic for Connect 4.
"""

# Package metadata
__version__ = '1.0.0'
__author__ = 'Melina Fellner & Martin Matzer'

from .game_board import GameBoard
from .game_setup import GameSetup
from .players import HumanPlayer, Bot, SmartBot

# Define what gets imported with "from package import *"
__all__ = ['GameBoard', 'GameSetup', 'HumanPlayer', 'Bot', 'SmartBot']

