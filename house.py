# Function to calculate the area of a house (square footage)
# Area = length x width
def square_footage():
    l = int(input("What's the length? "))
    w = int(input("What's the width? "))
    area = l * w
    print(f"The area of the house is {area} square feet.")

square_footage()

# Function to calculate the circumference of a circle.
def circum_circle():
    p = 3.14159265
    r = int(input("What is the radius of the circle? "))
    circumference = 2 * p * r
    print(f"The circumference of the circle is {circumference}.")

circum_circle()

