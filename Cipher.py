#  File: Cipher.py 

#  Description: When given two strings, we will encrypt the first string and decrypt the second string. To encrypt the first string,
#               we begin by building a table with K x K dimensions, where K is the square root of the length of the string when
#               being made into a perfect square by adding '*' to the string when necessary. Using this table, we will rotate it 
#               clockwise giving us an encrypted message when read by row. We will output the encrypted message omitting any asterisk 
#               and keeping the each character's case of the original message. To decrypt the second string, we will perform the 
#               reverse of this process by building a table of the encrypted message and rotating the table counter-clockwise.


import sys

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 

def encrypt ( strng ):
    L = len(strng)
    M = 0

  # Checks if length of string is a perfect square.
    while True:
        if (L**.5) % 1 == 0:
            M = L**.5
            break
        else:
          #keeps adding one until perfect square.
            L += 1
    K = int(M)
    M = M**2
    L = len(strng)

    # Adds * to empty spaces.
    for i in range(int(M)-L):
        strng += "*"

    # Creates 2D list.
    two_d = []
    for i in range(K):
        two_d.append([])
    
    # Adds letters in the string to list
    letter_list = []
    for i in strng:
        letter_list.append(i)

    # Adds letters to 2D list
    two = 0
    count = 0
    for i in strng:
        two_d[two].append(i)
        count += 1
        if count == K:
            strng[K:]
            two += 1
            count = 0

    #Create an empty list.
    new_two_d = []
    #Make the empty list 2-d with K by K dimensions
    for row in range(K):
      new_two_d.append([])
      for col in range(K):
        new_two_d[row].append([])
    #Create placeholders to traverse through table with original message and empty list
    rows = 0
    counter = 0
    y = 1
    #Create loop that will run K times and will append each row of original message table to each
    #column in empty list, starting with the last element in the first row to the first element
    #in the last row and repeating this process in each column.
    for i in range(int(K)):
      for x in two_d[rows]:
        new_two_d[counter][K-y].append(x)
        counter+=1
      counter = 0
      rows += 1
      y += 1
      
    encrypt_string = ""
    for row in range(K):
      for col in range(K):
        if new_two_d[row][col][0] == "*":
          encrypt_string += ""
        else:
          encrypt_string += new_two_d[row][col][0]
    return(encrypt_string)



def decrypt ( strng ):
    L = len(strng)
    M = 0

  # Checks if length of string is a perfect square.
    while True:
        if (L**.5) % 1 == 0:
            M = L**.5
            break
        else:
           #keeps adding one until perfect square.
            L += 1
    K = int(M)
    M = M**2
    L = len(strng)

  # Adds * to empty spaces.
    for i in range(int(M)-L):
        strng += "*"
    
    # Creates 2D list.
    two_d = []
    
    for i in range(K):
        two_d.append([])
    
    # Adds letters in the string to list
    letter_list = []
    for i in strng:
        letter_list.append(i)

    # Adds letters to 2D list 
    two = 0
    count = 0
    for i in strng:
        two_d[two].append(i)
        count += 1
        if count == K:
            strng[K:]
            two += 1
            count = 0
    #Create an empty list.    
    new_two_d = []
    #Make the empty list 2-d with K by K dimensions.
    for row in range(K):
      new_two_d.append([])
      for col in range(K):
        new_two_d[row].append([])
    #Create placeholders to traverse through the table with the encrypted message and the empty list. 
    rows = 0
    counter = K-1
    
    y = K
    #Create loop that will run K times and will append each row of the encrypted message table to each
    #column in the empty list, starting with the elements in the first row and appending them to the first 
    #elements in the first column (from bottom to top) and repeating this process in each column.
    for i in range(K):
      for x in two_d[rows]:
        new_two_d[counter][K-y].append(x)
        counter-=1
      counter = K-1
      rows += 1
      y -= 1
    
    decrypt_string = ""
    for row in range(K):
      for col in range(K):
        if new_two_d[row][col][0] == "*":
          decrypt_string += ""
        else:
          decrypt_string += new_two_d[row][col][0]
    return(decrypt_string)


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
# def decrypt ( strng ):

def main():
  # read the two strings P and Q from standard imput
    P = sys.stdin.readline()
    P = P.strip()
    Q = sys.stdin.readline()
    Q = Q.strip()
  # encrypt the string P
    e = encrypt(P)
  # decrypt the string Q
    d = decrypt(Q)
  # print the encrypted string of P and the 
    print(e)
  # decrypted string of Q to standard out
    print(d)

if __name__ == "__main__":
  main()
