Introduction

The problem statement involves designing a CSP algorithm to solve a tile placement problem on a given landscape with different colored bushes. The problem requires finding a suitable tile placement configuration that satisfies a given target condition of visible bushes. The problem aims to develop an efficient algorithm using heuristics, search algorithms, and constraint propagation to solve the problem.

Problem Definition

The problem involves fitting 3 different shapes of tiles, namely L-shape, outer block, and full block, onto a grid with specific target values for each color. The aim is to find a configuration of tiles that satisfies all the target values while considering the number of tiles used. The problem can be formulated as a CSP, where the variables are the tiles' shapes and locations, the domains are the possible values for each variable, and the constraints are the target values for each color.

Algorithm

The algorithm implemented for solving the problem is a backtracking search algorithm. It traverses the search space and tries to assign each variable a value that satisfies the constraints. The algorithm incorporates several techniques to improve its efficiency, such as Minimum Remaining Value (MRV) heuristic for selecting the next variable to assign, and Forward Checking for pruning the search space by removing values that would violate the constraints. Additionally, it uses Least Constraining Value (LCV) heuristic for selecting the values to assign to a variable that will leave the maximum number of choices for the remaining variables.
