import math
pi = math.pi


class sphere:
    def __init__(self, rad):
        self.rad = rad

    def volume(self):
        print(f"The sphere's volume is: {(4/3) * (pi * rad ** 3)}.")

    def area(self):
        print(f"The sphere's area is {4 * pi * rad ** 2}.")

class cylinder:
    def __init__(self, rad, length):
        self.rad = rad
        self.length = length

    def volume(rad, length):
        print(f"The cylinder's volume is: {pi * rad * rad * length}")

    def area(rad, length):
        print(f"The cylinder's area is: {((2*pi*rad) * length) + ((pi*rad**2)*2)}")

class square_pyramid:
    def __init__(self, base_edge, height):
        self.base_edge = base_edge
        self.height = height

    def volume(base_edge, height):
        print(f"The pyramid's volume is {1/3 * math.pow(base_edge, 2) * height}")

    def area(base_edge, height):
        print(f"The pyramid's area is: {math.pow(base_edge, 2) + 2*base_edge * math.sqrt(math.pow(base_edge, 2) / 4 + math.pow(height, 2))}")

class cuboid:
    def __init__(self, height, length, depth):
        self.height = height
        self.length = length
        self.depth = depth

    def volume(height, length, depth):
        print(f"The volume of your cuboid is: {height * length * depth}")

    def area(height,length, depth):
        print(f"The surface area of your cuboid is {(height * length * 2) + (length * depth * 2) + (height * depth * 2)}")

on = 1
while on == 1:
    print("""Hello! This program calculates the volume and surface area of 3D shapes. 
You will need some measurements to hand, such as the length of the sides and the radius of any circular measurements.
    
Please enter: 
1 if your shape is a SPHERE
2 if your shape is a CYLINDER
3 if your shape is a right square based PYRAMID
4 if your shape is a CUBOID
or 0 to exit the program""")
    shape = input("What kind of shape would you like?")
    if shape == "1":
        rad = float(input("Please enter the sphere's radius. "))
        sphere.volume(rad)
        sphere.area(rad)
    elif shape == "2":
        rad = float(input("Please enter the radius of the cylinder's circular face. "))
        length = float(input("Please enter the length of the cylinder, from circular face to circular face. "))
        cylinder.volume(rad, length)
        cylinder.area(rad, length)
    elif shape == "3":
        base_edge = float(input("What is the length of one of the base's edges?"))
        height = float(input("What is the perpendicular height (centre of the base to the top point) of the pyramid?"))
        square_pyramid.volume(base_edge, height)
        square_pyramid.area(base_edge, height)
    elif shape == "4":
        length = float(input("Please enter the cuboid's length: "))
        height = float(input("Please enter the cuboid's height"))
        depth = float(input("Please enter the cuboid's depth"))
        cuboid.volume(length, height, depth)
        cuboid.area(length, height, depth)
    elif shape == "0":
        on = 0
    else:
        print("Command not recognised. Please try again.")
print("Exiting program - goodbye.")

