'''
Write a program to generate the Fibonacci sequence up to n terms.

'''
n = int(input("Enter the number of terms: "))
fib_sequence = []

a, b = 0, 1
for _ in range(n):
    fib_sequence.append(a)
    a, b = b, a + b

print("Fibonacci sequence up to", n, "terms:")
print(fib_sequence)