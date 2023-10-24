class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def detail (self):
            print(self.name, "is studying")

p = person("triza",34,"female")
p.detail()
