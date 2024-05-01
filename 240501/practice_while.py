# 반복문 : while
'''customer = "박명수"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")'''

# 무한루프, ctrl + c로 강제종료
'''customer = "노홍철"
index = 1
while True:
    print("{0}님, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
    index += 1'''

# 입력값 받기
customer = "정준하"
person = "Unknown"

while person != customer:
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")