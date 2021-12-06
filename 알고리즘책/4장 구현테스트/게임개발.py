n , m = map(int,input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)] # m의 갯수 만큼 0리스트를 만들고 , n의 갯수만큼 리스트 또 생성 

print(d)
#현재 캐릭터의 x , y , 방향 입력받기

x,y,direction = map(int,input().split())

d[x][y] = 1 #현재 좌표 방문처리
        
#전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

#북동남서 방향 정의
dx = [-1 , 0 , 1 , 0]
dy = [ 0 , 1 , 0 , -1]

#왼쪽으로회전 
def turn_left():
    global direction
    direction -= 1 
    if direction == -1: #방향값이 -1이 되면 다시 3부터 돌아가기 위함
        direction = 3

#시뮬레이션 시작 
count = 1
turn_time = 0 #회전횟수
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]


    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0: #내가 안간곳이면서 육지 =0 인곳
        d[nx][ny] = 1 # 가본곳은 1로 변경
        x = nx #이동한 좌표의 값을 x로 다시 저장
        y = ny
        count += 1 #이동할때마다 count 증가
        turn_time = 0 #회전횟수를 다시 초기화 -> 4번 회전했을때의 갈곳없다는 체크표시이기 때문
        continue

    #회전한 이후 정면에 가보지않은 칸이 없거나 바다인경우
    else:
        turn_time += 1 #회전횟수 증가

        #네방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction] 
        ny = y - dx[direction]

        #뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny

        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)