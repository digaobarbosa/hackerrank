
(defn solution [matrix M N R]

  (let [a
        ])
  (for [x (range M)
        y (range N)]
    (let [value (get (get matrix x) y)]
      [[y x] value]
      )
    )
  )

(defn read-matrix [lines]
  (vec (map (fn [line]
              (vec (map read-string (clojure.string/split line #" ")))
              ) lines))
  )

(defn run-input [input]
  (let [rdr (line-seq (clojure.java.io/reader input))]
    (let [[M N R] (map read-string (clojure.string/split (first rdr) #" " ))
          mms (rest rdr)]
      (solution (read-matrix mms) M N R)
      )
    )
  )



