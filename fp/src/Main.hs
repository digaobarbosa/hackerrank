module Main where

factorial 0 = 1
factorial n = n*(factorial (n-1))
solve n = factorial n

main = do
    val1 <- readLn :: IO Int
    let sum = solve val1
    print sum
