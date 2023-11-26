-- | `Prelude` for Advent of Code problems.
module Adlude (
  pickOne,
  countBy,
  count,
  counts,
  partialSums,
) where

import Data.Foldable (toList)
import Data.List (foldl', inits, scanl', tails)
import Data.Map (Map)
import Data.Map qualified as Map

pickOne :: [a] -> [(a, [a])]
pickOne xs = do
  (ys, x : zs) <- zip (inits xs) (tails xs)
  return (x, ys ++ zs)

countBy :: (Foldable f) => (a -> Bool) -> f a -> Int
countBy p = foldl' (\acc x -> if p x then acc + 1 else acc) 0

count :: (Foldable f, Eq a) => a -> f a -> Int
count = countBy . (==)

counts :: (Foldable f, Ord a) => f a -> Map a Int
counts xs = Map.fromListWith (+) [(x, 1) | x <- toList xs]

partialSums :: (Num a) => [a] -> [a]
partialSums = scanl' (+) 0
