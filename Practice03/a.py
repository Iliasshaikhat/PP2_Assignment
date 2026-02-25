class Cat:
    def set_data(self, name, age, mood):
        self.name = name
        self.age = age
        self.mood = mood
    def __init__(self, name, age, mood):
        self.set_data(name, age, mood)
    def get_data(self):
        print("Name: ",self.name)
        print("Age: ", self.age)
        print("Mood: ", self.mood)
        

name, age, mood = input().split()

cat = Cat(name, age, mood) 
cat.get_data()