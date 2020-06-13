# Percolation Project
### Kshitij Gurung, May 01, 2020

We have been examining the 2-D percolation problem in which we have a n × n grid of squares.
Each square is either “open” with probability p or “closed” with probability 1 − p. We say that
percolation occurs if there is a path of open squares from any square in the top row to any square
in the bottom row of the grid.

In this project we try to understand how the probability for percolation happening depends on the grid size 'n' and the probability that a square is open 'p'.

Define variables:

- n: the number of rows and columns in the grid

- p: probability that a square is "open"

### Data Structures: Setting up the Grids
- First, we need to define a data structure for the  𝑛×𝑛  grid. We can use a NumPy array filled with 0 and 1 values. Let a 0 signify "closed" and a 1 signify "open." 
- We will define a funciton that takes n and p and make a grid.
- Second, we also need a n * n grid that marks the locations that are visited during perculatino.

**The Algorithm: Detecting Percolation**

We need to determine whether there exists a path of open cells from the top to the bottom of the grid.

Suppose that you are searching for a path. You might visit squares in the grid, asking the following questions at each square:

⮕ Am I on the bottom row?

- If yes, then I have found a percolation path.
- If no, then is there a path from any adjacent, unvisited, open cell to the bottom row? ✱

To answer the question marked with ✱, you could check each of the four adjacent square. For any adjacent square that is unvisited and open, you could just proceed from that square, asking the question marked with ⮕.

This leads us to a recursive function: a function that calls itself. In other words, we want to write a function findPath() that tells us whether a path exists from any given square to the bottom row of the grid. If the given square is not on the bottom row, then find path will check each of its neighbors, calling itself to determine whether a path exists from any neighbor of the given square. When there is a porculation if found, it raises an exception.
findpath function takes in a location (row, column), visited (grid to mark the visited locations), and grid ( the actual percolation grid).

## I attempt to investigate the following questions:

1) How does the probability of percolation depend on p when n = 10? Find the
probability of percolation for various values of p. Make a plot showing how the probability
of percolation depends on p.

2) How does the probability of percolation depend on p when n = 40? Find the probability of percolation for 
various values of p. Make a plot showing how this probability depends on p.

3) How does the probability of percolation depend on n when p = 0.55? Find the probability of percolation for various values of n. Make a plot showing how this probability depends on n.

4) How does the probability of percolation depend on n when p = 0.65? Find the probability of percolation for various values of n. Make a plot showing how this probability depends on n.

5) Conclusion, Limitation, and Future work
