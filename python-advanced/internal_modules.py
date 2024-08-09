import sys
def sys_module():
    # argv 속성: 명령형에서 넘어온 인수
    # print(sys.argv) # 0번 인덱스는 스크립트 명

    args = sys.argv[1:] # 스크립트를 제외한 인수
    print("명령형 인수:", args)

    # 시스템 관련 정보
    print("Platform:", sys.platform)
    print("version:", sys.version)

    # 파이썬은 모듈을 검색할 때, sys.path에 등록된 디렉토리를 대상으로 검색
    print("모듈 검색 경로:", sys.path)
    # 찾는 모듈이 sys.path에 없을 때,
    # sys.path.append ("추가할 모듈 경로")


def regexp_ex():
    """
    정규 표현식 예제
    """
    import re
    namecard="""\
Email: vv@gmail.com
Phone: 010-3535-3535

Email: cc@gmail.com
Phone: 010-1111-3535

Email: ww@gmail.com
Phone: 010-3535-1111
    """
    emaillist = re.findall(r"\w+[\w\.]*@\w+[\w\.]\.[a-z]+", namecard)

    phonelist = re.findall(r"[0-9]{3}-[0-9]{4}-[0-9]{4}", namecard)
    print(emaillist)
    print(phonelist)


def random_ex():
    import random

    # random.seed(42) # 난수 계산 시드값 고정

    print(random.random()) # 0 ~ 1 사이의 난수
    print(random.randint(1, 6)) # 1 ~ 6 사이의 정수 난수
    print(random.randrange(101)) # 0~ 100 사이의 난수
    print(random.randrange(1, 101, 3)) # 1 ~ 100 사이의 3간격 중에서 난수

    # 숫자형에 무작위성을 추가하는 부가 기능들
    seqvar = ['짬뽕', '짜장면', '탕수육', '깐풍기']
    print('seqvar:', seqvar)
    random.shuffle(seqvar)
    print('seqvar:', seqvar)
    print(random.choice(seqvar))

    # 샘플링?
    for i in range(5):
        print(random.sample(range(1, 48), 6))



if __name__ =="__main__":
    # sys_module()
    # regexp_ex()
    random_ex()