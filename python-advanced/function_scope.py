# 함수 스코핑 롤
x = 1


def scope_func(a):
    print(locals())
    return a + x  # a 는 외부로부터 전달된 파라미터, x 는 글로벌 영역의 데이터


print(scope_func(10))


def scope_func2(a):
    x = 2
    print(locals())
    return a + x


print(scope_func2(10))

print("global x:", x)  # global x 는 변경되지 않음

# 함수 내부에서 전역 객체를 사용할 필요가 있다면 함수 내부에 global 기워드를 사용할 수 있다
g = 1


def scope_func3(a):
    global g  # 함수 내부에서 사용할 변수 g 는 글로벌이다
    g = 3
    print(locals())
    return a + g


print(scope_func3(20))
print("global g:", g)

# local 확인 : locals()
# global 영역 확인 : globals(), dir() 함수
print(dir())
# builtin 영역 확인
print(dir('__builtin__'))