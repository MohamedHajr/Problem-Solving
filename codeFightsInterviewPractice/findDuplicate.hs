module Findduplicate (module Findduplicate) where

import Data.Vector

findFirstDuplicate :: [Int] -> Int -> Int
findFirstDuplicate [] _ = -1
findFirstDuplicate xs index 
  | xs !! index > 0 = findFirstDuplicate (updateList xs (xs !! abs (xs !! index)) (xs) ) index + 1
  | otherwise =  -1
 
updateList 