from bisect import bisect_left,bisect_right
from turtle import right

def solution(words,questions):
    words_list = []
    ques_list=[]
    words_index = []
    temp = [[] for _ in range(len(questions))]

    for i in words:
        words_list.append(list(i))
    for j in questions:
        ques_list.append(list(j))
        
    for i in ques_list:
        count = bisect_right(i,'?') #물음표의 갯수
        words_index.append(count)
    print(words_index)

    for i in range(len(ques_list)):
        for j in range(len(ques_list[i])):
            if ques_list[i][j] == '?':
                first_index = j
                break
        for j in range(len(ques_list[i])):
            if ques_list[i][j] =='?':
                last_index = j
        
        print(first_index,last_index)

    for i in range(len(questions)):
        for j in range(len(words)):
            if len(questions[i]) == len(words[j]):
                temp[i].append(words[j])
    
    print(temp) # 길이가 같은 값들만 추려냄

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j][0:first_index] == questions[i][0:first_index]:
                print(temp[i][j])
    
    return

def count_by_range(a,left_value,right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

#모든 단어를 길이마다 나누어 저장하기 위한 리스트   
array = [[] for _ in range(10001)]
#모든 단어를 길이마다 나누어 뒤집어서 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]

def correct_solution(words,queries):
    answer = []
    for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word) # 단어 삽입
        reversed_array[len(word)].append(word[::-1]) #단어를 뒤집어서 삽입

    for i in range(10001): #이진탐색을 수행하기 위해 각 단어 리스트 정렬
        array[i].sort()
        reversed_array[i].sort()
    
    for q in queries:
        if q[0] != '?': #접미사에 와일드카드가 붙은경우 ex) kak??
            res = count_by_range(array[len(q)], q.replace('?','a'), q.replace('?','z'))
        else: # 접두사에 와일드카드가 붙은경우 ex> ???ao
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
    
        answer.append(res)
    print(answer)
    return answer


words = ["frodo" , "front" , "frost" , "frozen" , "frame" , "kakao"]
questions = ["fro??" , "????o" , "fr???" , "fro???" , "pro?"]


correct_solution(words,questions)