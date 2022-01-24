# LIS구현법

# LIS(가장 긴 증가하는 부분 수열)
# 원소가 n개인 배열의 일부 원소를 골라내서 만든 부분 수열 중, 각 원소가 이전 원소보다 크다는 조건을 만족하고, 그 길이가 최대인 부분 수열을 최장 증가 부분 수열이라고 함

# 점화식 : 모든 0 <= j < i 에 대하여, D[i] = max(D[i],D[j+1]) if array[j] < array[i]

array = [1,3,4,6,3,2,8]
dp = [1] * len(array)

for i in range(1,len(array)):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j]+ 1)

print(dp)
#  1  3  4  6  3  2  8
# [1, 2, 3, 4, 2, 2, 5] (길이)
# 까지의 수가 이루는 최대 길이
