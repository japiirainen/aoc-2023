# aoc-2023

[Advent of Code 2023](https://adventofcode.com/2023) solutions written in [Haskell](https://www.haskell.org/).

## usage

This project is usable either via `nix` or via `cabal`. I will provide
commands for both in the following sections.

### run all solutions

#### nix

```sh
nix run .#aoc
```

#### cabal

```sh
cabal run exe:aoc
```

### run specific solution

It is possible to run only a specific day. In this example day # `01` is ran.

#### nix

```sh
nix run .#01
```

#### cabal

```sh
cabal run exe:01
```
