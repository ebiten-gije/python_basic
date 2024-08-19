def define_tuple():
    """
    튜플의 정의
    tuple: 리스트와 거의 동일하지만, 변경 불가한 자료형(immutable)
        len, index, slicing, 연결, 반복, 포함 여부
        내부 요소 변경은 불가능,,,
    """
    tp1 = () # 공 튜플 -> 타 순차형을 튜플로 변환하고자 할 때 쓸 수 있을 수도
    tp2 = tuple()
    print(tp1, type(tp1))
    print(tp2, type(tp2))

    tp3 = (3,) # 요소가 한 개일 경우, 요소 뒤에 "," 찍어줘야함
    print(tp3, type(tp3))


def tuple_oper():
    """
    튜플 연산
    """
    tp = (1, 2, 3, 4, 5)
    # 길이를 구할 수 있음
    print(tp, "length:", len(tp))
    # 순서 있는 자료형
    print(tp[-3], tp[-2], tp[-1], # 역방향 인덱싱
          tp[0], tp[1], tp[2], tp[3]) # 정방향

    # 슬라이싱: [시작경계:끝경계[:간격]]
    slice = tp[1:4]
    print(slice, type(slice))
    slice = tp[:]
    print(slice, type(slice)) # 처음과 끝은 생략 가능 -> 튜플 전체

    # 반복
    print(tp * 3)

    # 연결
    print(tp + (6, 7, 8, 9, 10))

    # 포함 여부: in, not in
    print(5 in tp)
    print(1 not in tp)


def tuple_assign():
    """
    튜플의 할당
    """
    # 튜플을 이용해서 좌우변에 여러 값을 동시에 할당
    x, y, z = 10, 20, 30 # 튜플
    print(x, y, z)

    # 튜플을 이용한 swap (값 교환)
    x, y = 10, 20
    print(x, y)
    x, y = y, x # 튜플을 이용한 교환
    print(x, y)


def tuple_method():
    """
    튜플의 메서드들
    """
    tp = (20, 30, 10, 12, 20)
    print("count:", tp.count(20)) # 특정 요소 갯수

    print("index:", tp.index(20)) # 요소 인덱스
    print("index:", tp.index(20, 1))


def packing_unpacking():
    """
    튜플의 패킹와 언패킹
    """
    # 튜플의 packing
    tp =(10, 20, 30, 'python') # 기본적으로 튜플을 만드는 방법
    print(tp, type(tp))
    tp = 10, 20, 30, 'python' # 값만 나열해도 자동으로 튜플,,,로 인식!
    print(tp, type(tp))

    # 기본 unpacking
    a, b, c, d = tp
    print(a, b, d, c)

    # a, b, c = tp # 변수의 갯수가 적음 -> ValueError
    # a, b, c, d, e = tp # 변수가 많음 -> ValueError

    # 확장 unpacking
    a, b, *c = tp # 확장 unpacking 기호 "*"
    print(a, b, c, type(c))

    *a, b = tp
    print(a, type(a))
    print(b, type(b))

    a, *b, c = tp
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))


if __name__ == "__main__":
    # define_tuple()
    # tuple_oper()
    # tuple_assign()
    # tuple_method()
    packing_unpacking()