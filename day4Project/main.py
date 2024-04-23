# 파이썬 제어문 실행영 스크립트

# 다른 파일에 있는 함수를 사용하려면 import 선언해야 함
# import 디렉토리명.파일명
# import test_bool.operator_sample
# 파일이 제공하는 함수 사용시 디렉토리명.파일명.함수명(...)

# 모듈명이 길거나 복잡할 경우 줄임말 지정하고 사용 가능함
# import 모듈명 as 줄임말
import test_bool.operator_sample as to
import conditional.ifSample as cif
import conditional.ifMission1 as cm1
import conditional.ifMission2 as cm2
import conditional.ifMission3 as cm3

# 프로그램을 시작하는 구문임
if __name__ == '__main__':
    # 임포트한 파일에서 제공하는 함수 사용
    # 모듈명.함수명() | 줄임말.함수명()
    # to.func_bool()
    # to.func_bool2()
    # to.func_compare()
    # to.func_logical()

    # 조건문 사용 테스트
    # cif.test_if()
    # cif.test_if2()
    # cif.test_even()
    # cif.test_even2()
    # cif.test_range()
    # cif.test_in()
    # cif.checkPayment()
    # cif.checkPayment2()
    # cif.multi_if()
    # cif.shortCondition()
    # cif.shortCondition2()

    # 조건문 실습 문제
    # cm1.practice1()
    # cm2.practice2()
    cm3.practice3()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
