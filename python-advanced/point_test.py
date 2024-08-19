from point import Point
def bound_instance_method():
    """
    bound instance method: 인스턴스 직접 바인딩된 메서드
    """
    p = Point() # Point 인스턴스 생성
    p.setY(20)
    p.setX(10)

    print(p.getX(), p.getY(), sep=', ')
    print(p.getX, p.getY)


def unbound_instance_method():
    """
    언바운드 메서드:
        클래스 메서드에 인스턴스 참조 주소를 전달해 우회접근하는 방법
        인스턴스 메서드의 첫 번째 인자가 self 인 이유
    """
    p = Point()
    Point.setX(p, 10)
    Point.setY(p, 20)
    print(Point.getX(p), Point.getY(p), sep=", ")
    print(Point.getX, Point.getY)


def class_member_test():
    p1 = Point()
    p1.setX(10)
    p1.setY(20)
    print(p1.getX(), p1.getY(), p1.instance_count)
    # p1.instance_count 는 클래스 맴버(인스턴스 맴버 아님)

    p2 = Point()
    p2.setX(20)
    p2.setY(30)
    print(p2.getX(), p2.getY(), p2.instance_count)
    # p2.instance_count 는 클래스 맴버

    print(p1.x is p2.x)
    print(p1.instance_count is p2.instance_count)


def constructor_test():
    p1 = Point(10, 20)
    print("instance count:", Point.instance_count)
    p2 = Point() # 생성자의 기본값이 활용
    print("instance count:", Point.instance_count)
    p3 = Point(30, 40)
    print("instance count:", Point.instance_count)

    del p1
    del p2

    print("instance count:", Point.instance_count)


def stringify():
    p = Point(10, 20)
    print(p) # 문자열화 -> __str__ 이 호출
    print(repr(p)) # 문자열화 -> 원래 객체를 재현할 수 있는 문자열

    p_repr = eval(repr(p))
    print(p_repr)

    print(p.x == p_repr.x)
    print(p.y == p_repr.y)


from point import Singleton
def singleton_test():
    s = Singleton()
    print(s)
    # s2 = Singleton()  # 예외 발생
    s2 = Singleton.getClassInstance()
    print(s2)

    # s, s2 동일 객체인가
    print(s is s2)


def oper_overriding():
    # 산술연산자 오버로딩
    print(Point(10, 20) + Point(30, 40))
    print(Point(10, 20) + 30)

    # 역이항 산술연산자 오버로딩
    print(30 + Point(10, 20))
    print(Point(30, 40) + Point(10, 20))

    print(Point(10, 20) == Point(10, 20))
    print(Point(10, 20) == Point(30, 40))

if __name__ =="__main__":
    # bound_instance_method()
    # unbound_instance_method()
    # class_member_test()
    # constructor_test()
    # stringify()
    # singleton_test()
    oper_overriding()