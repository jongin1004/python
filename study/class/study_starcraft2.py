class Unit:
    # init는 생성자로써, 객체가 만들어질 때 자동으로 생성
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} :{1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))
# Unit 을 상속받음


class AttackUnit(Unit):

    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진클래스


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2} ]"
              .format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
      print("[공중 유닛 이동]")
      self.fly(self.name, location)

 
# 벌쳐 : 지상유닛 , 기동성 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루져
battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")


# 발키리 : 공중 공격 유닛, 한번에  14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# class로 부터 생성되어지는 것들 (marine, tnak)을 객체라고 한다.
# marine, tnak는 Unit class의 인스턴스라고 한다.
# marine1 = AttackUnit("마린", 40, 5)
# marine2 = AttackUnit("마린", 40, 5)
# tank = AttackUnit("탱크", 150, 35)

# 맴버변수
# 클레스 내에서 사용할 수 있는 변수

# 레이스
wraith1 = AttackUnit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1} ".format(wraith1.name, wraith1.damage))

# 외부에서 객체에 접근해서 변수를 추가로 할당할 수 있음
# 변수를 확장시킬 수 는 있지만, 이 확장된 변수는 해당된 객체에서만 사용가능
# 예를 들어서 wraith1.clocking을 사용하게되면 오류가 나오게 된다.
# 왜? clocking이라는 변수는 wraith2에서만 외부에서 따로 확장한 변수이기 때문
wraith2 = AttackUnit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 파이어뱃
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# 메딕
