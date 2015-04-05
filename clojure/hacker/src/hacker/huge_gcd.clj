(defn gcd [a b]
  (if (< a b)
      (recur b a)
      (if (= b 0)
        a
        (recur b (mod a b))
        )
      )
  )

(defn solution1 [A B]
  (let [mult (fn [a b] (* a b))]
    (gcd (reduce mult A) (reduce mult B))
    )
  )
(def MOD 1000000007)

(defn solution2 [A B]
  (let [mult (fn [a b]  (* a b))]
    (mod (gcd (reduce mult A) (reduce mult B)) MOD)
    )
  )



(defn to_int [line]
  (map bigint (clojure.string/split line #" "))
  )

(defn run-input [input]
  (let [[n A _ B] (line-seq  (clojure.java.io/reader input))]
    (println  (biginteger (solution2 (to_int A) (to_int B))))
    ))


