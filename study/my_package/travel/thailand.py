class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (아시아 투어) 50만원")


# if name 정보를 활용해서 외부에서 이 모듈을 쓰는 건지 내부에서 쓰는 건지를
# 확인할 수 있다
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행되요")
    trip_to = ThailandPackage()
    trip_to.detail()

else:
    print("Thailand 외부에서 모듈 호출")
