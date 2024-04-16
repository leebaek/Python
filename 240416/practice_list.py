# 리스트[] : 순서를 가진 객체의 집합

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 박명수가 몇 번째 칸에 타고 있는가?
print(subway.index("박명수"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)
print(subway.index("하하"))

# 정형돈을 유재석과 조세호 사이에 태움
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 뺌
subway.pop()
print(subway)

# subway.pop()
# print(subway)

# subway.pop()
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 오름차순 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 내림차순 정렬
num_list.reverse()
print(num_list)

# 리스트 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
mix_list = ["유재석", 20, True]
print(mix_list)

# 리스트 합치기
num_list2 = [12,34,2,3,23]
num_list2.extend(mix_list)
print(num_list2)