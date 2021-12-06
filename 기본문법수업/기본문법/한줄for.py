#출석번호가 1 2 3 4, 앞에 100을 붙이기로함
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students] 
print(students)

#학생이름을 길이로 변환
students = ["iron man","Thor","iam groot"]
students = [len(i) for i in students] #i라는 변수의 길이를 for로 돌리면서 students리스트에 넣겠다는 소리
print(students)


#학생 이름을 대문자로 변환
students = ["iron man","Thor","iam groot"]
students = [i.upper() for i in students]
print(students)