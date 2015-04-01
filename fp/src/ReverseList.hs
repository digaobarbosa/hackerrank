module ReverseList where
rev [] = []
rev l = last l : init l

