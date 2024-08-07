# Operator
# 기본적으로 하나의 py 파일은 그 자체가 모듈

def arith_oper():
    print("============산술 연산===============")
    print(7/3) # 파이썬 3 -> int / int -> float
    print(7//3) # 정수 나눗셈의 몫 연산자 //
    print(7%3) # 정수 나눗셈의 나머지 %

    # 나눗셈의 몫과 나머지를 동시에 구하기
    print(divmod(7,3)) # -> (2, 1) : Tuple
    data = divmod(7, 3)
    print("7 나누기 3의 몫은? ", divmod(7, 3)[0])
    print("7 나누기 3의 나머지는? ", divmod(7, 3)[1])

    print(7**3) # 지수승: 7의 3제곱
    print(pow(7, 3)) # 지수 함수: 7의 3제곱


def rel_oper():
    # pass # 함수 구현부 없어도 비워두면 안됨...
    print ("===== 비교 연산자 =====")
    # >, >=, <, <=, ==, !=
    s1 = "python"; s2 = "python"
    print("문자열의 비교: ", s1 == s2)

    # 복합 관계식
    a = 6
    # a 가 0 ~ 10 사이의 값일까?
    #  조건 1. a > 0
    #  조건 2. a < 10
    #  조건 1 and 조건 2
    print (0 < a and a < 10)
    print (0 < a < 10)

    # 다양한 자료 구조의 대소 비교가 가능
    print("문자열의 대소: ", "abcd" > "abd")
    print("튜플의 대소: ", (1, 2, 3) > (1, 2, 2, 1))

    # 동질성의 비교 ==, 동일성의 비교 is
    a = 10; b = 20; c = a
    print("a == b ?", a == b)
    print("a is b ?", a is b)
    print("a == c ?", a == c)
    print("a is c ?", a is c)
    print(s1 == s2)


import keyword # import 키워드 -> 모듈을 불러오는 명령어
def var_ex():
    print("==== 변수")
    # 문자, 숫자, _의 조합
    # 숫자로 시작하면 안됨
    # 예약어는 변수명으로 사용될 수 없다.
    # 파일명도 변수 명명 규칙에 맞추자
    print("예약어 목록: ", keyword.kwlist)
    print("예약어 갯구: ",len(keyword.kwlist))


def assignment_ex():
    print ("========= 치환문")
    # 변수 선언 절차 필요 없다
    print("name space: ", dir())
    a = 2024 # 첫 번째 할당이 발생할 때 name space에 추가
    b = a + 1
    print(a, b)
    print("name space: ", dir())

    # 여러 변수를 한꺼번에 할당
    c, d = 3.5, 5.3
    print("c, d = ", c, d)
    # 값의 교환 (swap)
    c, d = d, c
    print("c, d = ", c, d)

    # 같은 값을 동시 할당
    x = y = z = 10
    print(x, y, z)

    # 파이썬은 동적 타이핑 언어
    a = 2024 # 값이 할당될 때 타입이 결정됨 -> 타입이 뭔지 확인할 필요가 생김
    print(a, " is ", type(a)) # 현재 객체의 형식을 체크

    # 특정 객체인지 여부를 판단하는 함수 : isinstance
    print("a는 str의 객체일까?", isinstance(a, str))

    #확장 치환문: 산술, 비교 연산자 등은 확장 치환문으로 변경할 수 있다
    a = 10
    a += 10 # a = a + 10
    print(a)


def bool_ex():
    print("=========bool 연습")
    # 참(), 거짓()
    # 내부적으로 거짓은 0, 나머지는 모두 참으로 판정
    # 조건 분기, 흐름 제어 활용되기 때문에 중요홤
    #boolean 판정 ->
    #   논리 연산자, 비교 연산자의 결과
    #   boolean 객체 함수를 통해 얻을 수 있음
    print(bool(0))
    a = 2024
    print(a > 0) # 비교 연산자를 통한 논리값의 판정
    print(type(a))

    print(isinstance(True, bool)) # True
    print(isinstance(True, int)) # True
    print(True + True)

    # 데이터 자료의 형태에 의한 boolean 판정
    print(bool(2024), bool(0)) # int 값에 의한 boolean
    print(bool(3.14), bool(0)) # float 값에 의한 boolean
    print(bool("python"), bool("")) # str 값에 의한 boolean

    print(bool([1, 2, 3]), bool([])) # list 값에 의한 boolean
    print(bool({"key":"value"}), bool({})) # dict 값에 의한 boolean
    print(bool(None)) # None -> 비어있음 -> Java's null

    # 논리식의 계산 순서: Curcuit Break
    # or 일 경우, 첫 번째 True 연산 결과를 취한다
    # and 일 경우, 둘 다 True면 뒤쪽 결과를 취한다
    # and 인 경우, 전체 논리식이 거짓이라면 None을 반환...
    print("CB 1: ", [] or "logical") # F or T
    print("CB 2: ", "logical" or "operator") # T or T
    print("CB 2-1: ", "logical" and "operator") # T and T
    print("CB 3: ", '' or "operator")  # F and T
    print("CB 3-2: ", '' and "operator")  # F and T
    print("CB 4: ", None and 1)  # F and T
    print("CB 5: ", None or [])  # F or F


def type_hint():
    # 파이썬은 동적 타이핑 언어 -> 변수의 타입을 명시적으로 지정하지 않음
    # 3.5 ~ 타입 힌트를 이용, 타입 체크를 진행할 수 있다!
    def add(a: int, b: int) -> int:
        return a + b
    print(add(10, 20))
    #print(add("python", 3.10))

    def greet(name: str) -> str: # str 입력 받아서 str 리턴하는 함수
        return 2024
        # return "Hello, " + name

    untyped = "string" # 타입 힌트가 적용되지 않은 변수
    print(untyped)
    print(greet(untyped))
    untyped = 2024

    typed: str = "string" # 타입 힌트가 적용된 변수
    print(typed)
    typed = 2024
    print (typed)
    print(greet(typed))


def int_ex():
    print("================== 정수형 연습!")

    a = 2024 # 리터럴 선언
    b = int(2024) # 타입 함수 사용

    print(a, "is", type(a))
    print(b, "is", type(b))

    # 2진, 8진, 16진 정수 표현 가능
    b = 0b1101 # 0b
    o = 0o23 # 0o
    x = 0xFF # 0x
    print(b, o, x)

    # 파이썬 3에서는 int / long 구분 없음
    # long 형 데이터 저장 크기 64bit 초과해서 적재할 수 있대
    i = 2 ** 2048
    print(i)
    print(i.bit_length())

    # 진법 변환 함수
    i = 48
    print(i, bin(i), oct(i), hex(i))


def float_ex():
    print("=======================실수형 연습..")

    a = 3.141592 # 리터럴로 생성
    print(a, "is", type(a))
    print(isinstance(a, float)) # a 는 float 인가

    b = float(3.00) # 타입 함수로 생성
    print(b, "is", type(b))
    print(isinstance(b, float))
    print(a.is_integer(), b.is_integer())

    # 지수 표기법으로도 확인 가능함
    c = 3e3 # 3 * 10 ** 3
    d = -2E-5 # -2 * 10 ** -5
    print(c, d)
    print(-2E-5 == -0.00002) # 같은 표현


def complex_ex():
    print("==========복소수 연습;;")
    # 복소수: 실수부 + 허수부j
    a = 4 + 5j
    print(a, "is", type(a))
    print(isinstance(a, complex))
    b = 3 - 2j
    print(a + b) # 복소수는 산술 연산이 가능
    print(b.real, b.imag) # 실수부, 허수부
    print(a, "의 켤레 복소수는 ", a.conjugate())



if __name__ == "__main__":
    # 다른 모듈로 import 되는 경우 __name__ == "python_basics"
    # 직접 실행될 경우 (최상위 모듈일 경우) __name__ == "__main__"
    # arith_oper() # 산술 연산자 연습
    # rel_oper() # 비교 연산자 연습
    # var_ex() # 변수 연습
    # assignment_ex() # 변수 치환 연습
    # bool_ex() #
    # type_hint() # 타입 치환
    # int_ex()
    # float_ex()
    complex_ex()