def solution(n, stations, w):
    answer = 0
    start, end = 1, n

    st = 0
    i = 1
    while i < n + 1:
        print(i)
        if stations[st] - w <= i <= stations[st] + w:  # 범위 안에 있음
            print(stations[st],'범위 안')
            i = (stations[st] + w + 1)
            if st < len(stations)-1:
                st += 1
        else:  # 범위 안에 없음
            answer += 1
            print(i + w, '에 설치')
            i += (2 * w + 1)

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer


# print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))