# any()는 하나라도 True인게 있으면 True
# all()은 모두 True여야 True

print(any([False,False,True]))
print(all([False,True,True]))
print()


value = 3
temp = [1,4,3,8,10]
if any(value < num for num in temp):
    print("value값보다 큰값이 존재합니다")

value = 1
temp = [1,3,4,5]
if all(value < num for num in temp):
    print("value값보다 전부 큽니다")
else:
    print("value값보다 하나라도 같거나 작은값이 있습니다")

