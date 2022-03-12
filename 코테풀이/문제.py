def solution(log,stime):

    for i in log:
        arr = list(i.split(" "))
        print(arr)

        start = int(stime[3:])
        penalty = int(arr[0][3:])
        print(penalty)

        if arr[1] == '정답':
            pass

    return

log = [
'12:10 정답 1 에밀리',
'12:20 정답 1 에밀리',
'12:30 오답 1 에밀리',
'12:50 정답 1 티거',
'13:20 정답 2 에밀리',
'13:40 오답 2 티거',
'13:50 오답 2 티거',
'14:10 정답 2 티거',
'15:00 정답 1 렉스']
stime = '12:00'
solution(log,stime)

# 시작시간부터 패널티 적용
# 정답이 최초인정된 후 부터는 패널티 미적용
# 정답 맞추기 전 오답 수 * 20 의 패널티 적용

# 결과값 = [에밀리,2,100],[티거,2,220],[렉스,1,180]