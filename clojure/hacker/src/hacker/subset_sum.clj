
(defn to_int [line]
   (sort (fn [a b] (- b a))
         (map read-string (clojure.string/split line #" ")))
  )


(defn solution [A s]
  (let [accfn (fn [acc count As]
                (if (>= acc s)
                  count
                  (if (empty? As)
                    -1
                    (recur (+ acc (first As)) (inc count) (rest As)))
                  )
                )]
    (accfn 0 0 A)
    )
  )

;;faster because we already have the sums ready
(defn sol2_sum [line]
  "Used to create a sum array when reading array A first time."
  (let [as (to_int line)
        accfn (fn [acc as last]
                (if (empty? as)
                  acc
                  (recur (conj acc
                           (+ last (first as))
                           )
                         (rest as) (+ last (first as)))
                  )
                )]

    (accfn [] as 0)
    )
  )

(defn solution2 [A s]
  "Uses arrays of sums to find the number of elements"
  (let [index (java.util.Collections/binarySearch A s)]
    (if (>= index 0)
      (inc index)
      (if (> (- index) (count A))
        -1
        (- index)
        )
      )
    )

  )
(defn run-input [input]
  (let [[n A n2 & tests] (line-seq  (clojure.java.io/reader input))]
    (let [as (sol2_sum A)]
      (doseq [t tests]
        (println (solution2 as (read-string t)))
        )
      )
    )
    )


