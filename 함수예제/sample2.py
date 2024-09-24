'''
[소수 찾기]
 소수: 1과 자기자신만을 약수로 가지는 수
 (풀이) 어떤 수 n이 소수인지 확인: n을 2에서 n-1까지 나눠서 나머지가 0이 아니면 소수임

 [실행화면]
 정수를 입력해 주세요: 101
 True 
'''


def test_prime(n):
    if n==1 or n==2:
        return True
    for i in  range(2,n):
        if n%i==0:
            return False
    return True

num=int(input('정수를 입력해 주세요:'))
print(test_prime(num))


'''
1~100까지 모든 소수를 찾으시오

[실행화면]
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
'''
# for i in range(2,100):
#     if test_prime(i):
#         print(i, end=' ')