# file 쓰는 것과 읽는 것을 단 2줄로 끝낼수 있음 close안해도 되기 때문에

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 고웁하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

with open("score.txt", "r", encoding="utf8") as score_file:
    print(score_file.read())
