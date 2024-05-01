# 분기 : if
weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
elif weather == "구름":
    print("겉옷을 챙기세요")
else:
    print("준비물 필요없어요")

temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 더우니 나가지 마시오")
elif 10 <= temp and temp < 30:
    print("따뜻한 날씨예요")
elif 0 <= temp <10:
    print("쌀쌀한 날씨예요")
else:
    print("넘 추워용")