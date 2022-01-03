def solution(phone_book):
    answer = True

    phone_book.sort(key = len) #문자열을 길이로 정렬
    print(phone_book)


    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
                break

    return answer
                

phone_book = ["119","25","1111911","13233","1323312","9999999"]
solution(phone_book)