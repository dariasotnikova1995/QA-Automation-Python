height = int(input("Enter the height of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
symbol = input("Enter symbol to build rectangular with: ")
for i in range(height):
    for j in range(width):
        print(symbol, end="")
    print()