def solution(x):
    number_list = list(map(int, str(x)))
    sum_number = int(sum(number_list))

    if x % sum_number == 0:
        answer = "true"
    else:
        answer = "false"

    return answer

solution(13)


def solution(x):
    X = list(map(int, str(x)))
    Sum = sum(X)

    if x % Sum == 0:
        return True
    else:
        return False