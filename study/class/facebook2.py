import datetime
import time

class Facebook :
    def __init__(self, name) :
        self.name = name
        self.posts = []
        self.followees = []

    def get_name(self) :
        return self.name

    def get_posts(self) :
        return self.posts

    def add_posts(self, post) :
        self.posts.append(post)

    def add_followees(self, name) :
        self.followees.append(name)

    def get_followees(self) :
        return self.followees

class Post :
    def __init__(self, text) :
        self.text = text
        now = datetime.datetime.now()
        self.date = now.strftime('%H:%M:%S')
        self.like = 0

    def get_text(self) :
        return self.text

    def get_date(self) :
        return self.date

    def get_like(self) :
        return self.like

    def increase_like(self) :
        self.like += 1

###############################

u_1 = Facebook("Kim")

p_1 = Post("a")
for i in range(5):
    p_1.increase_like()
u_1.add_posts(p_1)

p_2 = Post("b")
for i in range(10):
    p_2.increase_like()
u_1.add_posts(p_2)

###############################

u_2 = Facebook("Lee")

p_3 = Post("php good")
for i in range(15):
    p_3.increase_like()
u_2.add_posts(p_3)

time.sleep(1)

p_4 = Post("python good")
for i in range(20):
    p_4.increase_like()
u_2.add_posts(p_4)

time.sleep(1)

p_5 = Post("php fun")
for i in range(25):
    p_5.increase_like()
u_2.add_posts(p_5)

time.sleep(1)
###################################

u_3 = Facebook("Choi")

p_6 = Post("python fun")
for i in range(30):
    p_6.increase_like()
u_3.add_posts(p_6)

time.sleep(1)

p_7 = Post("python hard")
for i in range(35):
    p_7.increase_like()
u_3.add_posts(p_7)

###################################

u_1.add_followees(u_2)
u_1.add_followees(u_3)

###################################

#u_1 의 이름
print(u_1.get_name())
print("@@@@@@@@@@@@@@@@@@")
#u_1 의 followees 수
print(len(u_1.get_followees()))
print("@@@@@@@@@@@@@@@@@@")
#u_1 의 followees들 이름
for i in u_1.get_followees() :
    print(i.get_name())
print("@@@@@@@@@@@@@@@@@@")
#u_1의 followee 중 name이 "Choi"인 사람의 수
count = 0
for i in u_1.get_followees() :
    if i.get_name() == "Choi" :
        count += 1

print(count)
print("@@@@@@@@@@@@@@@@@@")
#u_1의 followee중, name이 "Choi"인 사람의 post들에 달린削減
#like의 총 수를 print
for i in u_1.get_followees() :
    if i.get_name() == "Choi" :
        total_like = 0
        posts = i.get_posts()
        for post in posts :
            total_like += post.get_like()

print(total_like)

print("@@@@@@@@@@@@@@@@@@")
#u_1의 followee들이 작성한 post중,
#python을 다루는 post들의 text print
for followee in u_1.get_followees() :
    posts = followee.get_posts()
    for post in posts :
        if "python" in post.get_text() :
            print(post.get_text())


print("@@@@@@@@@@@@@@@@@@")
#u_1의 followee들이 작성한 post중, python 을 다루는 post들의
#text와 post를 작성한 user의 name을 print하세요

for followee in u_1.get_followees() :
    posts = followee.get_posts()
    for post in posts :
        if "python" in post.get_text() :
            print("user : " +followee.get_name(),"text : "+ post.get_text())


print("@@@@@@@@@@@@@@@@@@")
follow_posts = []
for followee in u_1.get_followees() :
    posts = followee.get_posts()
    for post in posts :
        follow_posts.append(post)

post_time = int(follow_posts[0].get_date()[6:])
post_time2 = int(follow_posts[0+1].get_date()[6:])

count = len(follow_posts)
for i in range(count-1) :
    for j in range(count-1-i) :
        post_time = int(follow_posts[j].get_date()[6:])
        post_time2 = int(follow_posts[j+1].get_date()[6:])
        if post_time < post_time2 :
            follow_posts[j], follow_posts[j+1] = follow_posts[j+1], follow_posts[j]

for post in follow_posts :
    print(post.get_text())

print("@@@@@@@@@@@@@@@@@@")

for i in range(0,3) :
    print(follow_posts[i].get_text())

print("@@@@@@@@@@@@@@@@@@")
