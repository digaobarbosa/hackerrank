(use '[clojure.string :as s])

(defn solution [STR]
  "Manual solution"
  (loop [res "" line STR]
    (if (empty? line)
      res
      (let [c (subs line 0 1)]
          (recur (str res c) (s/replace line c ""))
        )
      )
    )
  )


(defn sol2 [STR]
  "It seems to work as distinct returns the same order as letters appears."
  (s/join (distinct STR))
  )

(defn run-input [input]
  (doseq [line (line-seq  (clojure.java.io/reader input))]
    (println (sol2 line))
    )
  )