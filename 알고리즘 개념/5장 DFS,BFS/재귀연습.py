def solve(i):
    print(i,"번째 재귀함수호출")
    if i == 10:
        return #재귀함수를 끝내기
    solve(i+1)

solve(1)