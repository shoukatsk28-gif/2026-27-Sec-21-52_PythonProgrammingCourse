# Example solution: break statement using a for loop
n = int(input("Enter N (print until N, stop early at 5): "))

for number in range(1, n + 1):
    if number == 5:
        print(f"Breaking for loop at number {number} (N was {n})")
        break
    print(f"for loop number = {number} (up to {n})")