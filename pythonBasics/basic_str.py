def define_str():
    """
    함수 정의 연습 ?
    """
    # 문자열의 정의
    # 한 줄 문자열(): ("), (') 모두 가능
    s1 = "Hello Python" # 리터럴
    s2 = str("Hello Python") # 타입 함수 사용
    s3 = str(3.141592) # 다른 타입을 변환 생성

    print("s1 은 str?", isinstance(s1, str))

    # 여러 줄 문자열: """, '''
    s4 = """Life is too short, You need Python.
 파이썬은 데이터 처리가 중요한 시대에서
가장 널리 사용되는 언어 중 하나라고 하더라"""

    print(s4)

    # 여러 줄 문자열은 한 줄 주석만 있는 파이썬에서
    # 여러 줄 주석을 사용하고자 할 때도 사용할 수 있다
    """여러 줄 문자열을 사용한 여러 줄 주석
    메서드 정의 바로 아래 여러 줄 주석을 추가하면
    문서화할 때 이용될 수 있고, 
    help 명령어로 해당 메서드의 주석을 볼 수 있다.
    docstring 이라 한다."""

    # f-string 문자열 포맷팅 방식 중 하나
    name, age = "스즈", 28
    message = f"안녕하세요, 제 이름은 {name}, {age}살입니다"
    print(message)

    width, height = 10, 5
    message = f"사각형의 면적은 {width * height}입니다"
    print(message)


def string_open():
    """
    문자열 련산
    """
    # 길이를 잡을 수 있다, len(), 인덱싱/슬라이싱 가능, 포함여부 판별 가능,,
    # immutable 이기에, 치환 불가능함
    str1 = "적당한 길이의 문자열"
    str2 = "Second String"
    print(len(str1), len(str2))

    # 인덱싱
    print(str1[0], str1[1], str1[2], "...", str1[8], str1[9], str1[10])
    print(str1[-1], str1[-5])

    # 문자열은 immutable -> 치환 불가
    # str1[0] = "당" # 변경 불가

    # 슬라이싱 [시작 경계 : 끝 경계[:간격]]
    print(str1)
    print(str1[4:7])
    print(str1[-7:-4])

    print(str1[0:3])
    print(str1[:3]) # 시작부터는 생략 가능

    print(str1[8:len(str1)])
    print(str1[8:]) # 끝까지도 생략 가능

    print(str2[::2]) # 2칸 간격으로 뽑기
    print(str1[::-1]) # 간격이 음수면 역방향


def transform_methods():
    """
    대소문자 변환 관련 연습
    """
    s = "i liKe pYthOn"
    print("UPPER: ", s.upper()) # 모두 대문자
    print("LOWER: ", s.lower()) # 모두 소문자

    print("CAPITALIZE: ", s.capitalize()) # 첫 글자만 대문자
    print("TITLE: ", s.title()) # 각 단어의 첫 글자만 대문자로

    print("SWAPCASE: ", s.title().swapcase()) # 대문자와 소문자를 바꿈

    # 불변 자료 -> 원본은 바뀌지 않음..
    print(s)


def search_methods():
    """
    문자열 검색 관련 예제
    :return:
    """
    s = "I Like Python, I Like Java Also"
    print("count: ", s.count("Like")) # 문자열 내부 Like 의 갯수

    # Like 찾기
    index = s.find("Like") # 문자열 내부 첫 번째 Like
    print("first find: ", index)
    index = s.find("Like", 3) # 인덱스 _start 부터 검색
    print("second find: ", index)
    index = s.find("Like", 20)
    print("third fine: ", index) # 없으면 -1로 반환

    # Like 찾기: index
    print("first index: ", s.index("Like"))
    print("second index: ", s.index("Like", 5))
    # print("third index: ", s.index("Like", 21)) # 찾는게 없으면 에러;;
    # 방법 1. 예외 처리
    # 방법 2. 먼저 검색어 포함 여부를 확인 후 검색
    if "Like" in s[21:]: # 포함 여부
        print("third index: ", s.index("Like", 21))
    else:
        print("Like 없는 것 같은데?ザコ")

    # 역방향 검색..! find
    print("Rfind: ", s.rfind("Like"))
    print("Rfind: ", s.rfind("Like", 0, 17  ))

    # 문자열이 특정 문자열로 시작되는가?
    url = "http://www.naver.com"
    surl = "https://www.google.com"
    ftp = "ftp://ftp.naver.com"

    print("Startswith: ", url.startswith("http://"))
    print("StartsWith: ", surl.startswith("https://"))
    print("STARTSWITH: ", ftp.startswith(("http://", "https://")))

    # 문자열이 특정 문자열로 끝나는가?
    print("endswith: ", url.endswith("naver.com"))
    print("Endswith: ", surl.endswith("naver.com"))

    # startswith, endswith 에서 검색 범위 제한
    print("STARTSWITH: ", ftp.startswith("ftp.", 6, len(ftp)))


def modify_replace_methods():
    """   문자열 수정, 치환 관련 메서드..연습
    """
    s = "        Alice and the Heart Queen        "
    print("STRIP: [", s.strip(), "]", sep="")
    print("LSTRIP: [", s.lstrip(), "]", sep="")
    print("RSTRIP: [", s.rstrip(), "]", sep="")

    s = "----------------------Alice and the heart queen---"
    print("strip -:[", s.strip("-"), "]", sep="")

    s = "I like Java"
    # Java -> Python
    print("REPLACE: ", s.replace("Java", "Python"))
    print("원본: ", s) # str 은 immutable -> 변경되지 않음..


def align_methods():
    """
    문자열 정렬 관련 메서드
    """
    s = "Alice and the Heart Queen"
    print("CENTER:[", s.center(60), "]", sep="")
    print("CENTER:[", s.center(60, "*"), "]", sep="")
    print("LJUST: [", s.ljust(60, "*"), "]", sep="")
    print("RJUST: [", s.rjust(60, "*"), "]", sep="")

    print("ZFILL: ", "1234".zfill(5)) # 5자리 확보 후 내용을 채우고 빈 공간은 0으로 채움
    print("ZFILL: ", "123456".zfill(5)) # 확보한 5자리는 최소 공간, 넘쳐도 잘리지는 않음


def split_join_method():
    """
    문자열 분할과 합치기 메서드
    """
    s = "Ham and Cheese and Breads and Ketchup"
    print("split: ", s.split()) # 공백 문자 기준으로 문자열 분리

    ingr = s.split(" and ") # " and "를 기준으로
    print("split: ", ingr)
    print("JOIN: ", ", ".join(ingr)) # ingr 리스트를 , 를 중심으로 합치기

    print(s.split(" and ", 2)) # 앞에서 2개만 분리
    print(s.rsplit(" and ", 2)) # 뒤에서 2개만


    #  줄 단위 구분: split("\n)과 동일
    lines = """\
    Java Programming
    Python Programming
    HTML Coding
    """
    print("split: ", lines.split())
    print("split: ", lines.split("\n"))

    print("split lines: ", lines.splitlines(True)) # 개행 문자 유지
    print("split lines: ", lines.splitlines(False)) # 개행 문자 유지하지 않음


def check_method():
    """문자열 (str) 데이터의 형태 판별"""
    print("1234".isdigit()) # 숫자 형태야?
    print("ABCD".isalpha()) # 알파벳?
    print("python3".isalnum()) # 숫자 + 알파벳?
    print("python 3".isalnum()) # 공백..
    print(" \r\n\t".isspace()) # 공백 문자? 스페이스, 개행, 탭 등 모두 공백 문자이다
    print("".isspace())

    print("PYTHON".isupper())
    print("python".islower())
    print("Python Programming".istitle())


def string_format():
    """
    문자열 포매팅
    """
    # c 스타일 문자열 포캣
    # %s, %c, %d, %f, %x, %o, %%(%출력)
    fmt = "%d개의 %s 중에서 %d개를 먹었다"
    print(fmt %(10, "사과", 10))

    print("현재 이자율은 %f%%입니다" % 3.4)
    print("현재 이자율은 %.2f%%입니다" % 3.4)

    # named formatting
    fmt = "%(total)d개의 %(fruit)s 중에서 %(eat)d개를 먹었다"
    print(fmt % {"total": 10, "fruit": "배", "eat": 5})
    print(fmt % {"fruit": "귤", "eat": 4, "total": 15})

    # format 메서드
    fmt = "{}개의 {} 중에서 {}개를 먹었다"
    print(fmt.format(10, "사과", 4))
    print("{0}개의 {1} 중에서 {2}개를 먹었다".format(10, "배", 1))

    # placeholder named parameter
    fmt = "{total}개의 {fruit} 중에서 {eat}개를 먹었다"
    print(fmt.format(total = 13, eat = 10, fruit = "메론"))

    # dict 작성된 데이터가 있을 경우: format_map
    data = {"total": 10, "eat": 12, "fruit": "복숭아"}
    print(fmt.format_map(data))

    # f-string
    # 포맷팅 문자열 앞에 f
    # {} 내부에 데이터, 변수명, 표현식 -> 해당 결과 바인딩 -> 최종 출력물
    total, fruit, eat = 10, "자두", 4
    print(f"{total}개의 {fruit} 중에서 {eat} 개를 먹엇따")
    # 플레이스 홀더 내부의 연산식 활용 가능
    total, fruit, eat = 10, "apple", 4
    print(f"{total}개의 {fruit.upper()} 중에서 {eat} 개를 먹어서 {total - eat}개가 남으미")


if __name__ == "__main__":
    # define_str()
    # string_open()
    # transform_methods()
    # search_methods()
    # modify_replace_methods()
    # align_methods()
    # split_join_method()
    # check_method()
    string_format()