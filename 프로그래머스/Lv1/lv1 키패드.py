def solution(numbers, hand):
    answer = ''

    pad = [[1,2,3],[4,5,6],[7,8,9],[10,0,11]]

    right_start_x , right_start_y = 3 , 0 #오른손 시작좌표
    left_start_x , left_start_y = 3 , 2 #왼손 시작좌표
    

    for i in numbers:
        if i in [1,4,7]: #1,4,7은 왼손으로
            answer += 'L'

            for j in range(4):
                for k in range(3):
                    if pad[j][k] == i:
                        left_x = j
                        left_y = k

            left_start_x,left_start_y = left_x, left_y
            print(i, left_start_x,left_start_y,'L')

        elif i in [3,6,9]: #3,6,9는 오른손으로
            answer += 'R'
            for j in range(len(pad)):
                for k in range(len(pad[j])):
                    if pad[j][k] == i:
                        right_x = j
                        right_y = k

            right_start_x,right_start_y = right_x, right_y
            print(i, right_start_x,right_start_y,'R')
        else: #그 외에 2 5 8 0 
            for j in range(len(pad)):
                for k in range(len(pad[j])):
                    if pad[j][k] == i:
                        mid_x = j
                        mid_y = k

                        if abs(right_start_x - mid_x) + abs(right_start_y - mid_y) > abs(left_start_x - mid_x) + abs(left_start_y - mid_y): 
                            #왼손 위치가 오른손위치보다 더 가까우면
                            answer +='L'
                            left_start_x = mid_x
                            left_start_y = mid_y
                            print(i, left_start_x,left_start_y,'L')
                        elif abs(right_start_x - mid_x) + abs(right_start_y - mid_y) < abs(left_start_x - mid_x) + abs(left_start_y - mid_y):
                            answer += 'R'
                            right_start_x = mid_x
                            right_start_y = mid_y
                            print(i, right_start_x,right_start_y,'R')
                        else: #둘이 길이가 같다면
                            if hand == 'right':
                                answer += 'R'
                                right_start_x = mid_x
                                right_start_y = mid_y
                                print(i, right_start_x,right_start_y,'R')
                            else:
                                answer += 'L'
                                left_start_x = mid_x
                                left_start_y = mid_y
                                print(i, left_start_x,left_start_y,'L')

    print(answer)
    
    return answer

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right")
print()
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],	"right")
print()
solution([1,3,2],"right")