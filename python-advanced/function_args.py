# 함수의 매개변수
# 기본적으로 필요한 만큼 선언할 수 있다


def sum_val(a, b):
    return a + b


def incr(a, step=1): # 두번째 인수 (step)은 기본 값이 있다
    return a + step


print(sum_val(1, 3))
print(incr(3)) # 두번째 인수가 부여되지 않으면 기본값을 활용
print(incr(3, 3)) # 기본 값을 무시하고 값을 부여해 활용


# 키워드 인수
def area(width, height):
    return width * height


print(area(4, 3)) # 설계된 매개변수 순서대로 호출
print(area(height=3, width=4)) # 매개변수의 이름으로 변수 지정하여 삽입
print(area(width=4, height=3)) # 호출 순서는 중요하지 않음


# 가변 인수 : 정해지지 않은 갯수의 매개변수 -> 매개변수 앞에 *
def get_total(*args): # args -> 정해지지 않은 갯수의 매개 변수
    total = 0
    for x in args:
        if isinstance(x, (int, float)):
            total += x
    return total


print(get_total(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(get_total(1, 4, 2, 3, 5))
print(get_total(1, 2, 3, 4, 5, "a", 6, 7, 8, 9, 10)) # error


# 키워드 인수 : **
# 함수에 고정인구, 가변인수, 키워드 인수
# 선언부에 고정인수, 가변인수, 키워드 인수 순으로 선언해야 함

def func_args (a, b, *args, **kwd):
    print("고정인수:", a, b)
    print("가변인수:", args, type(args))
    print("키워드인수:", kwd)


func_args(10, 20, 30, 40, 'a', option1='texas', option2='kw')