# Advent of Code 2023

My [Advent of Code 2023](https://adventofcode.com/2023) solutions.

## Table of Contents
- [Advent of Code 2023](#advent-of-code-2023)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
    - [Getting input](#getting-input)
    - [Running solutions](#running-solutions)

## Usage

### Getting input

`get_input.py` script can be used for acquiring the input data for the current day.
In order for this to work, you're current AOC `SESSION` cookie must be found from
from `COOKIE` environment variable.

```sh
export COOKIE=<cookie here>
./get_input.py
```

### Running solutions

All solutions expect to receive input from `stdin`.

So to run day [01p1](./src/01p1.py) you need to do the following.

```sh
./src/01p1.py < <inputfile>
```
