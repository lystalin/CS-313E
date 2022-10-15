#  File: Tower.py

#  Description: "Tower of Hanoi" is a puzzle in which a player has 8 disks of different radii placed
#               on one of three pegs with the largest disk at the bottom and the rest of the disks placed
#               on top in descending size. The goal of the puzzle was to move all 8 disks to the third peg
#               with only two rules: only one disk could be moved at a time and at no time could there be a
#               disk of a larger size on top of a disk of a smaller size. In this assignment, we have mimicked
#               the "Tower of Hanoi" puzzle with 4 pegs and n number of disks. We have recursively calculated
#               the minimum number of moves it would take to move all n pegs to the fourth peg while following
#               the two rules of the puzzle.

#  Student Name: Colleen Miller

#  Student UT EID: cem4948

#  Partner Name: Jazmin

#  Partner UT EID: jr68648

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/10/2022

#  Date Last Modified:
import sys
import math

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  else:
    k = round(n - math.sqrt(2 * n + 1) + 1)
    return num_moves(k) + 2**(n-k-1) -1 + 1 + 2**(n-k-1) -1 + num_moves(k)
# First move the topmost disks (say the top k disks) to one of the spare needles, say spare1.
# Then move n - k - 1 disks to spare2.
# Move the largest disk from source to destination.
# Move the n - k - 1 disks from spare2 to destination.
# Finally, move the top k disks from spare1 to destination.


def main():
  # read number of disks and print number of moves
  for line in sys.stdin:
    line = line.strip()
    num_disks = int (line)
    print (num_moves (num_disks))

if __name__ == "__main__":
  main()