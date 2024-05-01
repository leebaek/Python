# 반복문 : for
'''for waiting_no in range(1,6):
    print("대기번호 : {0}\n다음번호 : {1}".format(waiting_no, waiting_no))'''

starbucks = ["유재석", "박명수", "노홍철", "정준하", "하하", "정형돈", "길"]
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다.".format(customer))

# 한줄 for문
# 출석번호 1 2 3 4, 앞에 100을 붙이기로 함 -> 101 102 103 104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
student = ["lee", "park", "kim", "hwang"]
student = [len(i) for i in student]
print(student)

# 학생 이름을 대문자로 변환
muhan = ["jaeseok", "myeongsu", "junha", "hongchul", "haha", "gil", "hyeongdon"]
muhan = [i.upper() for i in muhan]
print(muhan)