
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

(def MOD 100000007)

(defn fib3 [n]
  (letfn [(f [a i1 i2]
             (if (= 0 a) i1
                         (recur (dec a) i2 (mod (+ i1 i2) MOD))))]
    (f n 0 1)
    )
  )

(defn fib4 [n]
  (if (zero? n)
    0
    (if (= 1 n)
      1
      (mod (+ (fib4 (dec n)) (fib4 (- n 2))) MOD)
      )
    )
  )
(def fib4 (memoize fib4))

(def fib5 (memoize (fn [x] (if (< x 2)
                            x
                            (mod (+ (fib5 (- x 1))
                                    (fib5 (- x 2))) MOD)))))



(defn run-input [input]
  (doseq [K (rest (line-seq  (clojure.java.io/reader input)))]
    (println (fib5 (read-string K)))
    )
  )