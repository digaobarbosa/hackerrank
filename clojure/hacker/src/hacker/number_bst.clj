(use '[clojure.string :as s])

(defn to_int [line]
  (map read-string (s/split line #" ")))

(def cache {})


(defn sol [N]
  (if (contains? cache N)
    (get cache N)
    (if (zero? N)
      0
      (if (= N 1)
        1
        (do (def cache (assoc cache N (reduce +
                                              (for [x (range 0 N)]
                                                (if (or (zero? x) (= N x))
                                                  0
                                                  (* (sol x) (sol (- N x)))
                                                  )
                                                ))
                                    ))
            (get cache N))
        )
      )
    ))
(def sol2 (memoize sol))


(defn run-input [input]
  (let [N (map read-string (rest (line-seq (clojure.java.io/reader input))))]
    (sol N)
    )
  )
