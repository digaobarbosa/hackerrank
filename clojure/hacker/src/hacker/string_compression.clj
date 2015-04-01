(defn solution [line]
  (let [sb (new StringBuilder)]
    (letfn [
            (to_str [letter count]
                    (.append sb (if (= count 1)
                                  letter
                                  (str letter count))))

            (f [res count input]
               (if (empty? input)
                 (to_str res count)          ;if count>1 adds numbers
                 (if (= res (first input))
                   (recur res (inc count) (rest input))      ;
                   (do
                     (to_str res count)
                     (recur (first input) 1 (rest input)
                       ))
                   )
                 )
               )]
      (f "" 1 line)
      (str sb)
      )
    )
  )


;; Runner, similar to how HackerRank wraps the solution.
(defn run [] (let [lines  (line-seq (java.io.BufferedReader. *in*))]
               (doseq [n lines]
                 (println (solution n)))
               ))

(run)

