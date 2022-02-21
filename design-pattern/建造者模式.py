class Burger:
    """主食类，价格名字
    """
    name = ''
    price = 0.0

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class ChesseBurger(Burger):
    """奶酪汉堡
    """

    def __init__(self):
        self.name = "chesse burger"
        self.price = 10.0


class SpicyChickenBurger(Burger):
    """香辣鸡汉堡
    """

    def __init__(self) -> None:
        self.name = "spicy chicken burger"
        self.price = 15.0


class Snack:
    """小食类价格以及名字
    """
    name = ''
    price = 0.0
    type = 'SNACK'

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Chips(Snack):
    """炸薯条
    """

    def __init__(self):
        self.name = 'chips'
        self.price = 6.0


class ChickenWings(Snack):
    """鸡翅
    """

    def __init__(self):
        self.name = 'chicken wings'
        self.price = 12.0


class Beverage:
    """饮料
    """
    name = ''
    price = 0.0
    type = 'BEVERAGE'

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name


class Coke(Beverage):
    """可乐
    """

    def __init__(self):
        self.name = 'coke'
        self.price = 4.0


class Milk(Beverage):
    """牛奶
    """

    def __init__(self) -> None:
        self.name = 'milk'
        self.price = 5.0


class Order:
    """订单对象，一个订单中包含一份主食，一份小食，一份饮料
    """
    burger = ''
    snack = ''
    beverage = ''

    def __init__(self, order_builder) -> None:
        self.burger = order_builder.b_burger
        self.snack = order_builder.b_snack
        self.beverage = order_builder.b_beverage

    def show(self):
        print('Burger:%s' % self.burger.get_name())
        print('Snack:%s' % self.snack.get_name())
        print('Beverage:%s' % self.beverage.get_name())


# 建造者
class OrderBuilder:
    """
    OrderBuilder就是建造者模式中所谓的“建造者”，
    将订单的建造与表示相分离，以达到解耦的目的。
    在上面订单的构建过程中，如果将Order直接通过参数定义好（其构建与表示没有分离），
    同时在多处进行订单生成，如果此时需要修改订单内容，则需要一处处去修改，业务风险提高了不少。
    """
    b_burger = ''
    b_snack = ''
    b_beverage = ''

    def add_burger(self, x_burger):
        self.b_burger = x_burger

    def add_snack(self, x_snack):
        self.b_snack = x_snack

    def add_beverage(self, x_beverage):
        self.b_beverage = x_beverage

    def build(self):
        return Order(self)


# Director类
class OrderDirector:
    """
    在建造者模式中，还可以加一个Director类，用以安排已有模块的构造步骤。
    对于在建造者中有比较严格的顺序要求时，该类会有比较大的用处。
    """
    order_builder = ''

    def __init__(self, order_builder) -> None:
        self.order_builder = order_builder

    def create_order(self, burger, snack, beverage):
        self.order_builder.add_burger(burger)
        self.order_builder.add_snack(snack)
        self.order_builder.add_beverage(beverage)
        return self.order_builder.build()


# 场景实现
if __name__ == '__main__':
    order_builder = OrderBuilder()
    order_builder.add_burger(SpicyChickenBurger())
    order_builder.add_snack(Chips())
    order_builder.add_beverage(Milk())
    order_1 = order_builder.build()
    order_1.show()
