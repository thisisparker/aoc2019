## Day 12

Part 1 was a fun opportunity to implement a little `Moon` class and stuff the puzzle into its methods. And it worked pretty well! This was the second time I had to make each object in a list interact with all the other objects in that list, and I used the same pattern of a list comprehension that looks like:
```python
[o for o in objects if o != this_object]
```
which does the job but feels a little clunky!

I also used the `@property` decorator, which I'm trying to get better about using.

I initially started running Part 2 in the same inefficient way, and thought... y'know, if it's in the first few million steps, maybe I can just stumble through this. (It very much was not.) I was lucky to realize that each of the variables are independent, so finding each cycle and then determining the least common multiple would suffice. I definitely had to look up how to find the LCM, but once I dropped that in the problem was basically solved.

I cracked 1000 for the first time on part 2, finishing in 897th place.
