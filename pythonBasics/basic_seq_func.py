def using_range():
    """
    range 객체 : 범위 객체
    - 범위 정보만 가지고 있따가 요청할 때, 조건을 바탕으로 계산한 결과를 반환
    - 큰 범위의 데이터를 생성해도 메모리가 증가하지 않음: Generator
        syntax: range([start=0, ] end [, step=1])
    """
    # 인자 값이 1개 -> 끝값
    seq = range(10) # 10은 범위에 포함되지 않음
    print(seq, type(seq))
    print(list(seq))

    # 인자값이 2개 -> 시작값, 끝값
    seq2 = range(2, 10) # 2 이상, 10 미만
    print(seq2, list(seq2))
    print()

    # 인자값이 3개? -> 시작, 끝, 간격
    seq3 = range(0, 10, 2) # 0 이상, 10 미만, 2칸
    print(seq3, list(seq3))
    print()

    # 큰수 -> 작은 수: 간격값을 음수로
    seq4 = range(0, -10, -1)
    print(seq4, list(seq4))
    print()

    # range 도 순차 자료형: len, 인덱싱, 슬라이싱, in, not in 가능
    print(seq, "Length:", len(seq))
    print(5 in seq) # 포함 여부 확인
    print(seq[-3], seq[-2], seq[-1], # 역방향
          seq[0], seq[1], seq[2], seq[3]) # 정방향

    # range는 변경 불가 자료형
    # seq[0] = 10 # error
    # 슬라이싱은 가능하지만, 치환은 불가능함
    print(list(seq[4:8]))

    # 예) 1부터 10까지 2간격으로 루프 돌릴 때
    for i in range(1, 11, 2):
        print(i, end="\t")
    else:
        print()

def using_enumerate():
    """
    enumerate 함수
    : 순차 자료형을 인덱스와 함께 tuple로 출력하는 함수 : generator
        주로 순차 자료형에서 아이템과 아이템의 인덱스를 함께 활용하고자 할 때 사용
    """
    colors=["red", "yellow", "blue", "green", "white", "black", "pink"]
    # 루프 돌리면서 인덱스와 함께 출력하고자 할 때.
    i = 0
    for color in colors:
        print("color {0}: {1}".format(i, color))
        i +=1

    for i, value in enumerate(colors): # (인덱스 정보, 요소값)
        print("color {0}: {1}".format(i, value))


def using_zip():
    """
    zip: 여러 시퀀스 자료를 동시에 루프, 튜플로 생성해주는 Generator
    """
    eng = ["Sunday", "Monday", "Tuesday", "Wednesday"]
    kor = ["일요일", "월요일", "화요일", "수요일", "목요일"]
    engkor = zip(eng, kor)
    print(engkor, type(engkor))

    # 기본 순회
    for pair in engkor:
        # print(pair, type(pair))
        print(f"영어 {pair[0]} -> 한국어 {pair[1]}")

    # 한번 순회 돌면 zip객체는 비어버림;;
    engkor = zip(eng, kor)

    # Unpacking
    for eng, kor in engkor:
        print(f"영단어 {eng}는 한국어로 {kor}입니다")


if __name__ == "__main__":
    # using_range()
    # using_enumerate()
    using_zip()