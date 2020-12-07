#pickle 프로그램 상에서 사용하는 데이터를 파일형식으로
#저장하는 것,  pickle을 통해서 데이터를 가져와서
#코딩에서 사용할 수  있다.
import pickle
#w 쓰기 목적 b는 바이너리를 의미 pickle을 쓰기위해서 는
#항상 바이너리를 설정해야 한다.
profile_file = open("profile.pickle", "wb")
profile = {"name" : "a", "age" : 10, "hobby" : ["a","b"] }
print(profile)
pickle.dump(profile, profile_file))#profile에 있는 정보를 file에 저장
profile_file.close()
