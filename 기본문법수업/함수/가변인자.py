# def profile(name ,age,lang1, lang2, lang3,lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t" .format(name,age),end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)


def profile(name ,age, *language): #서로다른 인수의 갯수를 넣으려면 가변인자 활용
    print("이름 : {0}\t나이 : {1}\t" .format(name,age),end=" ")
    for lang in language:
        print(lang, end= " ")
    print()

profile("유재석", 20 , "python","java","c","c++","c#","javaScript")
profile("김태호", 25 , "kotlin","swift","","","")