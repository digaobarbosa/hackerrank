(defn solution [K numbers]
  (let [ OK (set (->> numbers (frequencies) (filter #(>= (val %) K)) (map first)))]
    (filter OK (distinct numbers))
    )
  )

(defn to_int [ss]
  (map read-string (clojure.string/split ss #" "))
  )

(defn run-input [input]
  (doseq [[line1 line2]  (partition 2 (rest (line-seq (clojure.java.io/reader input))))]
         (let [res (solution (second (to_int line1)) (to_int line2))]
           (if (empty? res)
             (println -1)
             (println (clojure.string/join " " res))
             )
           )
         ))

(run-input "test.input")