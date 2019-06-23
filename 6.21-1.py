#피보나치 수열 출력 문제

def fibo(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n < 0:
        return -1
    else:
        return fibo(n - 1) + fibo(n - 2)

i = 1
a = input("피보나치 수열의 몇 번째 항까지 출력할까요? ")
while (i <= int(a)):
    print(fibo(i))
    i = i + 1