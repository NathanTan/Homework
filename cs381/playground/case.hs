



--fucn (Maybe 4)
--func (Just (4))
--func (Nothing)


func :: Maybe Int -> Int
func i = case i of
        Just x -> x
        Nothing -> 0

