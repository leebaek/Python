# 집합 : 중복 불가, 순서 없음
my_set = {9,2,3,5,2}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합(java와 python을 모두 할 수 있는 사람)
print(java&python)
print(java.intersection(python))

# 합집합(java나 python을 둘 중 하나라도 할 수 있는 사람)
print(java | python)
print(java.union(python))

# 차집합(java를 할 수 있는 사람 중 python을 할 줄 모르는 사람)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹은 사람
java.remove("김태호")
print(java)

# https://youtu.be/kWiCuklohdY?feature=shared&t=6524 부터