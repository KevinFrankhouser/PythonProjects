class Fish():
    name = 'Fish'
    sex = 'Male'
    legs = 0
    arms = 0
    fins = 0
    special_characteristic = None

    def swim(self):
        print("The Fish swims by using it's fins")
    
    def information(self):
        msg = "\nName: {}\nSex: {}\nLegs: {}\nArms: {}\nFins: {}\nSpecial Characteristics: {}".format(self.name, self.sex, self.legs, self.arms, self.fins, self.special_characteristic)
        return msg
  

class Eel(Fish):
    name = 'Eel'
    sex = 'Female'
    special_characteristic = 'No fins to use for swimming'

    def swim(self):
        print("The Eel swims by generating body waves which travel the length of their bodies.")
    

class Jellyfish(Fish):
    name = 'Jellyfish'
    sex = 'None'
    special_characteristic = "Can sting it's victims."
    


    def swim(self):
        print("They squeeze their bodies in order to push jets of water from the bottom of their bodies to propel them forward.")




if __name__ == "__main__":
    fish = Fish()
    print(fish.information())
    print(fish.swim())

    eel = Eel()
    print(eel.information())
    print(eel.swim())

    jellyfish = Jellyfish()
    print(jellyfish.information())
    print(jellyfish.swim())
