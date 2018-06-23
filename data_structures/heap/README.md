#### A heap is a binary tree T that stores a collection of items at its
positions and that satisfies two additional properties: a relational property defined
in terms of the way keys are stored in T and a structural property defined in terms
of the shape of T itself. The relational property is the following:

### Heap-Order Property: In a heap T , for every position p other than the root, the
key stored at p is greater than or equal to the key stored at p’s parent.
As a consequence of the heap-order property, the keys encountered on a path from
the root to a leaf of T are in nondecreasing order. Also, a minimum key is always
stored at the root of T . This makes it easy to locate such an item when min or
remove min is called, as it is informally said to be “at the top of the heap” (hence,
the name “heap” for the data structure). By the way, the heap data structure defined
here has nothing to do with the memory heap used in the run-time
environment supporting a programming language like Python.

### Complete Binary Tree Property: A heap T with height h is a complete binary tree
if levels 0, 1, 2, . . . , h − 1 of T have the maximum number of nodes possible
(namely, level i has 2 i nodes, for 0 ≤ i ≤ h − 1) and the remaining nodes at
level h reside in the leftmost possible positions at that level.
