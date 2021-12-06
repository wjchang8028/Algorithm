weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather =="눈":
    print("우산 챙기세요")
elif weather =="미세먼지":
    print("마스크 챙기세요")
else:
    print("준비물 필요없음")


temp = int(input("기온은 어때요? "))
if 30<= temp:
    print("너무 덥습니다. 나가지마세요")
elif 10<=temp and temp < 30:
        print("괜찮은 날씨입니다.")
elif 0 <= temp and temp < 10:
    print("외투를 챙기십쇼")
else:
    print("너무 춥습니다. 나가지마세요")