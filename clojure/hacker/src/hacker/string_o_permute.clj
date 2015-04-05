

(defn solution [str]
  (clojure.string/join
    (if (empty? str)
      []
      (concat
        (list (second str) (first str))
        (solution (rest (rest str))))))
  )


(defn sol2 [s]
  (let [sb (new StringBuilder)]
    (loop [x s]
      (if (empty? x)
        (str sb)
        (do
          (.append sb (str (second x) (first x)) )
          (recur (subs x 2))
          )
      )
    )

  ))

(defn sol3 [s]
  (clojure.string/join (flatten (map #(reverse %) (partition 2 s))))
  )
;; Runner, similar to how HackerRank wraps the solution.
(defn run [] (let [lines (rest (line-seq (java.io.BufferedReader. *in*)))]
               (doseq [n lines]
                 (println (sol3 n)))
               ))


