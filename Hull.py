#  File: Hull.py

#  Description: In this assignment we created a program that would take all of the points of a shape, find the outermost points
# and then find the area of this shape. Our program also returns the outer most points in a clockwise order.

#  Student Name: Colleen Miller

#  Student UT EID: cem4948

#  Partner Name: Jazmin Reyna

#  Partner UT EID: jr68648

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/24/2022

#  Date Last Modified: 9/26/2022

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)



# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
    #calculate the cross product of the three points
    #if positive, left turn
    #if negative, right turn
    #if 0, they are colinear

    return (q.x*r.y - r.x*q.y) - (p.x*r.y - p.y*r.x) + (p.x*q.y - p.y*q.x)


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull

def convex_hull (sorted_points):
    # initialize empty list
  upper_hull = []
  # add first two points
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])
  # add other points
  for i in range(2,len(sorted_points)):
    upper_hull.append(sorted_points[i])
    #remove points given conditions
    while len(upper_hull) >= 3 and det(upper_hull[-1], upper_hull[-2], upper_hull[-3]) >= 0:                      
        upper_hull.remove(upper_hull[-2])

  lower_hull = []
  #add last 2 points
  lower_hull.append(sorted_points[-1])
  lower_hull.append(sorted_points[-2])
  # remove points given condiitons
  for i in range(len(sorted_points)-2,-1,-1):
    lower_hull.append(sorted_points[i])
    while len(lower_hull) >= 3 and det(lower_hull[-1], lower_hull[-2], lower_hull[-3]) >= 0:                  
        lower_hull.remove(lower_hull[-2])
    # remove duplicate values
  lower_hull.remove(lower_hull[0])
  lower_hull.remove(lower_hull[-1])

  for i in lower_hull:
    upper_hull.append(i)

    #return sorted convex_hull points
  return sort(upper_hull)



# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly): 
  det = 0
  # cross multiply and add determinant
  for i in range(len(convex_poly)-1):
    det += convex_poly[i].x * convex_poly[i+1].y
  
  det += convex_poly[-1].x * convex_poly[0].y
  
  # cross multiple and subtract determinant
  for i in range(len(convex_poly)-1):
    det -= convex_poly[i].y * convex_poly[i+1].x

  det -= convex_poly[-1].y * convex_poly[0].x

# calculate area from determinant value
  return .5 * abs(det)



# Input: points is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: returns the point objects sorted in a clockwise fashion
def sort(points):
    # initializes empty lists
  angle_list = []
  final_list = []
  
  x = 0
  y = 0
  for i in points:
    x += i.x
    y += i.y
  centroid = Point(x / len(points), y / len(points))
  
  for i in points:
    lst =[]
    #calculates angle of point from starting point
    angle = math.atan2(i.y-centroid.y, i.x-centroid.x) * 180/math.pi
    lst.append(angle)
    lst.append(i)
    angle_list.append(lst)
   
   # remove first point so no duplicate
  angle_list.remove(angle_list[0])

  angle_list.sort(reverse = True)
  
  final_list.append(points[0])
  
  # append second element to final list
  for i in angle_list:
      final_list.append(i[1])

  return final_list

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)

  '''
  # print the sorted list of Point objects
  for p in sorted_points:
    print (str(p))
  '''

  # get the convex hull
  convex_h = convex_hull(sorted_points)
  # run your test cases
  # print your results to standard output
  # print the convex hull
  print("Convex Hull")
  for i in convex_h:
    print(i)
  # get the area of the convex hull
  print()
  area = area_poly(convex_h)
  # print the area of the convex hull
  print("Area of Convex Hull =",area)
if __name__ == "__main__":
  main()