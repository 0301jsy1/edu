import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius # __ : private로 선언
        #raise TypeError("양수를 넣으세요.")  #raise : 예외처리
    def get_area(self):
        return math.pi*(self.__radius**2)
    @property
    def radius(self): #선언된 private는 간접적으로 접근해야 함
        return self.__radius
    @radius.setter
    def radius(self,value):
        if value<=0:
            self.__radius=10
        else:
            self.__radius=value 
            

circle = Circle(-5)
circle.radius=10
circle = Circle(-5)
print(circle.get_area())
print(circle.radius)