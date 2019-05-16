#문제(1) ppt의 문제 3번
# """로 둘러싸인 코드들은 없는 걸로 처리됨. 지우고 사용할 것

#for을 이용한 풀이
"""
for i in range(1, 10):
    for j in range(1, 10):
        print("{0} x {1} = {2}".format(i, j, i*j))
"""

#while을 이용한 풀이
"""
i,j = 1,1
while(i <= 9):
    j = 1       #j를 다시 1로 초기화
    while(j <= 9):
        print("{0} x {1} = {2}".format(i, j, i*j))
        j+=1
    i+=1
"""