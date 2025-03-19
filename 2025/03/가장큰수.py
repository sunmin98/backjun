def custom_sort_debug(x):
    """ 정렬 기준을 출력하는 함수 """
    result = x * 3  # 정렬 기준이 되는 값
    print(f"'{x}' → '{result}'")  # 변환 과정 출력
    return result

def solution(numbers):
    str_numbers = list(map(str, numbers))  # 숫자를 문자열로 변환
    print(f"\n[초기 리스트]: {str_numbers}\n")

    # 정렬 과정 디버깅
    str_numbers.sort(key=custom_sort_debug, reverse=True)

    print(f"\n[정렬된 리스트]: {str_numbers}\n")  # 최종 정렬된 결과 출력
    return str(int("".join(str_numbers)))  # "000" 같은 경우 "0"으로 변환

# 테스트 실행
print(f"결과: {solution([3, 30, 34, 5, 9])}")  # 예상: "9534330"
