# print("python","java","javascript",sep="," , end="?") 
#print("무엇이 더 재밌을까요?")
#end는 문장의 끝부분을 end로 바꿔달라는 의미 -> 뒷문장이 한줄로 출력됨

import sys
# print("python","java","javascript",file=sys.stdout) 
# print("python","java","javascript",file=sys.stderr) #따로 에러처리


scores = {"수학":0,"영어":50,"코딩":100}
for subject, score in scores.items(): #items()키와 value 를 튜플로 보내줌
    #print(subject,score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
    #8칸 공백을 밀고 왼쪽정렬
    #4칸 공백을 밀고 오른쪽정렬

#은행 대기 순번표
for num in range(1,21):
    print("대기번호 : "+str(num).zfill(3)) #3크기만큼의 크기 확보후 빈공간채우기 

answer = input("아무값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")