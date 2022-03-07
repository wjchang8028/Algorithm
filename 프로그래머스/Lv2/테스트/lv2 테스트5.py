def solution(phone_book):
    answer = True

    phone_book.sort()
    print(phone_book)

    for i in range(len(phone_book)-1):
        
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                print(phone_book[i][:len(phone_book[0])])
                answer = False
                break
            else:
                answer = True
    print(answer)
        

    return answer


solution(["123","456","789"])
