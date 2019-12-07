## Day 5

Frustrating on a few counts.

- I did day 2 in the REPL, so I had to rewrite all of that from scratch. Not making that mistake again, especially given that I've read this kind of puzzle is one of the most common in AoC.
- Much worse: I'd misinterpreted what the jump commands were supposed to do, and spent a LONG time attempting to find the gap between my interpretation and my implementation, only to much later realize that I had "perfectly" implemented the wrong instruction. (For posterity's sake: I thought "set the instruction pointer to the value from the second parameter" meant to reset the value under the current instruction pointer. It instead means, of course, to change the location of the instruction pointer. You can get that from "jump," but there's enough pointer movement that that wasn't obvious to me.)
- In order to do that debugging, I basically rewrote my intire intcode interpreter from scratch. It's much cleaner now (if still a little loosey-goosey) so if there are more instructions added in the future, I'm ready.
