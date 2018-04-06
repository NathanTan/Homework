------------------------ 
-- HaskellExamples.hs --
------------------------ 

-- Add static numbers --
addStatic = let y = 1+2
                z = 4+6
                in y+z

-- Number Comparison --
-- If Statement      --
lessThanFive num = if num < 5 then True
                   else False
