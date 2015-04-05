
(defn to_int [line]
        (map read-string (clojure.string/split line #" ")))

(defn gcd [a b]
  (if (> b a)
    (recur b a)
    (if (zero? b)
      a
      (recur b (mod a b))
      )
    )
  )

(defn solution [M L]
  (let [max (gcd M L)]
    (loop [count 1
           n 2]
      (if (<= n max)                  ;
        (if (zero? (mod max n))
          (recur (inc count) (inc n))
          (recur count (inc n))
          )
        count
        )
      )
    )
  )

(defn solution2 [M L]
  (let [MAX (gcd M L)
        divide (fn [max n acc v]
                 (if (> n max)
                   (conj v acc)
                   (if (zero? (mod max n))
                     (recur (/ max n) n (inc acc) v)
                     (recur max (inc n) 1 (conj v acc))
                     )
                   )
                 )
        ]
    (reduce * (divide MAX 2 1 []))
      )
    )


(defn run-input [input]
  (let [[n & T] (line-seq  (clojure.java.io/reader input))]
    (doseq [t T]
      (let [[M L] (to_int t)]
        (println (solution2 M L))
        )
      )
    )
  )



