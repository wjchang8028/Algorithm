import sys

testcase = int(input()) #테스트케이스

for i in range(testcase):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)