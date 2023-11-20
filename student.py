class Student():
    def __init__(self):
        self.name = "Hiba"
        self.age = 19
        self.major = "Digital development"
        self.institution = "ISGI"
        self.city = "Marrakech"
        self.number = 1

    def info(self):
        print(f" Student {self.number} : ")
        print(f"- Name: {self.name}")
        print(f"- Age: {self.age}")
        print(f"- Major: {self.major}")
        print(f"- Institution: {self.institution}")
        print(f"- City: {self.city}")

student1 = Student()

student1.info()
