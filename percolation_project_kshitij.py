# -*- coding: utf-8 -*-
"""Percolation Project: Kshitij

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1te78oogJyO8si7A0bHbCwmYP7_0bPUQ_

# Percolation Project
### Kshitij Gurung, May 01, 2020

We have been examining the 2-D percolation problem in which we have a n × n grid of squares.
Each square is either “open” with probability p or “closed” with probability 1 − p. We say that
percolation occurs if there is a path of open squares from any square in the top row to any square
in the bottom row of the grid.

In this project we try to understand how the probability for percolation happening depends on the grid size 'n' and the probability that a square is open 'p'.

Import some necessary variables
"""

import random
 import numpy
 import matplotlib.pyplot as plt

"""Define variables:

- n: the number of rows and columns in the grid

- p: probability that a square is "open"

### Data Structures: Setting up the Grids
- First, we need to define a data structure for the  𝑛×𝑛  grid. We can use a NumPy array filled with 0 and 1 values. Let a 0 signify "closed" and a 1 signify "open." 
- We will define a funciton that takes n and p and make a grid.
- Second, we also need a n * n grid that marks the locations that are visited during perculatino.

This makegrid function takes in n and p and makes a n * n grid with p probability for the gates.
"""

# Setting up grid with n=10 and p = 0.5
def makegrid(n,p):
  grid = numpy.random.choice( [0,1], p=[1-p,p], size=(n,n) )
  return grid

"""Testing the makegrid function."""

print(makegrid(10,0.6))

"""# The Algorithm: Detecting Percolation
We need to determine whether there exists a path of open cells from the top to the bottom of the grid.

Suppose that you are searching for a path. You might visit squares in the grid, asking the following questions at each square:

⮕ Am I on the bottom row?

- If yes, then I have found a percolation path.
- If no, then is there a path from any adjacent, unvisited, open cell to the bottom row? ✱

To answer the question marked with ✱, you could check each of the four adjacent square. For any adjacent square that is unvisited and open, you could just proceed from that square, asking the question marked with ⮕.

This leads us to a recursive function: a function that calls itself. In other words, we want to write a function findPath() that tells us whether a path exists from any given square to the bottom row of the grid. If the given square is not on the bottom row, then find path will check each of its neighbors, calling itself to determine whether a path exists from any neighbor of the given square. When there is a porculation if found, it raises an exception.

findpath function takes in a location (row, column), visited (grid to mark the visited locations), and grid ( the actual percolation grid).
"""

# function findPath()
# Determines whether a path exists from (row, col) to the bottom of the grid.
# Assume that the grid of squares is already defined.
# Requires a 2D array that remembers which squares have already been visited.
def findPath(row, col, visited, grid):
  
  #print("visiting row ", row, ", column ", col) # this will help with testing
  
  # mark (row, col) as visited
  visited[row, col] = 1
  n = len(visited)

  # if row is the bottom row, then output "path found"
  if (row == n-1):
    raise percolationFound # raises exeption

  # otherwise:
  else: 
    # is there a path from the cell to the left?
    if (col-1 >= 0):
      if (grid[row, col-1]==1) and (visited[row, col-1]==0):
        # print("  going left from (", row, ",", col,")")
        findPath(row, col-1,visited, grid )

    # is there a path from the cell below?
    if grid[row+1, col]==1 and (visited[row+1, col]==0):
      # print("  going down from (", row, ",", col,")")
      findPath(row+1, col, visited, grid)

    # is there a path from the cell to the right?
    if (col+1) < n:
      if grid[row, col+1]==1 and (visited[row, col+1]==0):
        # print("  going right from (", row, ",", col,")")
        findPath(row, col+1,visited, grid)

    # is there a path from the cell above?
    if (row-1 >= 0) and (visited[row-1, col]==0):
      if grid[row-1, col]==1:
        #print("  going up from (", row, ",", col,")")
        findPath(row-1, col,visited, grid)

"""Let's define a function that uses a try and catch module and runs a for loop to test for percolation from each box on top. It calls findpath function to check for the porcolation."""

# define an exception that will be raised if percolation occurs
class percolationFound(Exception): pass

# Function to find percolation
# Requires that the grid of squares is already defined as a global variable.
def findPercolation(n,p):
  # initialize the visited data structure
  visited = numpy.zeros((n,n), dtype=int)
  
  # Makes a new grid 
  grid = makegrid(n,p)
  try:
    for c in range(n): # loop over columns in grid
      if grid[0,c] == 1:
        findPath(0, c, visited, grid) # start search from row 0, column c
  except percolationFound:
    #print("percolation found! Starting index [0,", c,']')
    return True
  else:
    #print("no percolation")
    return False

"""Let's test out function by passing the parameters for grid (n and p)."""

print(findPercolation(10,0.8))
print(findPercolation(12,0.65))

"""Looks like our function is working well.

## Your Task
How does the probability of percolation depend on p when n = 10? Find the
probability of percolation for various values of p. Make a plot showing how the probability
of percolation depends on p.

First, let's find the probability of percolation for p = 0.5, and n = 10. We use 10000 iteration and average them to find the probability.
"""

percu = [findPercolation(10, 0.5) for i in range(10000)]
print(percu)
numpy.mean(percu)

"""Turns out it has around 0.17 probability for percolation in average.

Define a percoProb function that takes in n, p, and ite( how many iteration to perform for finding the average).
"""

def percoProb(n,p,ite):
  percu = [findPercolation(n, p) for i in range(ite)]
  return(numpy.mean(percu))

percoProb(10,0.5,5000)

"""Let's calcuate the probabilites associated with different p values, a fixed n value of 10 and visualize the plot."""

probrange =[k/100 for k in range(0,110,10)]
prob = [percoProb(10,k/100,10000) for k in range(0,110,10)]

plt.plot(probrange, prob)
plt.title('Percolation probability vs p vlaues (n : 10)')
plt.xlabel('P values')
plt.ylabel('Porculation Probability');

"""As seen in the plot, the porculation probability increases as the p value for the grid increases. The relation is not exactly linear but somewhat like a s shaped. The probability is almost zero before p: 0.4, and it shoots up high and remains around 100% from p : 0.8 onwards.

2. How does the probability of percolation depend on p when n = 40? Find the
probability of percolation for various values of p. Make a plot showing how this probability
depends on p.

Running the same this as before with n value of 40.
"""

probrange =[k/100 for k in range(0,110,10)]
# calculation percolation probabilities for n = 40/
prob40 = [percoProb(40,k/100,1000) for k in range(0,110,10)]
# making plot
plt.plot(probrange, prob40)
plt.title('Percolation probability vs p vlaues (n : 40)')
plt.xlabel('P values')
plt.ylabel('Porculation Probability');

"""I personally thought the percolation peobability for smaller p values would increases for n :40, but turns out it is the opposite. The graph shifted right, with a even more strict jump in probability from p value 0.6 to 0.75. The porculation probability seems to increase only after the p values gets bigger than 0.5.

3. How does the probability of percolation depend on n when p = 0.55? Find the
probability of percolation for various values of n. Make a plot showing how this probability
depends on n.

Let's run the function with p: 0.55 on a range of n values and visualize the plot.
"""

probN = [percoProb(n, 0.55 ,500) for n in range(2, 101)]
# making plot
plt.plot(range(2,101), probN)
plt.title('Percolation probability vs N grid size (p : 0.55)')
plt.xlabel('N values')
plt.ylabel('Porculation Probability');

"""As the grid size (n) increases the percolation probability  decreases for fixed p vlaue of 0.55. This is counterintuitive to my initial thought because I guessed a bigger grid size would have more propability of percolation happening. The probability saturates to 0 around n value of 100.

4. How does the probability of percolation depend on n when p = 0.65? Find the
probability of percolation for various values of n. Make a plot showing how this probability
depends on n.

Running the same thing as question 3 but with p value of 0.65 and visualizing the plot.
"""

import sys
sys.setrecursionlimit(4000)

probN = [percoProb(n, 0.65 ,100) for n in range(2, 101)]
# making plot
plt.plot(range(2,101), probN)
plt.title('Percolation probability vs N grid size (p : 0.65)')
plt.xlabel('N values')
plt.ylabel('Porculation Probability');

"""Interestingly enough, as the n value increasese (p : 65) the porculation probability increases too, which is opposite to the previous case where p was 0.55. The graph looks like a square root function with probability saturating at 1 aroung n = 60.

# Conclusion
- Given that n is constant, p value is directly related to percolation probability. As the p value goes high, probability of percolation also increasese. It follows a 'S' shaped curve and the curve gets more stiff and abrupt as the n value increases. 
- There is a very interesting relationship between fixed p value and n value. For fixed p values smaller than around 0.60 the percolation probability decreases as n increases. However, for fixed p value greater than around 0.60, the percolation probability increases as the n increases. 

# Limitation and future work
- We would often see “maximum recursion depth exceeded” error. We could investigate further if we had a more powerful computer and codebase that could handle a lot of recursions.  
- We could not observer or understand why fixed p and n have such an interesting relationship. 
- I feel like there could be a sweet spot for p value where the probability of perculation in constant no matter the increases in n size. We did not study that.
- I am also interested in finding why there is such a strict and abrupt change in the percolation probability between 0.40 to 0.60 range. The distinction is even more abrupt as the n value increases, which is very interesting and counterintuitive to my initial guess. 
- I might actaully work on these future work and limitations as a part of extra project.
"""