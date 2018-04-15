module Test  where

myWords :: String -> [String]
myWords s = go s [] 
  where go "" res = res
        go x res  = go dropped taken
          where dropped = drop 1 $ dropWhile (/= ' ') x
                taken   = (++) res . (:[]) $ takeWhile (/= ' ') x
