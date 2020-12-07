#파라미터가 3개지만, age와 main_lang는 기초값을 지정했기 때문에
#파라미터 1개(name)만 보내도 정상적으로 작동
#age나 main_lang을 지정하고 싶으면 그대로 추가로 적어주면 됨

def profile(name, age=17, main_lang="python") :
    print("name : {0}\t age : {1}\t main_lang : {2}" \
    .format(name, age, main_lang))

profile("a", "2", "asd")
profile("b")

##################################################
#함수에서 전달받는 매개변수의 값을 키워드로 해서 함수를 호출해도
#순서가 바껴 있어도, 함수 안에있는 순서대로 제대로 호출된다.

def profile(name, age, main_lang) :
    print(name, age, main_lang)

profile(name="a", main_lang="b", age="5")

####################################################
#가변인자
#매개변수가 몇 개가 들어올지를 정할 수 없는 상황일
# def profile(name, age, lang1, lang2, lang3, lang4) :
#     print("name : {0}\t age : {1}\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4)
#
# print("a", 20, "python", "java", "php", "mysql")
# print("b", 25, "python", "java", "","")



def profile(name, age, *language) :
    print("name : {0}\t age : {1}\t".format(name,age), end=" ")
    for lang in language :
        print(lang, end=" ")
    print()

profile("a", 20, "python", "java", "php", "mysql")
profile("b", 25, "python", "java", "","")
