instance : Monad List where
  pure := List.pure
  bind := List.bind

namespace List

def interleave.{u} {α : Type u} (xs ys : List α) : List α := do
  let (a, b) ← xs.zip ys
  [a, b]

end List
