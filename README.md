
# Pi Digits Calculator
This project calculates the digits of Pi using the spigot algorithm in Python.
## Description

The spigot algorithm is used to generate the digits of Pi in this project. For more details on the algorithm, refer to the [spigot algorithm paper](https://www.cs.williams.edu/~heeringa/classes/cs135/s15/readings/spigot.pdf).

## Usage

### Requirements

- Python 3.x

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/KaanBahaSever/pi-digits.py.git
```

### Running

1. Navigate to the project directory:

```bash
cd pi-digits.py
```

2. Run the `main.py` file:

```bash
python main.py
```

### Example

The following example in `main.py` generates the first 100 digits of Pi:

```python
# Example usage: Generate the first 100 digits of Pi
print(generate_pi_digits(100))
```

## Functions

### `pi_spigot`

A generator function that calculates the digits of Pi using the spigot algorithm.

### `generate_pi_digits(limit)`

Generates a specified number of digits of Pi and returns them as a string.

- `limit`: The number of Pi digits to generate.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
