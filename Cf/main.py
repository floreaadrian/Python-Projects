def fastPow(a, p):
    r = 1
    while p > 0:
        if p % 2 == 1:
            r = r * a
        a = a * a
        p /= 2
    return r


def f(num):
    if (num <= 9):
        return num
    sumOfDigits = 0
    temp = num[:]
    while (temp > 0):
        sumOfDigits += temp % 10
        temp /= 10

    return f(sumOfDigits)


t = int(input())
for i in range(0, t):
    val=input().split(" ")
    a = int(val[0])
    n = int(val[1])
    print(f(fastPow(a, n)))
