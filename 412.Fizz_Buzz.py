"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

"""

n = list(range(1, int(input()) + 1))

for i in range(len(n)):
    if (n[i] % 3 == 0) and (n[i] % 5 == 0):
        n[i] = "FizzBuzz"
    elif n[i] % 3 == 0:
        n[i] = "Fizz"
    elif n[i] % 5 == 0:
        n[i] = "Buzz"
    else:
        n[i] = str(n[i])

print(n)