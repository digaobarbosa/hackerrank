(use '[clojure.string :as s])


(defn parse-int [s]
  (Integer/parseInt s ))

(def MOD 1000000007)

(def gcd
  (memoize (fn [a b]
             (if (zero? b)
               a
               (gcd b (mod a b)))))
  )

(defn lcm
  [a b]
  (/ (* a b) (gcd a b)))
;; to calculate the lcm for a variable number of arguments
(defn lcmv [v]  (reduce lcm v) )

(defn query [A l r]
  (let [As (subvec A l (inc r))]
    (println (str (mod (lcmv As) MOD)))
    )
  )

(defn sol [A T]
  (if (seq T)
    (let [[c l r] (s/split (first T) #" ")]
      (if (= c "U")
        (let [idx (parse-int l)
              v (bigint r)
              ]
          (recur (assoc A idx (* v (nth A idx))) (rest T))
          )
        (do
          (query A (parse-int l) (parse-int r))
          (recur A (rest T))
          )
        )
      )
    )
  )



(defn run-input [input]
  (let [[_a _t & T] (rest (line-seq  (clojure.java.io/reader input)))]
    (let [As (map bigint (s/split _a #" "))]
      (sol (vec As) T)
      )
    )
  )
