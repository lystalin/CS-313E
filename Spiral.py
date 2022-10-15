#  File: Spiral.py

#  Description: Given an odd number n, we will create a matrix with dimensions n by n filled with each number
#               between 1 and n in a spiral with 1 being at the center. When given a random integer x, if x is within
#               the spiral, we will calculate the sum of every number adjacent to x. If x is not within the
#               spiral, we will return 0.


import sys

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral ( n ):
  input = n
  #Create an empty list for our matrix.
  matrix = []
  #Create a 2-d array with dimensions n by n.
  for row in range(n):
    matrix.append([])
    for col in range(n):
      #Fill with 0s.
      matrix[row].append(0)

  #The end of the spiral (top-right corner) will be n**2.
  two_times = (input ** 2)
  #Create placeholders to be used when traversing through the matrix.
  iterate = 0
  row_count = 0
#  Loop through and fill in values of the matrix one by one in a spiral beginning at two_times until  
#  two_times = 1.We will increase iterate and row_count by 1 to traverse through the columns and rows.
  while two_times >0:
    for i in range(n-1-iterate,-1+iterate,-1):
      matrix[row_count][i] = two_times
      two_times -= 1
    for i in range(1+iterate,n-iterate):
      matrix[i][row_count] = two_times
      two_times -= 1
    for i in range(1+iterate,n-iterate):
      matrix[n-1-iterate][i] = two_times
      two_times -= 1
    for i in range(n-2-iterate,0+iterate,-1):
      matrix[i][n-1-iterate] = two_times
      two_times -=1
    row_count += 1
    iterate += 1
  #Return the finished matrix.
  return matrix  


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):
  length = len(spiral)
  rows = length
  columns = length
  #placeholder for result sum
  summation = 0

  for row in range(rows):
    for col in range(columns):
      if n == spiral[row][col]:
        if row + 1 > length-1:
          summation += 0
        else:
          summation += spiral[row+1][col]
        if row - 1 < 0:
          summation += 0
        else:
          summation += spiral[row-1][col] 
        if col + 1 > length - 1:
          summation += 0
        else:
          summation += spiral[row][col+1]
        if col - 1 < 0:
          summation += 0
        else:
          summation += spiral[row][col-1]
        if row + 1 > length - 1 or col + 1 > length - 1:
          summation += 0
        else:
          summation += spiral[row+1][col+1]
        if row - 1 < 0 or col - 1 < 0:
          summation += 0
        else:
          summation += spiral[row-1][col-1]
        if row + 1 > length - 1 or col - 1 < 0:
          summation += 0
        else:
          summation += spiral[row+1][col-1]
        if row - 1 < 0 or col + 1 > length - 1:
          summation += 0
        else:
          summation += spiral[row-1][col+1]
  return summation
      

def main():
  # Read the input file.
  dimension = sys.stdin.readline()
  dimension = dimension.strip()
  # Create the spiral.
  spiral = create_spiral(int(dimension))
  # Add the adjacent numbers.
  for num in sys.stdin:
    num = num.strip()
  # Print the result.
    result = sum_adjacent_numbers(spiral,int(num))
    if int(num) > int(dimension) ** 2:
      print(0)
    else:
      print(result)
  
  

if __name__ == "__main__":
  main()
