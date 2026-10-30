# Example solution: continue statement using a for loop
n = int(input("Enter N (print 1 to N, skip even numbers): "))

for number in range(1, n + 1):
    if number % 2 == 0:
        print(f"Skipping even number {number} with continue (N is {n})")
        continue
    print(f"for loop odd number = {number} (up to {n})")