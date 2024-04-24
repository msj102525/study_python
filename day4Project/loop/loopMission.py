# path : loop\\loopMission.py
# module : loop.loopMission

# 리스트 안의 튜플아이템의 값들에 대해
# 둘 중의 큰값과 작은값을 분류해서 출력 처리

# 방법 1 : 조건식 직접 작성
def practice1():
    nlist = [(12, 45), (90, 32), (56, 19)]
    # for 문 안에서 if 문 사용
    for first, second in nlist:
        if first > second:
            max = first
            min = second
        else:
            max = second
            min = first
        print(f'큰값 : {max}, 작은값 : {min}')


# 방법 2 : 내장함수 이용
def practice2():
    nlist = [(12, 45), (90, 32), (56, 19)]
    # for 문 안에서 if 문 사용
    for first, second in nlist:
        vmax = max(first, second)
        vmin = min(first, second)
        print(f'큰값 : {vmax}, 작은값 : {vmin}')


# 활용 실습 : 조건식 직접 작성
# 리스트 안의 군집아이템들이 가진 값들 중 각각 가장 큰 값을 골라 내서
# 별도의 리스트에 저장 처리하고 출력
def practice3():
    lists = [[43, 1, 20], (22, 41, 10, 73), {12, 32, 45, 3, 9}]
    max_list = []

    for item in lists:
        max_value = 0
        for value in item:
            if max_value < value:
                max_value = value
            max_list.append(max_value)
    print(max_list)


# 내장함수 max(Iterable) 사용
def practice4():
    lists = [[43, 1, 20], (22, 41, 10, 73), {12, 32, 45, 3, 9}]
    max_list = []

    for item in lists:
        max_list.append(max(item))
    print(max_list)


''' while 문 실습문제
아래의 작성된 for문을 while문으로 변경하시오.
sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]

for student in sungjuk_list:
    if(student[2] >= 60):
        print('{}번 {} 학생은 합격입니다.'.format(student[0], student[1]))
    else:
        print('{}번 {} 학생은 불합격입니다.'.format(student[0], student[1]))
'''


# 1. while 문으로 변경

def practice_while():
    sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]

    num = 0
    while num < len(sungjuk_list):
        if (sungjuk_list[num][2] >= 60):
            print('{}번 {} 학생은 합격입니다.'.format(sungjuk_list[num][0], sungjuk_list[num][1]))
        else:
            print('{}번 {} 학생은 불합격입니다.'.format(sungjuk_list[num][0], sungjuk_list[num][1]))

        num += 1


if __name__ == '__main__':
    # practice1()
    # practice2()
    # practice3()
    # practice4()
    practice_while()
