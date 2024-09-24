'''
메시지(msg)와 number를 매개변수러 지정하고, 이때 number를 생략하면 기본값 1로 지정함
메시지(msg)가 number 수만큼 반복해서 출력되는 함수 작성 --> prn_msg(msg, number=1)
'''
def prn_msg(msg, number=1):
    for _ in range(number):
        print(msg)

prn_msg('안녕하세요')
prn_msg('좋은 하루',5)