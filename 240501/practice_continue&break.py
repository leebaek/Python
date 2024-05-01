# continue & break

absent = [2, 5] # 결석
no_book = [7] # 책을 안가져온 학생
for student in range(1, 11): # 1~10
    if student in absent:
        continue # if문에 해당하면 실행하지 않고 다음으로 계속 이어감
    elif student in no_book:
        print("오늘 수업 여기까지 {0}너는 교무실로 와".format(student))
        break # if문에 해당하면 실행하지 않고 구문에서 빠져나옴
    print("{0}, 책을 읽어봐".format(student))
