def if_statement():
    """
    if - elif - else
    """

    """
    금액을 입력 받고
    금액이 10,000원 이상이면 by taxi
    금액이 2,000원 이상이면 by bus
    그 미만이면 on foot
    """

    money = int(input("동전 소리가 들리는 것 같은데? "))

    message = ""

    if money >= 10000:
        message += "택시 타도 될 것 같아!"
    elif money >= 2000:
        message += "그래도 버스는...!"
    else:
        message += "걸어가자."

    print(message)


def cond_expr():
    """
    조건 표현식
    """
    money = int(input("뛰어봐"))

    message = "오늘은 택시다" if money >= 10000 else "버스 타자" if money >= 2000 else ".."
    print(message)


def for_ex():
    """
    반복문 활용 패턴
    """
    # 기본적인 순회: for 타겟 변수 in 순차 자료형
    for animal in ['cat', 'dog', 'rabbit', 'tiger', 'fox']: # 순차형의 length 만큼 순회
        print(animal, end='\t') #sep=' ' (구분자), end='\n' (종결자)
    else:
        print()

    # 인덱스와 요소를 함께 받아올 때: enumerate
    for index, color in enumerate(['red', 'pink', 'sky blue', 'hot pink', 'green']):
        print(index, color)

    # continue: 남아있는 코드 실행 중단 -> 다음번 루프
    # break: 반복을 종료하고 바깥으로~~

    # 1~10 루프 중 짝수만 출력
    for i in range(1, 11):
        if i % 2 != 0:
            continue
        print(i, end=' ')
    else:
        print()

    # break
    r1 = list(range(1, 12, 2))
    print(r1)
    r2 = r1 + [12, 13, 15]
    print(r2)

    # 리스트 내부에서 짝수 찾으면 '미츠케' -> 루프 종료
    # 못찾으면 '미엔'
    for i in r1:
        if i % 2 == 0 :
            print("미츠케타!", i)
            break
    else:
        print('미엔데피엔')

    """
    while 반복조건:
        반복 코드
        - 반복 조건을 잘 제어해서 무한 루프에 빠지지 않도록 제어!
    """

def exex():
    for i in range(1, 10):
        print("")
        for x in range(1, 10):
            print(i * x, end=" ")
        else:
            print()
    else:
        print()

    i = int()

    while i < 6:
        i += 1
        x = int()
        while x < i:
            print("*", end='')
            x += 1
        else:
            print()
    else:
        print()


def list_comprehension():
    """
    리스트 내포
    Syntax: [표현식 for 타겟 in 순차 자료형]
    """
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 내부 요소 2배 list 만들기
    result = []
    for num in data :
        result.append(num * 2)

    print(data)
    print(result)

    result = [num * 2 for num in data]
    print(result)

    strings = ["a", "as", "bat", "car", "dove", "python"]
    # 문자열 리스트에서 문자열의 길이가 3 이상인 문자열 목록을 만들자
    result=[string.upper() for string in strings if len(string) >= 3]
    print(result)

    # 1~100 정수 중 3의 배수만 뽑아서 리스트 만들기
    result = [num for num in range(1, 101) if num % 3 == 0]
    print(result)


def set_conprehension():
    """
    set comprehension
    Syntax: {표현식 for 타겟변수 in 순차형 if 조건}
    """
    strings = ["a", "as", "bat", "car", "dove", "python"]
    # strings 에서 각 단어의 길이를 set 만들기
    lens = {len(s) for s in strings}
    print(lens)

def dict_comprehension():
    """
    dict comprehension
    Syntax : {키 표현식: 값 표현식 for 객체() in 순차 자료형 if 조건}
    """
    strings = ["a", "as", "bat", "car", "dove", "python"]
    # {"a":1, "as":2, ..., "python":6}
    len_dict = {s: len(s)for s in strings}
    print(len_dict)




if __name__ == "__main__":
    # if_statement()
    # cond_expr()
    # for_ex()
    # exex()
    # list_comprehension()
    # set_conprehension()
    dict_comprehension()