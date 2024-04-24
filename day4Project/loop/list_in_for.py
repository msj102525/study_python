# path : loop/list_in_for
# module : loop.list_in_for
# 리스트 내포 (리스트 안의 for) 확인영 스크립트

# 리스트 안에 값 추가를 위한 for 문을 포함하는 구문
# [기록할값 for 변수 in 시퀀스객체]
# 주의 : 기록할값과 변수의 이름이 반드시 같아야 함
# 시퀀스객체(Iterable) : 순차적으로 값을 저장한 객체 (str, list, tuple)
# 시퀀스객체 대신에 range(시작값, 끝값, 간격) 함수 사용 가능함

# 리스트에 값을 기록하는 방법 1 : append() 사용
def list_append():
    sample_list = list()    # sample_list = []
    for n in range(1, 6):
        sample_list.append(n)
    print(sample_list)

# 리스트 내포로 바꾼다면
def list_append_2():
    sample_list = [n for n in range(1, 6)]
    print(sample_list)

# 리스트 내포시에 if 문도 같이 포함할 수 있음
def list_append_3():
    sample_list = list()
    for n in range(1, 11):
        if n % 2 == 0:
            sample_list.append(n)
    print(sample_list)

# 리스트 내포로 바꾼다면
def list_append_4():
    sample_list = [n for n in range(1, 11) if n % 2 ==0]
    print(sample_list)

# for 문 안에 for 문이 사용되는 경우 (다중 for 문)
def list_append_5():
    sample_list = list()
    for n in range(1, 6):
        for m in range(1, 5):
            sample_list.append(n + m)

    print(sample_list)

# 리스트 내포
def list_append_6():
    sample_list = [n + m for n in range(1, 6) for m in range(1, 6)]
    print(sample_list)

# 구구단 2단부터 9단까지 곱하기한 결과값을 리스트에 저장 처리함
# 리스트 내포
def list_append_7():
    result_list = [dan * su for dan in range(2, 10) for su in range(1, 10)]
    print(result_list)




# 함수 실행
if __name__ == '__main__':
    # list_append()
    # list_append_2()
    # list_append_3()
    # list_append_4()
    # list_append_5()
    # list_append_6()
    list_append_7()