(use '[clojure.string :as s])

(defn solution [store pass]
    (let [totalp (re-pattern (str "(" (s/join "|" store) ")+"))
          patp (re-pattern (str "(" (s/join "|" (map #(str "(" % ")") store)) ")+"))
          ]
      (if (re-matches totalp pass)
        "OK"
        "WRONG PASSWORD"
        )
      )
  )

(defn sol2 [STORE pass]
  (let [accfn (fn [result store pass]
                (let [word (first store)]
                  (if (empty? pass)                         ;already found
                    result
                    (if word
                      (if (.startsWith pass word)
                        (recur (conj result word) STORE (subs pass (count word)) ) ;adds word to result and search ending str
                        (recur result (rest store) pass)    ;tries next word on store with same pass
                        )
                      nil                                   ;if theres no word, wrong pasword
                      )
                    )
                  )
                )]
    (let [res (accfn [] STORE pass)]
      (if res
        (s/join " " res)
        "WRONG PASSWORD"
        )
      )
    )
  )

(defn run-input [input]
  (loop [file (rest (line-seq  (clojure.java.io/reader input)))]
    (let [
          [n storeWords pass] (take 3 file)
          ]
      (if n
        (do
          (println (sol2 (s/split storeWords #" ") pass))
          (recur (nthrest file 3))
          )

        )
      )
    )
  )