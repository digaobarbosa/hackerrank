
(defn fib [n]
  (if (= 1 n)
    0
    (if (= 2 n)
      1
      (+ (fib (- n 1)) (fib (- n 2)))))
  )


(defn fib2 [n]
  (letfn [(f [a i1 i2]
             (if (= 1 a) i1
                 (recur (dec a) i2 (+ i1 i2))))]
           (f n 0 1)
           )
  )

;; Runner, similar to how HackerRank wraps the solution.
(defn run [] (
   let [lines (line-seq (java.io.BufferedReader. *in*))]
                       (doseq [n (map #(Integer/parseInt %) lines)]
                         (println (fib2 n)))
))

