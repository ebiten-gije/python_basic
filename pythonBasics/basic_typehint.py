# 변수 타입 힌트
age: int = 25
name: str = "홍길동"

age = "장길산"

# 함수 매개변수 및 반환값 타입 힌트
def greet (name:str) -> str: # str 변수 입력, str 출력
    return f"너 이름이 {name}이구나"

# 복잡한 타입 힌트는 typing 패키지에 있는 타입 클래스를 import
from typing import List, Tuple, Set, Dict, Optional, Union, Any, Callable

# 컬렉션 타입 힌트 예제
numbers: List[int] = [1, 2, 3, 4, 5]
person: Tuple[str, int] = ("마린", 30)
user: Dict[str, str] = {"name": "마린"}
unique_names: Set[str] = {"마린", "미코", "아쿠아"}

# 옵션 타입 힌트
def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "마린"
    else:
        return None


# 유니온 타입 예제
def process_value(value: Union[int, str]) -> str:
    return str(value)


# 함수 데이터 타입
def execute_op(op: Callable[[int, int], int], a:int, b:int) -> int:
    return op(a, b)



if __name__ == "__main__":
    print(greet("기제"))