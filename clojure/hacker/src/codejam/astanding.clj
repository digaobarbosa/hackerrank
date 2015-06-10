(defn solution [audience]
  (loop [aud audience
         Si 0
         acc 0
         toadd 0
         ]
    (if (empty? aud)
      toadd
      (if (or (>= acc Si) (zero? (first aud)))
        (recur (rest aud) (inc Si) (+ acc (first aud)) toadd)
        (recur (rest aud) (inc Si) (+ Si (first aud)) (+ toadd (- Si acc) ))
        )
      )
    )

  )

(def C 0)

(defn parse-input [line]
  (let [[a b] (clojure.string/split line #" ")]
    (def C (inc C))
    [C (map read-string (clojure.string/split b #""))]
    )
  )

(defn run-input [input]
  (with-open [writer (clojure.java.io/writer "output.txt")]

  (doseq [line (rest (line-seq  (clojure.java.io/reader input)))]
    (let [[C line] (parse-input line)]
      (.write writer (str "Case #" C ": " (solution line) "\n"))
      )
    )
  )
  )