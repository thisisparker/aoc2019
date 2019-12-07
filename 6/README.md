## Day 6

A nice straightforward one. I thought about trying to actually implement some kind of tree or network data structure, but I didn't have a tool handy to do that readily, so I came up with something on the fly that ended up working nicely.

Each object directly orbits exactly one other object, all the way down to a Center Of Mass. So I made a dictionary where each key is one such object, and each value is an ordered list of those orbits, all the way down to the center.

To calculate the number of direct and indirect orbits was just summing the length of each of those lists. Then I lucked out, because my data structure made it easy to calculate the number of hops between orbits too: it's just the sum of the indexes of the first common object between the two.
