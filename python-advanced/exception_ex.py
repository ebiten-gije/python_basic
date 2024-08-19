def handling_exception():
    """
    예외 처리 절차
    """
    lst = []

    # 1번째 시도!
    try:
        lst[0] = 1 # 예외 발생 코드
    except:
        print("예외 발생했음") # 예외가 발생했을 때 처리되는 블록

    # 2번째!
    try:
        lst[0] = 1 # 예외 발생 코드
        4 / 0
    except Exception: # 발생 예외를 지칭할 수 있음!
        print("Exception 예외 발생했음") # 예외가 발생했을 때 처리되는 블록

    # 일단 오류는 회피,, 어떤 예외가 발생했는지 알 수 없음..

    # 3번째
    try:
        # lst[0] = 1 # 예외 발생 코드 -> IndexError
        4 / 0       # ZeroDivisionError
    except Exception as e: # 발생 예외를 지칭할 수 있음! -> 심볼을 붙여 예외 종류 확인
        print("Exception: ", e)
        print("예외 타입:", type(e))

    # 4번째..
    # Exception 예외는 모든 예외를 다 처리하기 때문에
    # 구체적인 예외를 분리할 필요가 있음
    try:
        # lst[0] = 1 # 예외 발생 코드 -> IndexError
        # 4 / 0  # ZeroDivisionError
        val = int('string')
    except ValueError as e:
        print('정수로 변환될 것 같냐')
    except IndexError as e:
        print(e)
    except ZeroDivisionError as e:
        print('0으로 숫자를 나눌 수 없다는데?')
    except Exception as e:  # 발생 예외를 지칭할 수 있음! -> 심볼을 붙여 예외 종류 확인
        print("Exception: ", e)
        print("예외 타입:", type(e))

    # 5번째 시도...
    # Exception 예외는 모든 예외를 다 처리하기 때문에
    # 구체적인 예외를 분리할 필요가 있음
    print('----------5번째---------')
    try:
        # lst[0] = 1 # 예외 발생 코드 -> IndexError
        # 4 / 0  # ZeroDivisionError
        val = int('2024')
    except ValueError as e:
        print('정수로 변환될 것 같냐')
    except IndexError as e:
        print(e)
    except ZeroDivisionError as e:
        print('0으로 숫자를 나눌 수 없다는데?')
    except Exception as e:  # 발생 예외를 지칭할 수 있음! -> 심볼을 붙여 예외 종류 확인
        print("Exception: ", e)
        print("예외 타입:", type(e))
    else:   # 예외가 없을 때 실행되는 블럭
        print(val)
    finally:    # 예외 유무 상관 없이 실행
        print("예외처리.. 해치웠나")


def raise_exception():
    def beware_dog(animal):
        if animal == 'dog':
            raise RuntimeError('강아지는 출입을 제한합니다')
        else:
            print(animal, '이군여, 어사오세요')

    try:
        beware_dog('cat')
        beware_dog('cow')
        beware_dog('dog')
    except Exception as e:
        print(e, type(e))


if __name__ == "__main__":
    # handling_exception()
    raise_exception()