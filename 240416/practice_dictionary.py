# 사전
cabinet = {3:"유재석", 100:"김종국"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # 5라는 키가 없기 때문에 오류를 발생시키고 다음에 나오는 hi는 출력되지 않는다.
# print("hi")

print(cabinet.get(5)) # .get()으로 찾으면 오류대신 none이 출력되고 다음에 나오는 hi를 출력한다.
print(cabinet.get(5, "사용가능")) # none대신 사용가능이라는 문구를 출력한다.
print("hi")

print(3 in cabinet) # 키가 사전에 존재하는지? True
print(5 in cabinet)

dump = {"A-3":"유재석", "B-100":"김종국"}
print(dump["A-3"])
print(dump["B-100"])

# 손님 추가
print(dump)
dump["A-3"] = "노홍철"
dump["C-20"] = "조세호"
print(dump)

# 손님 삭제
del dump["A-3"]
print(dump)

# 키들만 출력
print(dump.keys())

# value들만 출력
print(dump.values())

# key, value 쌍으로 출력
print(dump.items())

# 목욕탕 폐점
dump.clear()
print(dump)