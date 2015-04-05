(defn solution [line]
  (clojure.string/join "" (doall (distinct (seq line))))
  )

(defn run-input [input]
  (let [line (line-seq  (clojure.java.io/reader input))]
    (println  (solution (first line)))
    ))

(run-input "test.input")