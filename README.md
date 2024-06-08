# Uno Card Game

A simple Uno card game implementation in Python.

## Features

- Two-player game (Player 1 vs. Player 2)
- Basic Uno game rules: matching by color or number
- Automated gameplay with simple AI for both players
- Dynamic deck shuffling and card drawing

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/username/uno-card-game.git
    ```
2. Navigate to the project directory:
    ```sh
    cd uno-card-game
    ```
3. (Optional) Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

## Usage

Run the game using the following command:
    ```sh
    python uno_card_game.py
    ```

## How to Play

- The game starts with each player being dealt 7 cards.
- A card from the deck is placed face-up to start the game.
- Players take turns playing a card from their hand that matches the color or number of the face-up card.
- If a player cannot play a card, they draw a card from the deck.
- The game continues until one player has no cards left. The player who runs out of cards first wins.

## Code Overview

### `UnoCards` Class

Represents an individual Uno card with a color and a number. Provides methods to check if a card can be played based on the top card of the discard pile.

### `CollectionOfUnoCards` Class

Represents a collection of Uno cards, such as a deck or a player's hand. Provides methods to add, remove, shuffle, and manage cards.

### `Uno` Class

Manages the gameplay, including dealing cards, handling turns, and determining the winner.


## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes.


## Acknowledgments

This project was created by Ali Durgut.
