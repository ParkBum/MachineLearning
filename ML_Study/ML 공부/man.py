# 클래스 안에 들면 메소드랄고 함.. 
# 클래스의 이름은 대문자로 시작한다. 
# def 메소드.. 가 있음

class Man:
    def __init__(self, name):
        self.name = name
        print("Initalized!")
    
    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good bye " + self.name + " !")

m = Man("beom su")
m.hello()
m.goodbye()
