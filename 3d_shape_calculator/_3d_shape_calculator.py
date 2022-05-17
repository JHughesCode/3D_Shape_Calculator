pi = 3.1415926

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

on = 1
while on == 1:
    print("""Hello! This program calculates the volume and surface area of 3D shapes. 
You will need some measurements to hand, such as the length of the sides and the radius of any circular measurements.
    
Please enter: 
1 if your shape is a SPHERE
2 if your shape is a CYLINDER
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
    elif shape == "0":
        on = 0
    else:
        print("Command not recognised. Please try again.")
    print("Exiting program - goodbye.")

