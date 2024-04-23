# test_dict 디렉토리 안에 있는 dict_sample.py 파일 안의 함수를 사용하려면
# import 문을 사용해서 임포트 선언해야 함

# 모듈 : 함수를 가지고 있는 파이썬 파일
# import 파일명  => 같은 디렉토리 안의 파일을 불러 들일 때
# import 디렉토리명.파일명    => 다른 디렉토리의 파일을 불러 들일 때

# import test_dict.dict_sample
# 모듈명이 길거나 복잡하면 줄임말을 지정할 수도 있음
# import 모듈명 as 줄임말
# import test_dict.dict_sample as ts
# import mission.dict_mission1 as m1
# # import mission.dict_mission2 as m2
import test_set.set_sample as tts

if __name__ == '__main__':
    # 임포트한 모듈(파일)이 가진 함수를 사용하려면 (함수 실행)
    # 모듈명.함수명()  또는 모듈줄임말.함수명()
    # test_dict.dict_sample.test1()
    # ts.test1()
    # ts.test2()
    # ts.test3()
    # ts.test4()
    # ts.test5()
    # ts.test6()
    # ts.test7()
    # ts.test8()

    # 사전 자료형 복습문제 1
    # m1.dict_func()
    # m1.dictfunc2()
    # m1.dictfunc3()

    # 사전 자료형 복습문제 2
    # m2.dictfunc1()
    # m2.dictfunc2()

    # set 자료형 테스트
    tts.test1()
    tts.test2()
    tts.test3()
    tts.test4()
    tts.test5()
    tts.test6()
    tts.test7()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
