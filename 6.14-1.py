#함수에 인수 n을 전달시 n보다 작은 소수만 출력하는 프로그램을 작성하시오

def sosu(n):
    num = 0
    for i in range(2, n):
        for j in range(1, i+1):
            if(i % j == 0):
                num = num + 1
        if(num == 2):
            print(i)
        num = 0

n = input("n을 입력하세요 : ")
sosu(int(n))