(defn solution [A B]
  (let [am (frequencies A)
        bm (frequencies B)
        diff (fn [a]
               (if (pos? (- (second a) (get am (first a) 0)))
                 (first a)
                 nil
                 )
               )
        ]
    (sort (filter identity (map diff bm)))
    )
  )

(defn to_int [ss]
  (map read-string (clojure.string/split ss #" "))
  )
;; Runner, similar to how HackerRank wraps the solution.
;; Runner, similar to how HackerRank wraps the solution.
 (defn run2 []
           (let [[a A c B] (line-seq  (clojure.java.io/reader "test.input"))]
             (println (clojure.string/join " " (solution (to_int A) (to_int B))))
             )
           )

(defn run []
  (let [[a A c B] (line-seq  (clojure.java.io/reader *in*))]
    (println (clojure.string/join " " (solution (to_int A) (to_int B))))
    )
  )
(run)