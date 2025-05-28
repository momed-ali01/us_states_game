# US States Game

An interactive educational game that helps users learn and memorize the names and locations of all 50 US states. Built with Python using the Turtle graphics library, this game provides a fun and engaging way to test your knowledge of US geography.

## Features

- Interactive map of the United States
- Real-time state name input
- Visual feedback with state names appearing on the map
- Progress tracking (X/50 states correct)
- Automatic saving of missed states for later review
- Clean and intuitive interface
- Exit functionality that saves learning progress

## Requirements

- Python 3.x
- pandas
- turtle (built into Python standard library)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/momed-ali01/us_states_game.git
cd us_states_game
```

2. Install required dependencies:

```bash
pip install pandas
```

## Usage

Run the game:

```bash
python main.py
```

### Game Controls

- Text Input: Type the name of a US state
- "Exit" Command: End the game and save progress
- Click on the window to close after exiting

### Game Structure

- The game displays a blank map of the United States
- Players input state names one at a time
- Correct answers appear on the map at the state's location
- Progress is tracked (X/50 states correct)
- Upon exiting, missed states are saved to `states_to_learn.csv`

## Learning Resources

The game uses two main data files:

- `50_states.csv`: Contains the names and coordinates of all 50 US states
- `states_to_learn.csv`: Generated file containing states that need more practice

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
