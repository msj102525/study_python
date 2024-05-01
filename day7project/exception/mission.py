# path : exception\\mission.py
# 예외처리 실습문제

# 2단에서 9단까지의 구구단을 선택해서 한개의 단을 출력처리함
# 키보드로 출력할 단을 입력받아서 진행함
# 입력된 단수는 정수여야 함 (예외처리)
# 입력된 단수는  2~ 9 사이의 값이여야 구구단 출력됨
# 입력된 단수가 2보다 작으면 단수는 2로 처리함
# 입력된 단수가 9보다 크면 단수는 9로 처리함
# try: except: else: finally: 형식으로 작성함

def gugudan():
    try:
        num = int(input("숫자 단 입력 : "))
        if num <= 2:
            num = 2
        elif num >= 9:
            num = 9
    except ValueError as msg:
        print('숫자 입력 : ', msg)
    except Exception as msg:
        print('다른 에러 : ', msg)
    else:
        for su in range(1, 10):
            print(f'{num} * {su} = {num * su}')
    finally:
        print("구구단 종료")



if __name__ == '__main__':
    gugudan()