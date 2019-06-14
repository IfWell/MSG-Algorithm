#함수에 인자 둘을 전달했을 때 두 수와 두 수 사이의 구구단을 출력하는 함수를 작성하시오

#구구단 출력 함수
def gugudan(n):
    for i in range(1, 10):
        print("%d X %d = %d" %(n, i, n*i))

def manygugudan(a, b):
    if a > b:
        n1 = b
        n2 = a
    elif a < b:
        n1 = a
        n2 = b
    else:
        n1 = a
        n2 = a

    for i in range(n1, n2+1):
        gugudan(i)
        print('')

a = input("a를 입력하세요 : ")
b = input("b를 입력하세요 : ")
manygugudan(int(a), int(b))