# def profile(name, age, main_lang):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" \
#           .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업을 듣는 학생이라고 가정!

def profile(name, age=17, main_lang="파이썬"): # 함수의 기본값 사용!
    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" \
          .format(name, age, main_lang))
    
profile("정준하")
profile("김태호")

# 키워드 값을 통해 함수 호출 시 순서를 변경해도 출력은 정의된 순서대로 함.
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")