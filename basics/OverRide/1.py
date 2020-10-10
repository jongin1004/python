class C1:
    def m(self):
        return 'parent'

class C2(C1):
    def m(self):  #부모 객체의 m 이라는 method를 재정의

        return super().m() + ' child' # super()은 현재 객체의 부모객체를 의미한다. 그 뒤에 . 뒤에 나오는 m()는 부모 객채의 method를 가르킴
    pass    #method가 존재하지 않는 class는 오류가 나오기 때문에 pass를 적어줘야한다.
o = C2()
print(o.m())
