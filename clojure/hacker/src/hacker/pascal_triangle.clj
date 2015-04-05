
(defn fact [n]
  (let [acfn (fn [acc i]
               (if (<= i 1)
                  acc
                 (recur (* i acc) (dec i)))
               )]
    (acfn 1 n)
    )

  )
(def mfact (memoize fact))

(defn pascal [K]
  (doseq [row (range K)]
    (doseq [col (range (inc row))]
      (print (/ (mfact row) (* (mfact col) (mfact (- row col)))) "")
      )
    (println)
    )
  )


(defn run-input [input]
  (doseq [K (line-seq  (clojure.java.io/reader input))]
    (pascal (read-string K))
    )
 )



