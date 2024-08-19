def write_file():
    """
    파일에 텍스트 저장
    : 문장 1개 -> ./sample/test.txt 에 기록
    : open(파일명, 파일 모드, encoding)
    : 액션 모드: r(read), w(write), a(append)
    : 형식 모드: t(text: default), b(binary)
    """
    f = open("./sample/test.txt", 'wt', encoding="UTF-8")
    write_size = f.write('Life is short, You need Nintendo') # 기록한 컨텐츠의 길이를 반환
    print('기록된 길이:', write_size)


def write_file2():
    """
    여러 줄 -> ./sample/multilines.txt
    """
    f = open("./sample/multilines.txt", "wt", encoding="UTF-8")
    for i in range(1, 11):
        f.write(f'Line {i}\n')
    f.close()


def read_file():
    """
    ./sample/multilines.txt 읽어오기
    """
    f = open("./sample/multilines.txt", encoding="UTF-8")
    text = f.read() # 콘텐츠 전체 -> 내용이 많으면 메모리 부하++
    print(text)
    f.close()


def read_file_by_line():
    """
    ./sample/multilines.txt 한 줄 단위로 읽어, 메모리 부하 --
    """
    f = open("./sample/multilines.txt", 'rt', encoding="UTF-8")
    while True:
        line = f.readline() # 한 줄 읽어오기
        if not line: # 더 읽을 것이 있나?
            break
        print(line)
    f.close()


def read_file_readlines():
    with open("./sample/multilines.txt", "rt", encoding="UTF-8") as f:
        lines = f.readlines()
        # print(lines)
        for line in lines:
            print(line.strip())


def copy_binary_file():
    """
    이진 파일을 읽거나 쓰기 위해서는 모드를 b로 설정
    : ./sample/rose-flower.jpeg -> rose-flower-copy.jpeg로 복사
    """
    # 읽어오기
    with open("./sample/rose-flower.jpeg", "rb") as f:
        data = f.read()
        print(type(data), "length:", len(data))

    # 저장하기
    with open("./sample/rose-flower-copy.jpeg", "wb") as f:
        f.write(data)

    print("파일 복제 성공")


import pickle
def serialize():
    """
    pickle 모듈의 dump 메서드를 이용한 직렬화
    """
    with open("./sample/players.bin", "wb") as f:
        pickle.dump({"baseball", 9}, f, 1) # dump(객체, 파일 포인터, 프로토콜 버전)
        pickle.dump({"basketball", 5}, f, pickle.HIGHEST_PROTOCOL) # 최신 피클 버전
        pickle.dump({"soccer", 11}, f) # 위와 동일

    print("직렬화 완료래")


def deserialize():
    """
    pickle 역직렬화 load, 프로토콜 버전은 명시 안해도 됨
    """
    data_list = []
    with open('./sample/players.bin', 'rb') as f:
        # print(pickle.load(f))
        # print(pickle.load(f))
        # print(pickle.load(f))
        # print(pickle.load(f))
        while True : # 몇개인지 모르니까 루프
            try:
                data = pickle.load(f)
            except EOFError: # 피클이 없다면
                break
            data_list.append(data)

    print("역직렬화 결과>", data_list)


"""연습
- sangbuk.csv -> 읽어서
', '를 기준으로 분할
- 한 개 레코드를 dict으로 만들기
    예) {"name":채치수, "backno":4, "heigth":197, "position":센터}
-sangbuk-players.bin 에 pickle로 dump
"""
def read_sangbuk():
    cows = []
    with (open('./sample/sangbuk.csv', 'r', encoding="UTF-8") as f):
        lines = f.readlines()

        for line in lines:
            strip_line = line.strip()
            split_line = strip_line.split(", ")

            cow = {
                "name": split_line[0],
                "backno": split_line[1],
                "heigth": split_line[2],
                "position": split_line[3]
            }
            cows.append(cow)
        with open("./sample/sangbuk-players.bin", "wb") as f:
            pickle.dump(cows, f, pickle.HIGHEST_PROTOCOL)


def read_sangbuk2():
    sangbuk_list = []
    with open('./sample/sangbuk-players.bin', 'rb') as f:
        while True:  # 몇개인지 모르니까 루프
            try:
                data = pickle.load(f)
            except EOFError:  # 피클이 없다면
                break
            sangbuk_list.append(data)

    print("역직렬화 결과>", sangbuk_list)



if __name__ == "__main__":
    # write_file()
    # write_file2()
    # read_file()
    # read_file_by_line()
    # read_file_readlines()
    # copy_binary_file()
    # serialize()
    # deserialize()
    read_sangbuk()
    read_sangbuk2()