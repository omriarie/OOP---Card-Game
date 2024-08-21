# Domino Game System

![Domino Game Logo](Domino Game-logo.png "Logo of the Domino Game")

This project is a Domino game implemented using Object-Oriented Programming (OOP) principles in Python. The game supports various player strategies and team-based gameplay, with an emphasis on modularity and code reuse. The project also includes a comprehensive suite of unit tests to ensure the correctness and reliability of the game components.

## Key Features

- **OOP Structure:** The game is structured using OOP principles, with well-defined classes and methods for each game component.
- **Player Strategies:** The system includes different player types (`NaivePlayer`, `RandomPlayer`, `MaxScorePlayer`), each with a unique strategy for playing the game.
- **Team-Based Play:** Players can be grouped into teams, allowing for team-based competition in the game.
- **Game Logic:** The game logic manages the interactions between players, the board, and the domino tiles, ensuring a smooth and consistent gameplay experience.
- **Extensive Testing:** The project includes unit tests for each class and method, ensuring that all components work as expected and making it easier to identify and fix bugs.

## Technologies Used

- **Python:** The game is implemented in Python, leveraging its OOP capabilities.
- **unittest:** Python's built-in `unittest` framework is used to create and run tests for the project.

## Project Structure

- **`Collection.py`:** A base class for managing collections of dominoes or other game pieces.
- **`Domino.py`:** Represents an individual domino tile with methods for comparing and flipping tiles.
- **`Board.py`:** Manages the game board, where dominoes are placed during gameplay.
- **`Hand.py`:** Represents a player's hand, managing the collection of dominoes they hold.
- **`Player.py`:** An abstract base class for all player types, providing common functionality.
- **`NaivePlayer.py`:** A player who places the first available domino that matches the board.
- **`RandomPlayer.py`:** A player who shuffles their hand randomly before placing a domino.
- **`MaxScorePlayer.py`:** A player who prioritizes placing the highest-scoring dominoes.
- **`Team.py`:** Manages a team of players, tracking their combined score and managing their turns.
- **`Game.py`:** Oversees the gameplay, alternating turns between two teams and determining the winner.
- **Test Files:** A suite of test files (e.g., `TestBoard.py`, `TestDomino.py`) that verify the functionality of each component using the `unittest` framework.

## Unit Testing

The project includes a comprehensive suite of unit tests to ensure that each component of the game functions as expected. The tests cover the core functionalities of each class, including the logic for adding and removing dominoes, managing player hands, team interactions, and game flow. The unit tests achieve a code coverage of approximately 90%, providing confidence in the robustness and reliability of the implementation.

To run the tests and verify the functionality, use the following command:

```bash
python -m unittest discover
```

## Setup and Installation

Ensure you have Python installed on your system. This project was developed using Python 3.8.

1. **Clone the repository**
   ```bash
   git clone https://github.com/omriarie/OOP---Card-Game
   ```

2. **Navigate to the project directory**
   ```bash
   cd OOP---Card-Game
   ```
3. **Install dependencies**  
   No additional dependencies are required, just Python 3.

## Running the Application
**Game Execution**  
You can instantiate and run the game by creating instances of the Board, Player, and Team classes and calling the play method in the Game class.

## Running Tests
To run the tests and ensure that everything is functioning correctly, use the following command:
```bash
   python -m unittest discover
   ```

## Contact
For any inquiries or issues, please open an issue on the GitHub repository or contact the maintainers directly:

Omri Arie – omriarie@gmail.com  
Project Link: https://github.com/omriarie/Trivia-Client-Server
