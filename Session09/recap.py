# User menu to compute areas of shapes
# Done before eastern brake
menu = """
Pick a shape (1-3):
    1) Square
    2) Rectangle
    3) Triangle
"""
def compute_area():
    try:
        shape = int(input(menu))
        if shape == 1:
            length = float(input("Length: "))
            print("Area of square = ", length ** 2)
        elif shape == 2:
            length = float(input("Length: "))
            width = float(input("Width: "))
            print("Area of rectangle = ", width * length)
        elif shape == 3:
            length = float(input("Length: "))
            base = float(input("Base: "))
            print("Area of rectangle = ", length * base/2)
        else:
            print("Not a valid shape. Try again")
            compute_area()
    except Exception:
        print("Oops, something went wrong...try again")
        compute_area()

compute_area()