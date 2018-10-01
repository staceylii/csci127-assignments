#Stacey Li
#Darren Liang

"f(n) = {n / 2 if n is even, 3n + 1 if n is odd"
"in the loop, print out sequence. return and print out the # of steps"

def collatz(n):
    count = 0
    print(n)
    while n > 1:
        if n % 2 == 0:
            n = n/2
            print(int(n))
            count += 1
        else:
            n = 3 * n + 1
            print(int(n))
            count += 1
    return "Count: " + str(count)

print(collatz(5))
print(collatz(27))