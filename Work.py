#  File: Work.py 

#  Description:  Vyasa must write n number of lines of code before morning. To help him stay awake, he drinks cup after cup of black
#                coffee. However, after each cup of coffee, Vyasa's productivity goes down by a factor of k. Given integers n and k, I
#                will write a program that searches for a number v representing the number of lines of code he must write before his first
#                cup of coffee, where n <= (v // k ** 0) + (v // k ** 1) + (v // k ** 2) + ... (v // k ** p), and (v // k ** p+1) = 0. I 
#                will first find v through binary search, then through linear search. I will output the timed searches and their v values.

#  Student Name:  Jazmin Reyna

#  Student UT EID:  jr68648

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/27/2922

#  Date Last Modified:  9/30/2022

import sys, time

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
  # use linear search here
  j = 1
  #check if every number from j to n is >= n
  while (j < n):
        if total_code_lines(j,k) >= n:
            return j
        j += 1
  return j

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # use binary search here
    low = 0
    high = n
    
    while high > low:
        mid = (high + low) // 2
        mid_total = total_code_lines(mid,k)
        if mid_total <= n:
            low = mid + 1
        elif mid_total >= n:
            high = mid - 1
        else:
            break
    
    high_total = total_code_lines(high,k)
    low_total = total_code_lines(low,k)

    #check if high_total, low_total, or mid_total are the closest to n
    if mid_total - n > high_total - n >= 0 and n - high_total < mid_total - n or mid_total < n:
        mid = high
    
    if mid_total - n > low_total - n >= 0 and n - low_total < mid_total - n:
        mid = low
    
    #return value v representing lines of code that must be written before first cup of coffee
    return mid

#helper function
#takes an a value v which represents number of lines before first cup of coffee with a decreasing productivity factor
#sums total until holder value == 0, which is when Vyasa falls asleep
#returns total
def total_code_lines(v,k):
    temp_exp = 0
    total = 0
    holder = v
    while holder > 0:
        holder = v // (k ** (temp_exp))
        temp_exp += 1
        total += holder
    
    return total


# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
