#open 파일을 열고 "w" 쓰기 위한 목적
score_file = open("score.txt1", "w", encoding="utf8")
print("a : 0", file = score_file)
print("b : 50", file = score_file)
score_file.close()

#a는 내용이 존재하는 파일에 계속 이어서 쓰고싶을 경우에 사용
#w는 계쏙 덮어쓰기가 된다.
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("c : 80")
score_file.write("\nd : 100")
scroe_file.close()

#r은 파일을 읽을 때 사용
#read 파일에 있는 모든 내용을 다 읽어오는 것
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()


#한줄 한줄 불러오고 싶은 경우
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") #줄 별로 읽기, 한 줄 읽고 커서는 다음주로 이동
print(score_file.readline(), end="")
score_file.close()

#몇 줄인지 모를 때 글 가져오는 경우
score_file = open("score.txt", "r", encoding="utf8")
while True :
    line = score_file.readline()
    if not line :
        break
    print(line)
score_file.close()

#list 형식으로 글을 저장하는 경우
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #list형태로 저장
for line in lines :
    print(line, end="")

score_file.close()
