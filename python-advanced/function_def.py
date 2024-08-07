def dummy():
    # 함수 구현부가 없더라도 비워두면 안돼
    pass


def times(a, b):
    return a * b


# 매개변수의 유무, 출력의 유무에 따라서 4가지 형태로 구분
# return문
    # 기본적으로 함수를 종료하고, 함수 호출 지점으로 돌아감
    # 돌려줄 출력 값이 있을 경우 return 뒤에 데이터를 명시

def none():
    return # 출력 없이 return 문만 있을 경우, none이 반환됨


print(none())
# 함수도 객체
    # 다른 객체와 동등한 권리를 갖는다
    # - 변수에 할당될 수 있고
    # - 다른 함수의 매개변수로 전달될 수 있다
    # - 함수의 결과로 반환될 수 있다

fun = times # 변수에 할당
print(fun, type(fun))
# 실행 가능 객체인지 확인 -> callable
print(callable(fun)) # fun 은 실행 가능한?

if callable(fun):
    print(fun(38, 76))