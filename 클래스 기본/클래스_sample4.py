'''
참고사이트:
https://datascienceschool.net/01%20python/02.12%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D.html
'''

import datetime

class BankAccount:
    def __init__(self, filepath):
        self.filepath = filepath
        self.balance = self.load_account()

    # 잔액(balance) 불러오기
    def load_account(self):
        with open(self.filepath, 'r') as f:
            txt = list(f)
        balance = int(txt[-1].split(':')[-1].strip())
        return balance

    # 적금하기
    def save(self):
        chk = self.balance
        while True:
            amount = int(input('얼마를 저축하시겠습니까?(종료는 -1) '))
            if amount == -1:
                print('프로그램이 종료됩니다.')
                break
            self.balance += amount
            print(f'지금까지 저축액은 {self.balance}입니다.')
        if self.balance != chk:
            self.write_account()

    # 통장에 기록하기
    def write_account(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filepath, 'a') as f:
            f.write(f'{now} balance:{self.balance}\n')
        print(f'{self.balance}원을 통장에 기록했습니다.')

# 메인 프로그램
if __name__ == '__main__':
    account = BankAccount('./my_bank.txt')  # BankAccount 인스턴스 생성
    print(f'현재 잔액은 {account.balance}원입니다.')  # 현재 잔액 출력
    account.save()  # 저축하기
