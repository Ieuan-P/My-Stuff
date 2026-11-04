def fibonacci(n):
    prev = 0
    curr = 1
    temp = 0
    for i in range(n - 1):
        temp = curr
        curr = prev + curr
        prev = temp
    return prev

print(fibonacci(int(input("Enter a number: "))))