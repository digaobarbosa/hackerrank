(ns hacker.string-rotation)

(defn solution [line]
  "Teste do all"
  (letfn [(f [start]
             (clojure.string/join (doall (take (count line) (drop start (cycle line)))))
             )]
    (clojure.string/join " " (map f (range 1 (inc (count line)))))
    )
  )



;; Runner, similar to how HackerRank wraps the solution.
;; Runner, similar to how HackerRank wraps the solution.
(defn run [] (let [lines (rest (line-seq (java.io.BufferedReader. *in*)))]
               (doseq [n lines]
                 (println (solution n)))
               ))

(run)
