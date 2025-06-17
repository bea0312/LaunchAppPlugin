# LaunchAppPlugin

## Overview
LaunchAppPlugin is a Python plugin designed to provide a simple way to launch the GNOME calculator using a keyboard shortcut. This project is structured to facilitate easy development and testing.

## Project Structure
```
LaunchAppPlugin
├── src
│   ├── __init__.py
│   ├── launch_calculator.py
│   └── utils.py
├── tests
│   └── test_launch_calculator.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation
To install the necessary dependencies for this project, run the following command:

```
pip install -r requirements.txt
```

## Usage
After installing the dependencies, you can use the plugin by triggering the keyboard shortcut associated with the LaunchCalculator action. This will open the GNOME calculator.

## Testing
To run the unit tests for the LaunchCalculator class, navigate to the `tests` directory and execute:

```
python -m unittest test_launch_calculator.py
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.