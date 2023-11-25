import Solutions.Day01
import Lib.Common

def solutions : List (IO Unit) := [
  Day01.main
]

def sep (n : Nat) : IO Unit := do
  IO.println s!"Day {n}:"

def main : IO Unit := do
  let it := List.map sep ∘ List.map (· + 1) ∘ List.range
  (it solutions.length).interleave solutions |>.forM id
