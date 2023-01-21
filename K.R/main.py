import random
class Human:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True
        self.money=10
        self.strong=10
        self.dish=10
        self.drink=10
        self.sleep=0

    def chill(self):
        print("Піду пограю")
        self.progress-=0.5
        self.gladness+=5
        self.dish-=4
        self.strong-=2
        self.drink-=4
        self.sleep+=5


    def study(self):
        print("Час навчатись")
        self.progress+=1
        self.gladness-=10
        self.strong-=2
        self.sleep += 5

    def side_job(self):
        print("Час підробітки")
        self.progress+=0.5
        self.gladness-=5
        self.strong+=2
        self.money+=10
        self.dish-=4
        self.drink -= 4
        self.sleep += 5

    def training(self):
        print("Час тренування")
        self.progress += 2
        self.gladness -= 5
        self.strong += 2
        self.money -= 1
        self.dish -= 5
        self.drink -= 5
        self.sleep += 5

    def eat(self):
        print("Час їсти")
        self.progress += 0.5
        self.money -= 3
        self.dish += 15

    def water(self):
        print("Час пити")
        self.progress += 1
        self.money -= 5
        self.drink += 10

    def sleeping(self):
        print("Я йду спати")
        self.gladness += 15
        self.dish -= 1
        self.drink -= 2
        self.sleep -= 20

    def dog(self):
        print("Гав гав")
        self.gladness += 20

    def is_alive(self):
        if self.progress<-0.5:
            print("Відрахували...")
            self.alive=False
        if self.gladness>=20:
            print("Життерадісний")
            self.alive=False
        elif self.gladness<=1:
            print("Дипресія")
            self.alive=False
        elif self.progress>=5:
            print("Закінчив універсетет")
            self.alive=False
        elif self.dish>=32:
            print("Ожиріння")
            self.alive = False
        if self.money<=10:
            print("Став бідним")
            self.alive = False
        elif self.money>=20:
            print("Став багатий")
            self.alive = False
        if self.strong>=20:
            print("Став сильний")
            self.alive = False
        elif self.strong>=25:
            print("Став сильний")
            self.alive = False
        if self.dish>=25:
            print("Став жирний")
            self.alive = False
        elif self.dish<=10:
            print("Став худий")
            self.alive = False
        elif self.drink<20:
            print("Напився")
            self.alive = False
        elif self.sleep<25:
            print("не виспався")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,6)}")

    def live(self, day):
        day="Day" + str(day) + "of" + self.name + "litle"
        print(f"{day:=^50}")
        cube=random.randint(1,7)
        if cube==1:
            self.study()
        elif cube==2:
            self.sleeping()
        elif cube==3:
            self.chill()
        elif cube==4:
            self.eat()
        elif cube==5:
            self.side_job()
        elif cube==6:
            self.water()
        elif cube==7:
            self.training()
        elif cube==8:
            self.dog()

        self.end_of_day()
        self.is_alive()

nick=Human(name='Gyro')
for day in range(365):
    if nick.live==False:
        break
    nick.live(day)








