#  File: Intervals.py

#  Description: 

#  Student Name: Colleen Miller

#  Student UT EID: cem4948

#  Partner Name: Jazmin Reyna

#  Partner UT EID: jr68648

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/7/2022

#  Date Last Modified: 

import sys

def tuples(pair):
    split = pair.split()

    main_tuple = ()
    for num in split:
        num = int(num)
        num_tuple = (num,)
        main_tuple += num_tuple
    return main_tuple

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):
  tuples_list.sort()

  tup_list = []
  for i in tuples_list:
    tup_list.append(list(i))

  merge_lst = []
  stored = tup_list[0]

  for i in range(len(tup_list)):
    if tup_list[i][0] <= stored[1]:
      if stored[1] < tup_list[i][1]:
        stored[1] = tup_list[i][1]
    else:
      merge_lst.append(stored)
      stored = tup_list[i]
  merge_lst.append(stored)
  
  final_list = []
  for i in merge_lst:
    i = tuple(i)
    final_list.append(i)
  
  return final_list


# Input: tuples_list is a list of tuples denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
  # Begin with second item and compare it to the left to determine whether it is smaller or larger.
  # Continue through list and only move the item to the left if it is smaller.  for tuple in range(1,len(tuples_list)):
  for tuple in range(1,len(tuples_list)):
    j = tuple
    while j > 0 and interval_size(tuples_list[j]) < interval_size(tuples_list[j-1]):
      tuples_list[j], tuples_list[j - 1] = tuples_list[j - 1], tuples_list[j]
      j -= 1
  # return sorted tuples_list
  return tuples_list

# Create helper function to determine the size of an interval.
# Will take in a tuple and return the difference between the first and second element inside of the tuple
def interval_size(tuple):
  size = tuple[1]-tuple[0]
  return size


# # Input: no input
# # Output: a string denoting all test cases have passed
# def test_cases ():
#   assert merge_tuples([(1,2)]) == [(1,2)]
#   # write your own test cases

#   assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
#   # write your own test cases

#   return "all test cases passed"

def main():
  # open file intervals.in and read the data and create a list of tuples
    n = sys.stdin.readline()
    n = n.strip()

    tuples_list = []

    for string_pair in sys.stdin:
        string_pair = string_pair.strip()

        individual_tuples = tuples(string_pair)
        tuples_list.append(individual_tuples)
  # merge the list of tuples

    merge = merge_tuples(tuples_list)
    print(merge)
    test = sort_by_interval_size(merge)
    print(test)
#   # sort the list of tuples according to the size of the interval
#         sort = sort_by_interval_size(merge)
  # run your test cases
#   '''
#   print (test_cases())
#   '''

  # write the output list of tuples from the two functions

if __name__ == "__main__":
  main()
