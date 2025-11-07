import math

# asking user for the 3 sides of a triangle

side_1 = int(input("Enter one length for the 3 sides of a trianble: "))

side_2 = int(input("Enter length number 2 of the 3 sides: "))

side_3 = int(input("Enter the 3rd side of the 3 sides: "))

# below is the calculation and answer to the area of the triangle

s = (side_1 + side_2 + side_3) / 2

area = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))

print(area)


