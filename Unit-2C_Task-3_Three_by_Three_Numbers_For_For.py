# Example solution: 3x3 grid of numbers (for-for)
num = 1

for row_loop_var in range(1, 4):
    for column_loop_var in range(1, 4):
        print(num, end=" ")
        num = num + 1
    print()