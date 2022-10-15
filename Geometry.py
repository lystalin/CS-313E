#  File: Geometry.py 

#  Description: 

#  Student Name: Colleen Miller

#  Student UT EID: cem4948

#  Partner Name: Jazmin Reyna

#  Partner UT EID: jr68648

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/13/2022

#  Date Last Modified: 


import math
import sys

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = x
    self.y = y
    self.z = z

# get the distance to another point
  def distance(self, other):
    return math.sqrt ((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

# string representation of a point
  def __str__(self):
    return '(' + str(float(self.x)) + ', ' + str(float(self.y)) + ', ' + str(float(self.z)) + ')'

# test for equality of two points
  def __eq__(self, other):
    tol = 1.0e-6
    return((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.center = Point(x, y, z)
    self.radius = radius

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return 'Center: (' + str(float(self.center.x)) + ', ' + str(float(self.center.y)) + ', ' + str(float(self.center.z)) + '), Radius: ' + str(float(self.radius))

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    return (((self.radius)**2)*(4)*(math.pi))

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    return (((self.radius)**3)*(4/3)*(math.pi))

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    distance = math.sqrt ((self.center.x - p.x)**2 + (self.center.y - p.y)**2 + (self.center.z - p.z)**2)
    return distance < self.radius

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    dist_centers = math.sqrt ((self.center.x - other.center.x)**2 + (self.center.y - other.center.y)**2 + (self.center.z - other.center.z)**2)
    return dist_centers + other.radius < self.radius

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    #Check if any of the eight vertices of the cube are inside the sphere.
    vertices = [
        Point(a_cube.center.x + a_cube.side/2, a_cube.center.y + a_cube.side/2, a_cube.center.z + a_cube.side/2),
        Point(a_cube.center.x + a_cube.side/2, a_cube.center.y + a_cube.side/2, a_cube.center.z - a_cube.side/2),
        Point(a_cube.center.x + a_cube.side/2, a_cube.center.y - a_cube.side/2, a_cube.center.z - a_cube.side/2),
        Point(a_cube.center.x + a_cube.side/2, a_cube.center.y - a_cube.side/2, a_cube.center.z + a_cube.side/2),
        Point(a_cube.center.x - a_cube.side/2, a_cube.center.y + a_cube.side/2, a_cube.center.z + a_cube.side/2),
        Point(a_cube.center.x - a_cube.side/2, a_cube.center.y + a_cube.side/2, a_cube.center.z - a_cube.side/2),
        Point(a_cube.center.x - a_cube.side/2, a_cube.center.y - a_cube.side/2, a_cube.center.z + a_cube.side/2),
        Point(a_cube.center.x - a_cube.side/2, a_cube.center.y - a_cube.side/2, a_cube.center.z - a_cube.side/2)
        ]
    for p in vertices:
      distance = math.sqrt ((self.center.x - p.x)**2 + (self.center.y - p.y)**2 + (self.center.z - p.z)**2)
      if distance > self.radius:
        return False
    
    return True

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
    dist_center = math.sqrt ((self.center.x - a_cyl.center.x)**2 + (self.center.y - a_cyl.center.y)**2 + (self.center.z - a_cyl.center.z)**2)
    cyl_diagonal = (math.sqrt( a_cyl.height**2 + (a_cyl.radius*2)**2))/2

    return cyl_diagonal + dist_center < self.radius

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    dist_centers = math.sqrt ((self.center.x - other.center.x)**2 + (self.center.y - other.center.y)**2 + (self.center.z - other.center.z)**2)
    if dist_centers + other.radius > self.radius and dist_centers < self.radius + other.radius:
        return True
    else:
        return False

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
        vertices = [
        Point(a_cube.center.x + a_cube.side/2, a_cube.center.y + a_cube.side/2, a_cube.center.z + a_cube.side/2),
        Point(a_cube.center.x + a_cube.side/2, a_cube.center.y + a_cube.side/2, a_cube.center.z - a_cube.side/2),
        Point(a_cube.center.x + a_cube.side/2, a_cube.center.y - a_cube.side/2, a_cube.center.z - a_cube.side/2),
        Point(a_cube.center.x + a_cube.side/2, a_cube.center.y - a_cube.side/2, a_cube.center.z + a_cube.side/2),
        Point(a_cube.center.x - a_cube.side/2, a_cube.center.y + a_cube.side/2, a_cube.center.z + a_cube.side/2),
        Point(a_cube.center.x - a_cube.side/2, a_cube.center.y + a_cube.side/2, a_cube.center.z - a_cube.side/2),
        Point(a_cube.center.x - a_cube.side/2, a_cube.center.y - a_cube.side/2, a_cube.center.z + a_cube.side/2),
        Point(a_cube.center.x - a_cube.side/2, a_cube.center.y - a_cube.side/2, a_cube.center.z - a_cube.side/2)
        ]
        
        counter = 0

        for i in vertices:
          distance = math.sqrt ((self.center.x - i.x)**2 + (self.center.y - i.y)**2 + (self.center.z - i.z)**2)
          if distance < self.radius:
            counter +=1
        
        if counter >= 1 and counter <= 7 :
          return True
        else:
          return False

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    largest_dist_vertices = (self.radius * 2 / math.sqrt(3))

    c_cube = Cube ( self.center.x , self.center.y , self.center.z , largest_dist_vertices )

    return c_cube


class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.center = Point(x, y, z)
    self.side = side

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return 'Center: (' + str(float(self.center.x)) + ', ' + str(float(self.center.y)) + ', ' + str(float(self.center.z)) + '), Side: ' + str(float(self.side))

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return (6*((self.side)**2))

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return ((self.side)**3)

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
        if (self.center.x + self.side/2) > p.x > (self.center.x - self.side/2) and (self.center.y + self.side/2) > p.y > (self.center.y - self.side/2) and (self.center.z + self.side/2) > p.z > (self.center.z - self.side/2):
            return True
        else:
            return False

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):

    #calculate distance between the centers of sphere and of cube
    distance = math.sqrt ((self.center.x - a_sphere.center.x)**2 + (self.center.y - a_sphere.center.y)**2 + (self.center.z - a_sphere.center.z)**2)
    #if the distance between centers + the radius of sphere < (self cube side / 2), it is strictly inside
    return distance + a_sphere.radius < self.side/2


  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):

    #calculate distance between the centers of the two cubes
    distance = math.sqrt ((self.center.x - other.center.x)**2 + (self.center.y - other.center.y)**2 + (self.center.z - other.center.z)**2)
    #if the distance between the centers + (other cube side / 2) < (self cube side / 2), it is strictly inside
    return distance + other.side / 2 < self.side / 2

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):

    max_x_cube = self.center.x + self.side/2
    max_y_cube = self.center.y + self.side/2
    max_z_cube = self.center.z + self.side/2
    min_x_cube = self.center.x - self.side/2
    min_y_cube = self.center.y - self.side/2
    min_z_cube = self.center.z - self.side/2
    
    max_x_cyl = a_cyl.center.x + a_cyl.radius
    max_y_cyl = a_cyl.center.y + a_cyl.radius
    max_z_cyl = a_cyl.center.z + a_cyl.height/2
    min_x_cyl = a_cyl.center.x - a_cyl.radius
    min_y_cyl = a_cyl.center.y - a_cyl.radius
    min_z_cyl = a_cyl.center.z - a_cyl.height/2

    if max_x_cube > max_x_cyl and min_x_cube < min_x_cyl and max_y_cube > max_y_cyl and min_y_cube < min_y_cyl and max_z_cube > max_z_cyl and min_z_cube < min_z_cyl:
      return True
    else:
      return False


  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):

    vertices = [
    Point(other.center.x + other.side/2, other.center.y + other.side/2, other.center.z + other.side/2),
    Point(other.center.x + other.side/2, other.center.y + other.side/2, other.center.z - other.side/2),
    Point(other.center.x + other.side/2, other.center.y - other.side/2, other.center.z - other.side/2),
    Point(other.center.x + other.side/2, other.center.y - other.side/2, other.center.z + other.side/2),
    Point(other.center.x - other.side/2, other.center.y + other.side/2, other.center.z + other.side/2),
    Point(other.center.x - other.side/2, other.center.y + other.side/2, other.center.z - other.side/2),
    Point(other.center.x - other.side/2, other.center.y - other.side/2, other.center.z + other.side/2),
    Point(other.center.x - other.side/2, other.center.y - other.side/2, other.center.z - other.side/2)
    ]

    counter = 0

    for p in vertices:
      if (self.center.x + self.side/2) > p.x > (self.center.x - self.side/2) and (self.center.y + self.side/2) > p.y > (self.center.y - self.side/2) and (self.center.z + self.side/2) > p.z > (self.center.z - self.side/2):
        counter +=1
    
    if counter >= 1 and counter <= 7 :
      return True
    else:
      return False

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number


  def intersection_volume (self, other):
    #we need to calculate the volume of the two cubes that intersect and find the difference
    #we will return that difference

    distance = math.sqrt ((self.center.x - other.center.x)**2 + (self.center.y - other.center.y)**2 + (self.center.z - other.center.z)**2)
    if distance + other.side / 2 > self.side / 2 and distance < other.side + self.side:
        value =  True
    else:
        value = False
      
    if value == True:
      return abs(self.volume() -other.volume())
    
    if value == False:
      return 0
    
  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):

    #radius of sphere is = self cube side / 2
    radius = self.side/2
    #create sphere with same center as self cube with radius self cube side / 2
    new_sphere = Sphere(self.center.x,self.center.y,self.center.z,radius)
    return new_sphere

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.center = Point(x, y, z)
    self.radius = radius
    self.height = height

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return 'Center: (' + str(float(self.center.x)) + ', ' + str(float(self.center.y)) + ', ' + str(float(self.center.z)) + '), Radius: ' + str(float(self.radius)) + ', Height: ' + str(float(self.height))

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return ((self.radius)*(self.height)*(2)*(math.pi) + ((self.radius)**2)*(2)*(math.pi))

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return (((self.radius)**2)*(self.height)*(math.pi))

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    max_x_cyl = self.center.x + self.radius
    max_y_cyl = self.center.y + self.radius
    max_z_cyl = self.center.z + self.height/2
    min_x_cyl = self.center.x - self.radius
    min_y_cyl = self.center.y - self.radius
    min_z_cyl = self.center.z - self.height/2

    if max_x_cyl > p.x > min_x_cyl and max_y_cyl > p.y > min_y_cyl and max_z_cyl > p.z > min_z_cyl:
      return True
    else:
      return False

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    max_x_sphere = a_sphere.center.x + a_sphere.radius
    max_y_sphere = a_sphere.center.y + a_sphere.radius
    max_z_sphere = a_sphere.center.z + a_sphere.radius
    min_x_sphere = a_sphere.center.x - a_sphere.radius
    min_y_sphere = a_sphere.center.y - a_sphere.radius
    min_z_sphere = a_sphere.center.z - a_sphere.radius


    max_x_cyl = self.center.x + self.radius
    max_y_cyl = self.center.y + self.radius
    max_z_cyl = self.center.z + self.height/2
    min_x_cyl = self.center.x - self.radius
    min_y_cyl = self.center.y - self.radius
    min_z_cyl = self.center.z - self.height/2

    if max_x_cyl > max_x_sphere and min_x_cyl < min_x_sphere and max_y_cyl > max_y_sphere and min_y_cyl < min_y_sphere and max_z_cyl > max_z_sphere and min_z_cyl < min_z_sphere:
      return True
    else:
      return False

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    max_x_cube = a_cube.center.x + a_cube.side/2
    max_y_cube = a_cube.center.y + a_cube.side/2
    max_z_cube = a_cube.center.z + a_cube.side/2
    min_x_cube = a_cube.center.x - a_cube.side/2
    min_y_cube = a_cube.center.y - a_cube.side/2
    min_z_cube = a_cube.center.z - a_cube.side/2


    max_x_cyl = self.center.x + self.radius
    max_y_cyl = self.center.y + self.radius
    max_z_cyl = self.center.z + self.height/2
    min_x_cyl = self.center.x - self.radius
    min_y_cyl = self.center.y - self.radius
    min_z_cyl = self.center.z - self.height/2

    if max_x_cyl > max_x_cube and min_x_cyl < min_x_cube and max_y_cyl > max_y_cube and min_y_cyl < min_y_cube and max_z_cyl > max_z_cube and min_z_cyl < min_z_cube:
      return True
    else:
      return False

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):

    max_x_cyl2 = other.center.x + other.radius
    max_y_cyl2 = other.center.y + other.radius
    max_z_cyl2 = other.center.z + other.height/2
    min_x_cyl2 = other.center.x - other.radius
    min_y_cyl2 = other.center.y - other.radius
    min_z_cyl2 = other.center.z - other.height/2

    max_x_cyl = self.center.x + self.radius
    max_y_cyl = self.center.y + self.radius
    max_z_cyl = self.center.z + self.height/2
    min_x_cyl = self.center.x - self.radius
    min_y_cyl = self.center.y - self.radius
    min_z_cyl = self.center.z - self.height/2

    if max_x_cyl > max_x_cyl2 and min_x_cyl < min_x_cyl2 and max_y_cyl > max_y_cyl2 and min_y_cyl < min_y_cyl2 and max_z_cyl > max_z_cyl2 and min_z_cyl < min_z_cyl2:
      return True
    else:
      return False


  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
    
    #Check if the 2-d circles of the two cylinders intersect eachother
    #if they do, check if the z ranges of the two cylinders intersect eachother
    #if both intersect, return True
    
    dist_circle_2d = math.hypot (self.center.x - other.center.x, self.center.y - other.center.y)
    diff_between_z = abs( self.center.z - other.center.z )

    if dist_circle_2d + other.radius > self.radius and dist_circle_2d < self.radius + other.radius and diff_between_z < self.height/2 + other.height/2:
      return True
    else:
      return False

def main():
  # read data from standard input
  # read the coordinates of the first Point p
    L = sys.stdin.readline()
    L = L.strip()

    count = 0
    first = ""
    second = ""
    third = ""
    for i in L.split():
      if count == 0:
        first += i
      if count == 1:
        second += i
      if count == 2:
        third += i
      count += 1
  # create a Point object 
    p_object = Point(float(first),float(second),float(third))
  # read the coordinates of the second Point q
    L = sys.stdin.readline()
    L = L.strip()

    count = 0
    first = ""
    second = ""
    third = ""
    for i in L.split():
      if count == 0:
        first += i
      if count == 1:
        second += i
      if count == 2:
        third += i
      count += 1  
  # create a Point object 
    q_object = Point(float(first),float(second),float(third))
  # read the coordinates of the center and radius of sphereA
    L = sys.stdin.readline()
    L = L.strip()

    count = 0
    first = ""
    second = ""
    third = ""
    fourth = ""
    for i in L.split():
      if count == 0:
        first += i
      if count == 1:
        second += i
      if count == 2:
        third += i
      if count == 3:
        fourth += i
      count += 1  
  # create a Sphere object 
    sphere_a_object = Sphere(float(first),float(second),float(third),float(fourth))
  # read the coordinates of the center and radius of sphereB
    L = sys.stdin.readline()
    L = L.strip()

    count = 0
    first = ""
    second = ""
    third = ""
    fourth = ""
    for i in L.split():
      if count == 0:
        first += i
      if count == 1:
        second += i
      if count == 2:
        third += i
      if count == 3:
        fourth += i
      count += 1  
  # create a Sphere object
    sphere_b_object = Sphere(float(first),float(second),float(third),float(fourth))
  # read the coordinates of the center and side of cubeA
    L = sys.stdin.readline()
    L = L.strip()

    count = 0
    first = ""
    second = ""
    third = ""
    fourth = ""
    for i in L.split():
      if count == 0:
        first += i
      if count == 1:
        second += i
      if count == 2:
        third += i
      if count == 3:
        fourth += i
      count += 1  
  # create a Cube object 
    cube_a_object = Cube(float(first),float(second),float(third),float(fourth))
  # read the coordinates of the center and side of cubeB
    L = sys.stdin.readline()
    L = L.strip()

    count = 0
    first = ""
    second = ""
    third = ""
    fourth = ""
    for i in L.split():
      if count == 0:
        first += i
      if count == 1:
        second += i
      if count == 2:
        third += i
      if count == 3:
        fourth += i
      count += 1  
  # create a Cube object 
    cube_b_object = Cube(float(first),float(second),float(third),float(fourth))
  # read the coordinates of the center, radius and height of cylA
    L = sys.stdin.readline()
    L = L.strip()

    count = 0
    first = ""
    second = ""
    third = ""
    fourth = ""
    fifth = ""
    for i in L.split():
      if count == 0:
        first += i
      if count == 1:
        second += i
      if count == 2:
        third += i
      if count == 3:
        fourth += i
      if count == 4:
        fifth += i
      count += 1  
  # create a Cylinder object 
    cylinder_a_object = Cylinder(float(first),float(second),float(third),float(fourth),float(fifth))
  # read the coordinates of the center, radius and height of cylB
    L = sys.stdin.readline()
    L = L.strip()

    count = 0
    first = ""
    second = ""
    third = ""
    fourth = ""
    fifth = ""
    for i in L.split():
      if count == 0:
        first += i
      if count == 1:
        second += i
      if count == 2:
        third += i
      if count == 3:
        fourth += i
      if count == 4:
        fifth += i
      count += 1  
  # create a Cylinder object
    cylinder_b_object = Cylinder(float(first),float(second),float(third),float(fourth),float(fifth))
  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
    origin = Point()
    if p_object.distance(origin) > q_object.distance(origin):
      print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
    else:
      print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")

    # # print if Point p is inside sphereA
    if sphere_a_object.is_inside_point(p_object) == True:
        print("Point p is inside sphereA")
    else:
        print("Point p is not inside sphereA")

    # # print if sphereB is inside sphereA
    if sphere_a_object.is_inside_sphere(sphere_b_object) == True:
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")

    # # print if cubeA is inside sphereA
    if sphere_a_object.is_inside_cube(cube_a_object) == True:
          print("cubeA is inside sphereA")
    else:
          print("cubeA is not inside sphereA")

    # # print if cylA is inside sphereA
    if sphere_a_object.is_inside_cyl(cylinder_a_object) == True:
      print("cylA is inside sphereA")
    else:
      print("cylA is not inside sphereA")

    # # print if sphereA intersects with sphereB
    if sphere_a_object.does_intersect_sphere(sphere_b_object) == True:
          print("sphereA does intersect sphereB")
    else:
          print("sphereA does not intersect sphereB")

    # # print if cubeB intersects with sphereB
    if sphere_b_object.does_intersect_cube(cube_b_object) == True:
          print("cubeB does intersect sphereB")
    else:
          print("cubeB does not intersect sphereB")

  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
        
    if sphere_a_object.circumscribe_cube().volume() > cylinder_a_object.volume():
        print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
    else:
        print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

#     # print if Point p is inside cubeA
    if cube_a_object.is_inside_point(p_object) == True:
          print("Point p is inside cubeA")
    else:
          print("Point p is not inside cubeA")

#     # print if sphereA is inside cubeA
    if cube_a_object.is_inside_sphere(sphere_a_object) == True:
          print("sphereA is inside cubeA")
    else:
          print("sphereA is not inside cubeA")

#     # print if cubeB is inside cubeA
    if cube_a_object.is_inside_cube(cube_b_object) == True:
          print("cubeB is inside cubeA")
    else:
          print("cubeB is not inside cubeA")

#     # print if cylA is inside cubeA
    if cube_a_object.is_inside_cylinder(cylinder_a_object) == True:
          print("cylA is inside cubeA")
    else:
          print("cylA is not inside cubeA")

#     # print if cubeA intersects with cubeB
    if cube_a_object.does_intersect_cube(cube_b_object) == True:
          print("cubeA does intersect cubeB")
    else:
          print("cubeA does not intersect cubeB")

#   # print if the intersection volume of cubeA and cubeB
#   # is greater than the volume of sphereA
    if cube_a_object.intersection_volume(cube_b_object) > cylinder_a_object.volume():
        print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
    else:
        print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")

#   # print if the surface area of the largest Sphere object inscribed 
#   # by cubeA is greater than the surface area of cylA
    if cube_a_object.inscribe_sphere().area() > cylinder_a_object.area():
        print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
    else:
        print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")
  
#     # print if Point p is inside cylA
    if cylinder_a_object.is_inside_point(p_object) == True:
          print("Point p is inside cylA")
    else:
          print("Point p is not inside cylA")

#     # print if sphereA is inside cylA
    if cylinder_a_object.is_inside_sphere(sphere_a_object) == True:
          print("sphereA is inside cylA")
    else:
          print("sphereA is not inside cylA")

#     # print if cubeA is inside cylA
    if cylinder_a_object.is_inside_cube(cube_a_object) == True:
          print("cubeA is inside cylA")
    else:
          print("cubeA is not inside cylA")

    # print if cylB is inside cylA
    if cylinder_a_object.is_inside_cylinder(cylinder_b_object) == True:
          print("cylB is inside cylA")
    else:
          print("cylB is not inside cylA")

    # print if cylB intersects with cylA
    if cylinder_a_object.does_intersect_cylinder(cylinder_b_object) == True:
          print("cylB does intersect cylA")
    else:
          print("cylB does not intersect cylA")

if __name__ == "__main__":
  main()