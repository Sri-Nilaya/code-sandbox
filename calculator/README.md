# Python Calculator Project

A simple calculator application built in Python with both command-line and GUI interfaces.

## Project Overview

This project implements a calculator with basic arithmetic operations. It's structured using modular design principles to separate core logic from user interfaces, allowing for easy maintenance and extension.

The calculator features:
- Basic operations (addition, subtraction, multiplication, division)
- Command-line interface for quick calculations
- GUI interface using Tkinter (coming soon)
- Error handling for invalid inputs and edge cases

## Project Structure

```
calculator/
├── README.md
├── calculator/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── operations.py
│   ├── cli/
│   │   ├── __init__.py
│   │   └── interface.py
│   ├── gui/
│   │   ├── __init__.py
│   │   └── app.py
│   └── main.py
└── tests/
    ├── __init__.py
    └── test_operations.py
```

## Getting Started

### Prerequisites
- Python 3.6+

### Installation
1. Clone this repository
   ```
   git clone https://github.com/yourusername/python-calculator.git
   cd python-calculator
   ```

2. Run the calculator
   ```
   python -m calculator.main
   ```

## Usage

### Command-line Interface
The command-line interface allows you to perform calculations by following the prompts:
1. Enter the first number
2. Select an operation
3. Enter the second number
4. View the result

### GUI Interface (Coming Soon)
A graphical user interface built with Tkinter will be available in future updates.

## Development

This is a learning project created to practice Python programming concepts including:
- Modular code organization
- Object-oriented programming
- GUI development with Tkinter
- Testing and error handling

## Contributors
- Sri Nilaya 
- Sri Charan