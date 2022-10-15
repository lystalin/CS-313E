#  File: Triangle.py

#  Description: #  Description: We have taken several approaches into solving a variation of a problem from project Euler. Given an input with the first
#               line n representing n number of rows, followed by n number of lines, we are able to construct a grid representing a triangle. 
#               Using 4 different algorithms such as brute force, dynamic programming, divide and conquer, and greedy algorithm, we have 
#               calculated the greatest path sum beginning at the top of the triangle and only summing numbers adjacent in the row below. 
#               The brute force and divide and conquer methods are recursive approaches.


#  Student Name: Colleen Miller

#  Student UT EID: cem4948

#  Partner Name: Jazmin Reyna

#  Partner UT EID: jr68648

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/8/2022

#  Date Last Modified: 10/10/2022

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid): 
  # helper function has initial x, initial y, empty list, the grid, and 0 points as parameters
  return brute_helper(0,0, [], grid, 0)

def brute_helper(x, y, value_lst, grid, points):
  if x == len(grid):
    # add the paths value to the list
    value_lst.append(points)
    points = 0
    if len(value_lst) == 2**len(grid)-1:
      # find maximum path in list
      return max(value_lst)
  else:
    # iterate through paths
    return brute_helper(x+1, y, value_lst, grid, grid[x][y] + points) or brute_helper(x+1, y+1, value_lst, grid, grid[x][y] + points)

# returns the greatest path sum using greedy approach
def greedy (grid):
  #need to sum the initial grid center
  sum = grid[0][0]
  #need to go to next row and compare the two next to eachother
  #left is in same column, right is one to the right
  #so it would be [row + 1][col] and [row + 1][col + 1]
  #for loop until we get to the bottom row
  #establish initial column because it will be changing inside for loop
  col = 0
  for row in range(0, len(grid)-1):
    left = grid[row + 1][col]
    right = grid[row + 1][col + 1]
    #check which is optimal in this comparison
    if left > right:
      sum += left
      #column does not change
    if right > left:
      sum += right
      #we are now one column to the right
      col += 1

  return sum

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  # helper function takes the x and y positions, the grid, and an empty points holder
  return div_helper(0, 0, grid, 0)

def div_helper(x, y, grid, points):
  # if x reaches the end of the grid, return the points
  if x >= len(grid):
    return points
  else:
    # points is the new path number + old path points
    points = grid[x][y] + points
    left = div_helper(x+1, y, grid, points)
    right = div_helper(x+1, y+1, grid, points)
    # return the max path between the left and the right path
    return max(left, right)
  

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  #we will be changing the triangle, so we want to make a copy so that we are not acyually changing the 
  #original triangle and instead changing a copy
  new_grid = grid
  x = 0
  for row in range(len(new_grid)-1,0,-1):
    for col in range(len(new_grid)-1-x):
      if new_grid[row][col] > new_grid[row][col + 1]:
        new_grid[row-1][col] += new_grid[row][col]
      else:
        new_grid[row-1][col] += new_grid[row][col+1]
    x += 1
  return new_grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()