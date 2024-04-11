# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower()) # 문자열을 전부 소문자로 출력
print(python.upper()) # 문자열을 전부 대문자로 출력
print(python[0].isupper()) # 변수의 첫문자가 대문자인가? T or F
print(python[0].islower()) # 변수의 첫문자가 소문자인가?
print(len(python)) # 문자열의 길이
print(python.replace("Python", "Java")) # 원하는 문자를 다른 문자로 바꾸기

index = python.index("n") # n이라는 문자가 몇번째에 위치했나?
print(index)
index = python.index("n", index + 1) # n이라는 문자를 위에 정의된 5 + 1 자리부터 찾는다.
print(index)

print(python.find("n"))
print(python.find("Java")) # find 함수에서는 문자열에 없는 단어를 찾으면 -1을 반환하고 프로그램이 종료되지 않는다.
print("hi")

# print(python.index("Java")) # index 함수에서는 문자열에 없는 단어를 찾으면 오류가 뜨면서 프로그램이 종료된다.
print("hi")

print(python.count("n")) # 문자열에서 n이라는 단어가 몇개나 되나?