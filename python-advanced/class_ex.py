class MyString(str): # 스트링 객체를 상속 받은 새로운 클래스
    pass

s = MyString()
print(s, ", type:", type(s))

s = MyString('My Class')
print(MyString.__bases__) # MyString 의 부모
print(MyString.__bases__[0].__bases__) # MyString의 첫 부모의 부모

# s 의 부모는 str 이므로 str의 모든 메서드를 활용할 수 있다
print(s.lower())

class myobj:
    pass


class Chimera(str, myobj):
    pass


print(type(Chimera))
print(Chimera.__bases__)

print(issubclass(Chimera, str)) # 서브 클래스 여부 확인


from point import Point
p = Point()
p.setX(4)
p.setY(5)
print(p, type(p), "x=", p.getX(), "y=", p.getY())