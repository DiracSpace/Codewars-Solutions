module Codewars.Triangles where

import Data.List (sort)

isTriangle :: Int -> Int -> Int -> Bool
isTriangle a b c =
  if ((a + b) > c && (b + c) > a && (a + c) > b)
    then True
  else False
