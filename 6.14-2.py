#함수에 인자 n을 전달하면 구구단 n단을 출력하는 함수를 작성하시오

def gugudan(n):
    for i in range(1, 10):
        print("%d X %d = %d" %(n, i, n*i))

n = input("구구단 몇 단을 출력하시겠습니까? ")
gugudan(int(n))