(define (problem hanoi3)
    (:domain hanoi)

    (:objects
        peg1 peg2 peg3 d1 d2 d3
    )

    (:init
        (larger peg1 d1) (larger peg1 d2) (larger peg1 d3) 
        (larger peg2 d1) (larger peg2 d2) (larger peg2 d3)
        (larger peg3 d1) (larger peg3 d2) (larger peg3 d3) 
        (larger d2 d1) (larger d3 d1) (larger d3 d2)
        (clear peg2) (clear peg3) (clear d1)
        (on d3 peg1) (on d2 d3) (on d1 d2)
    )

    (:goal (and
        (on d3 peg3) (on d2 d3) (on d1 d2)
    ))
)