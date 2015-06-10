(defn solution [numbers]
  (let [ OK (set (->> numbers (frequencies) (filter #(>= (val %) K)) (map first)))]
    (filter OK (distinct numbers))
    )
  )

(defn to_int [ss]
  (map read-string (clojure.string/split ss #" "))
  )

(defn run-input [input]
  (let [[N K] (clojure.string/split (first (line-seq (clojure.java.io/reader input))) " ")]
    (println N K)

    ))

(run-input "test.input")