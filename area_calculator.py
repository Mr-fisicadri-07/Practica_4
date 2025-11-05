b = float(input("\nEnter the width of the rectangle (cm): \n"))

h = float(input("\nEnter the height of the rectangle (cm): \n"))

def area_of_rectangle(b, h):
    area = b * h
    return area

print("\nThe area of the rectangle is: {:.2f} square centimeters\n".format (area_of_rectangle(b, h)))