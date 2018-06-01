{-# LANGUAGE FlexibleInstances, UndecidableInstances, DuplicateRecordFields #-}

module Main where

import Data.List ()


--
-- Complete the simpleArraySum function below.
--
main :: IO()
main = interact $ show . sum . map read . words
