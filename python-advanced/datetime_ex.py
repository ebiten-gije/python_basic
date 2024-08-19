# import datetime
from datetime import datetime, date, time   # 특정 패키지(모듈) 내부의 객체
def get_datetime():
    """
    현재 날짜, 시간 정보의 획득
    """
    # 현재 시간 -> now()
    now = datetime.now()
    print("현재 시간:", now)

    # 생성자를 이용한 날짜 지정
    # 년, 월, 일, 시, 분, 초, 마이크로세컨드 -> 최소 연, 월, 일은 있어야 함
    dt = datetime(1999, 12, 31, 23)
    # 없는 날짜 지정하면 ValueError
    print(dt)

    # datetime 의 속성
    print(now.year, now.month, now.day, now.weekday(), now.hour,
        now.minute, now.second, now.microsecond)

    # 요일 정보: weekday(), 0=월, 6=일
    print("요일:", now.weekday())

    # 날짜 정보를 반환 date() -> date 객체
    # 시간 정보 반환 time() -> time 객체
    print("date:", now.date(), type(now.date())) # 날짜 정보
    print("time:", now.time(), type(now.time())) # 시간 정보

    # date 객체는 datetime 객체의 날짜 관련 속성, 메서드만 사용 가능
    # time 객체 역시 datetime 객체의 시간 관련 속성, 메서드만 사용 가능


def timedelta_ex():
    """
    timedelta 클래스: 두 날짜 사이의 시간 간격
    """
    current= datetime.now() # 현재 시간
    past = datetime(1997, 11, 26) # 과거
    # 대소 비교 가능
    print(current >= past) # current 가 past 보다 큼(뒤)?
    # 두 날짜 사이의 간격
    diff = current - past
    print(diff)

    # 속성: days, seconds, microseconds
    print(diff.days, diff.seconds, diff.microseconds)
    # 메서드 : total_seconds()
    print("총", diff.total_seconds(), "초 흘렀다")

    # datetime과 timedelta의 합산?
    print(current, "에서", diff, "를 합산한 결과:", current + diff)


def format_date():
    """
    .strftime() -> 날짜 시간 정보를 문자열로 formating
    .strptime() -> 문자열 정보를 datetime으로 해독
    """
    current = datetime.now()
    print(current)
    print(current.strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))

    strdate = "2045년 08월 04일"
    dt = datetime.strptime(strdate, "%Y년 %m월 %d일")
    print(dt)
    print(repr(dt))

    dt2 = eval(repr(dt))
    print(dt2, type(dt2))



if __name__ == "__main__":
    # get_datetime()
    # timedelta_ex()
    format_date()