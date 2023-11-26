-- | A simple wrapper around ReadP to make it more convenient to use.
module Parsing (
  Parser,
  parse,
  unsigned,
  signed,
  space,
  spaces,
  newline,
  -- | re-exports
  module Text.ParserCombinators.ReadP,
  module Control.Monad,
  module Data.Functor,
  module Control.Applicative,
)
where

import Control.Applicative ((<|>))
import Control.Monad
import Data.Char (isDigit)
import Data.Functor
import Text.ParserCombinators.ReadP

type Parser = ReadP

parse :: Parser a -> String -> a
parse p input = head do
  (x, input') <- readP_to_S p input
  guard (null input')
  pure x

unsigned :: Parser Int
unsigned = read <$> munch isDigit

signed :: Parser Int
signed = do
  sign <- option '+' (char '-')
  n <- unsigned
  pure if sign == '-' then -n else n

space :: Parser ()
space = void $ char ' '

spaces :: Parser ()
spaces = void $ many space

newline :: Parser ()
newline = void $ char '\n'
