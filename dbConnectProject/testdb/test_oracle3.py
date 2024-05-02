# path : testdb\\test_oracle2.py
# 오라클 연동과 update 쿼리문 실행 테스트

# 1.
import cx_Oracle
import os
import common.dbConnectTemplate as dbtemp

# 2.
dbtemp.oracle_init()
conn = dbtemp.connect()

# 3.
# query = "update member set userpwd = 'tp77', phone = '010-213-252', email = 'tp77@test.org' where userid = 'user77'"

# # 4.
# cursor = conn.cursor()
# try:
#     cursor.execute(query)
#     conn.commit()
# except:
#     conn.rollback()
# finally:
#     cursor.close
#     dbtemp.close(conn)

# update 구문에 사용할 값을 외부 데이터를 이용할 경우 (키보드 입력 데이터 등)
# 주의 : 쿼리문에 적용할 외부 값은 반드시 튜플로 저장해야 함
# 키보드로 값을 입력 받아서 튜플에 저장 처리 :
# userid = input("아이디 : ")
# passwd = input("암호 : ")
# phone = input("전화번호 : ")
# email = input("이메일 : ")

# tu = (passwd, phone, email, userid)
tu = (input("암호 : "), input("전화번호 : "), input("이메일 : "), input("아이디 : "))

# 튜플을 쿼리문에 적용할 때, 값을 1234 순으로 적용해야 함 (순서 주의)
query = "update member set userpwd = :1, phone = :2, email = :4 where userid = :4"

# 4.
cursor = conn.cursor()
try:
    # cursor.execute(query, tu)
    cursor.execute(query, tu)
    conn.commit()
except:
    conn.rollback()
finally:
    cursor.close
    dbtemp.close(conn)