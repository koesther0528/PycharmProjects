class Icecream:

    def __init__(self, name): #생성자. 주로 변수 초기화
        self.name = name

    def set_explanation(self, explanation):
        self.explanation = explanation

    def __str__(self): #객체를 알아보기 쉽게 문자열로 return. 주로 print()에서 호출
        return f'이름:{self.name}'

class Order:
    _CATEGORIES = ['싱글레귤러', '더블레귤러', '파인트']
    _PRICES = (3200, 6200, 8200)

    def __init__(self):
        self.set_cateries()
        self.menu = []
        self.init_menu()
        self.order_menu = []

    def __str__(self):
        pass

    def set_cateries(self):
        for index, category in enumerate(Order._CATEGORIES):
            print(index+1, category)
        category_num = input('종류를 골라주세요: ')
        self.category = int(category_num)

    def init_menu(self):
        self.menu.append(Icecream('이상한나라의솜사탕'))
        self.menu.append(Icecream('뉴욕치즈케이크'))
        self.menu.append(Icecream('트리플민초'))

    def show_menu(self):
        for index, icecream in enumerate(self.menu):
            print(f'{index + 1}.{icecream}')

    def order(self):
        self.show_menu()
        for i in range(self.category):
            icecream = input('아이스크림을 골라주세요: ')
            icecream = int(icecream)
            self.order_menu.append(self.menu[icecream - 1])
        print('-'*10 + '주문 내역입니다' + '-'*10)
        print(Order._CATEGORIES[self.category - 1])
        print(str(Order._PRICES[self.category - 1]) +'원')
        for icecream in self.order_menu:
            print(icecream)
order = Order()
order.order()

