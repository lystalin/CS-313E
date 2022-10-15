#  File: Palindrome.py

#  Description: In this program, we're making inputted letters/words into palindromes. We are either adding letters onto the beginning or ends of 
# these strings in order to do so.


import sys

# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string
def smallest_palindrome(str):

    # Checks if is a palindrome
    if is_palindrome(str) == True:
        # Returns the string if it is
        return str
    
    # Appends the individual letters to a list
    string_list = []
    for i in str:
        string_list.append(i)

    # While the string isn't a palindrome, add the -ith element
    j = 1
    while is_palindrome(str) == False:
        extra_string = ''
        for i in range(1,j):
        # Add the last last ith element
          extra_string += string_list[-i]
        new_str = extra_string + str
        j += 1
        # If the string is a palindrome, then break
        if is_palindrome(new_str)== True:
          break
    
    # Return the new string
    return new_str


# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the reverse order of the inputted string
def reverse_string(word):
  result = ''
  for i in range(len(word)-1,-1,-1):
    result = result + word[i]
  return result


# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a boolean that determines whether the inputted string is a palindrome
def is_palindrome(word):
  word_p = reverse_string(word)
  # if the inputted word is equal to the reverse of the word, then it's a palindrome
  if word_p == word:
    return True
  if word_p != word:
    return False 


# Input: no input
# Output: a string denoting all test cases have passed
# def test_cases():
#   # write your own test cases

#   return "all test cases passed"

def main():
    # run your test cases
    '''
    print (test_cases())
    '''

    # read the data
    while True:
      line = sys.stdin.readline()
      if line == "":
        break
      else:
        line = line.strip()
        # print the smallest palindromic string that can be made for each input
        print(smallest_palindrome(line))
         

if __name__ == "__main__":
  main()
