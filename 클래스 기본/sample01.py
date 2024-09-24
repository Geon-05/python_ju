'''
참고사이트:
https://datascienceschool.net/01%20python/02.12%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D.html
'''

class Product: 
    def __init__(self, n, p, s): 
        self.name, self.price, self.stock = n, p, s

    def information(self): 
        print('상품 이름 : ', self.name)
        print('상품 가격 : ', self.price)
        print('남은 재고 : ', self.stock)

class Member: 
    def __init__(self, n, d): 
        self.name, self.join_date = n, d
        self.purchase_list = []
        self.purchase_amount = 0

    def information(self): 
        print('회원 이름 :', self.name)
        print('가입 날짜 :', self.join_date)
        print('구매 내역 :', self.purchase_list)
        print('누적 구매금액 :', self.purchase_amount)

    # Product 객체가 인자로 전달됨
    def buy(self, product, count): 
        print(self.name, '고객님이', product.name, count, '개 구매!')
        product.stock -= count     # 구매 개수만큼 상품 재고 감소
        self.purchase_list.append(product.name) # 구매내역에 상품 추가
        self.purchase_amount += (product.price * count) # 누적 구매금액 수정
# 물건 등록
socks = Product('socks', 1000, 10)
books = Product('books', 17500, 15)

# 회원가입
Anna = Member('Anna', '20200420')
Grace = Member('Grace', '20200130')


Anna.buy(socks, 1)
Anna.information()

socks.information()

Grace.buy(books, 2)
books.information()
Grace.information()

# 새로운 물건 입고
pen = Product('pen', 1200, 25)
Anna.buy(pen, 5)
Anna.information()