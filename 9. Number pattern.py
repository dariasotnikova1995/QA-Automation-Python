def print_number_pattern(n):
    if n < 1 or n > 9:
        print("Number must be in the range 1 to 9.")
        return
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end="w")
        print()
n = int(input("Enter n: "))
print_number_pattern(n)