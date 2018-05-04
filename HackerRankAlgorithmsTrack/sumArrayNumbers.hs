{-# LANGUAGE FlexibleInstances, UndecidableInstances, DuplicateRecordFields #-}

module Main where

import Control.Monad
import Data.List
---import Data.List.Split
import Data.Set
import System.Environment
import System.IO


--
-- Complete the simpleArraySum function below.
--
mySum :: Num a => [a] -> a
mySum [] = 0
mySum (x : xs) = x + sum xs


readMultipleLinesAsStringArray :: Int -> IO [String]
readMultipleLinesAsStringArray 0 = return []
readMultipleLinesAsStringArray n = do
    line <- getLine
    rest <- readMultipleLinesAsStringArray(n - 1)
    return (line : rest)

main :: IO()
main = do
    stdout <- getEnv "OUTPUT_PATH"
    fptr <- openFile stdout WriteMode

    arCount <- readLn :: IO Int

    arTemp <- getLine

    let ar = Data.List.map (read :: String -> Int) . words $ arTemp

    let result = sum ar

    hPutStrLn fptr $ show result

    hFlush fptr
    hClose fptr


