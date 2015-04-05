(use '[clojure.string :as s])

(defn to_set [line]
   (map read-string (s/split line #" ")))


(defn sol [lines]
  (let [facts (partition 2 (flatten (map to_set lines)))
        min_count (count lines)
        redfn2 (fn [M v]
                 "returns a list with pairs of factors"
                 (let [key (first v) val (second v)]
                   (assoc M key (conj (get M key []) val))
                   )
                 )
        ]
    (map (fn [a] [(first a) (apply min (second a))])
         (filter #(= (count (second %)) min_count)
                                         (reduce redfn2 (sorted-map) facts)))
    )
  )
(defn print_sol [lines]
  (println (s/join " " (flatten (sol lines))))
  )



(defn run-input [input]
  (let [lines (rest (line-seq  (clojure.java.io/reader input)))]
    (print_sol lines)
    )
  )
