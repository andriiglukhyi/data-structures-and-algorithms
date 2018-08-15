The analysis of the brute-force pattern-matching algorithm could not be simpler.
It consists of two nested loops, with the outer loop indexing through all possible
starting indices of the pattern in the text, and the inner loop indexing through each
character of the pattern, comparing it to its potentially corresponding character
in the text. Thus, the correctness of the brute-force pattern-matching algorithm
follows immediately from this exhaustive search approach.
The running time of brute-force pattern matching in the worst case is not good,
however, because, for each candidate index in T, we can perform up to m character
comparisons to discover that P does not match T at the current index. Referring to
Code Fragment 13.1, we see that the outer for loop is executed at most n−m+1
times, and the inner while loop is executed at most m times. Thus, the worst-case
running time of the brute-force method is O(nm).