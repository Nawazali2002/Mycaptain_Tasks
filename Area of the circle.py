import math

def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

def main():
    radius = float(input("Input the radius of the circle: "))
    circle_area = calculate_circle_area(radius)
    print("The area of the circle with radius", radius, "is:", circle_area)

if __name__ == "__main__":
    main()

