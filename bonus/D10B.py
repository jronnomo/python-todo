# demonstrate the difference between errors and checks

try:
    length = float(input("Enter a rectangle width: "))
    height = float(input("Enter a rectangle height: "))
    if length == height:
        print("We do not accept squares")
        exit()
    area = length * height
    print(f"The area of the rectangle is: {area}")
except ValueError:
    print("Enter only numeric values")