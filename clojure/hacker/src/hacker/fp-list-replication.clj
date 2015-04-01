(ns hacker.fp-list-replication
    (:gen-class))
 "Solution for https://www.hackerrank.com/domains/fp/intro"
(fn ! [n l] (concat (repeat n (first l))
                    (if (empty? (rest l)) [] (! n (rest l)) )))