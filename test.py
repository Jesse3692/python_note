from abc import ABCMeta, abstractmethod


class Pursuit:
    """追求者
    """

    def __init__(self, name):
        self.name = name

    def give_flowers(self):
        print(self.name + '送你鲜花')
        return self.name + '送你鲜花'

    def give_chocolate(self):
        print(self.name + '送你巧克力')
        return self.name + '送你巧克力'

    def give_dolls(self):
        print(self.name + '送你洋娃娃')
        return self.name + '送你洋娃娃'


class Proxy(Pursuit):
    """代理者
    """

    def __init__(self, name):
        self.name = name
        self.pursuit = Pursuit(name)

    def sgive_flowers(self):
        print(self.name + '代理送你鲜花')
        return self.pursuit.give_flowers()

    def sgive_chocolate(self):
        print(self.name + '代理送你巧克力')
        return self.pursuit.give_chocolate()

    def sgive_dolls(self):
        print(self.name + '代理送你洋娃娃')
        return self.pursuit.give_dolls()


class Gril:
    def __init__(self, name, gift):
        self.name = name
        self.gift = gift


if __name__ == '__main__':
    proxy = Proxy('小王')
    proxy.sgive_flowers()
