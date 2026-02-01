class Demo:
    def __init__(self):
        self.No1 = 10   # public
        self._No2 = 20  # protected
        self.__No3 = 30 # private

obj = Demo()
print(obj.No1)
print(obj._No2)
print(obj.__No3)