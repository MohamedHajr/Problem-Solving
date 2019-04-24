{-# LANGUAGE FlexibleInstances, UndecidableInstances, DuplicateRecordFields #-}

module Main where

import Control.Monad
import Data.List
import Data.List.Split
import Data.Set
import System.Environment
import System.IO

--
-- Complete the solve function below.
--
solve a0 a1 a2 b0 b1 b2 = do
  print a0
    --
    -- Write your code here.
    --

main :: IO()
main = do
    outputPath <- getEnv "OUTPUT_PATH"
    fptr <- openFile outputPath WriteMode

    a0A1A2Temp <- getLine
    print a0A1A2Temp
    let a0A1A2 = words a0A1A2Temp

    let a0 = read (a0A1A2 !! 0) :: Int

    let a1 = read (a0A1A2 !! 1) :: Int

    let a2 = read (a0A1A2 !! 2) :: Int

    b0B1B2Temp <- getLine
    let b0B1B2 = words b0B1B2Temp

    let b0 = read (b0B1B2 !! 0) :: Int

    let b1 = read (b0B1B2 !! 1) :: Int

    let b2 = read (b0B1B2 !! 2) :: Int

    {-let result = solve a0 a1 a2 b0 b1 b2-}

    {-hPutStrLn fptr $ intercalate " " $ Data.List.map (\x -> show x) $ result-}

    hFlush fptr
    hClose fptr
