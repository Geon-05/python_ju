'''
1)사각형 넓이를 구하는 함수 작성 --> area(가로, 세로)
2)사각형의 가로, 세로 길이가 양수인지 입력검증하는 함수 작성 -->input_pos(msg)

[실행화면]
사각형의 가로: -1
양수만 입력하시오
사각형의 가로: 100
사각형의 세로: 100
면적 = 10000
'''

#사각형 넓이
def area(w,h):
    return w*h

def input_pos(msg):
    while True:
        value=int(input(msg))
        if value > 0:
            return value
        else:
            print('양수만 입력하시오.')
        
# 메인실행
width = input_pos('사각형의 가로 넓이: ') # 가로 길이 입력
height= input_pos('사각형의 세로 넓이: ') # 세로 길이 입력

res_area=area(width, height)  #사각형 넓이 구하기
print('면적 = ', res_area)

