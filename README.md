# Best_Path_Selector
Best Path Selector

Aim of this simulator is achieving the highest score along the journey to a GoldenPoint A to a GoldenPoint B,
passing through intermediate SilverPoints, each one carrying a nominal score, using path tiles which allow 
the transition through the given grid of places to visit.
Each tile has a cost of use and comes in a fixed number of available items.

Not every tile allows you to move in any direction of the grid, and there are several groups of these aforementioned kinds of tiles. 

The algorithm starts from a Chosen GoldenPoint and proceeds to the next one on the list checking if in the adjacent positions on the grid is located any SilverPoint (max distance check: 2 elements from the current location for every visited location on the grid).