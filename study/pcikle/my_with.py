import pickle

with open("profile.pickle", "rb") as profile_file:  # pickle파일을 불러와서 profile_file 이라는 변수에 저장
    print(pickle.load(profile_file))
