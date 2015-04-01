(defn solution [P Q]
  "Solution for https://www.hackerrank.com/challenges/string-mingling"
  (let [sb (new StringBuilder)]
    (doseq [i (range (count P))]
      (.append sb (str (nth P i) (nth Q i) ))
      )
    (str sb)
    )
  )


;; Runner, similar to how HackerRank wraps the solution.
(defn run [] (let [[in1 in2 & more]  (line-seq (java.io.BufferedReader. *in*))]
               (println (solution in1 in2))
               ))

(run)

