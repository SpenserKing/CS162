# Project requires TWO functions:
# 1. rect_area (length, width) which will return the area of a rectangle
# 2. rect_surface_area (length, width, height) which will return the area of a solid rectangular object

def rect_area(length, width):
    # Computes area
    return length * width


def rect_surface_area(length, width, height):
    # Computes surface area
    face1 = rect_area(length, width)
    face2 = rect_area(length, height)
    face3 = rect_area(width, height)
    total_area = 2 * (face1 + face2 + face3)
    return total_area

# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the object as an integer: "))
width = int(input("Enter the width of the object as an integer: "))
height = int(input("Enter the height of the object as an integer: "))

# Call the surface area function
surface_area = rect_surface_area(length, width, height)

# Output the results
print("Length =", length, "Width =", width, "Height =", height)
print("Total Surface Area =", surface_area)

# end