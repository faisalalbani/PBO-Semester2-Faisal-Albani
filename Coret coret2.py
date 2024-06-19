class Hero:

    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def serang (self, lawan):
        print (self.name + " menyerang " + lawan.name)
        lawan.diserang(self)

    def diserang (self, lawan):
        print (self.name + " diserang " + lawan.name)
        serangan_terasa = lawan.attack - self.armor
        print ("besar serangan yang diterima: ", (serangan_terasa)) 
        self.health -= serangan_terasa
        print("darah: " + self.name + " tersisa: ", (self.health))



layla = Hero ("layla", 100, 40, 20)
zilong = Hero ("zilong", 100, 10, 10)

layla.serang(zilong)
print("\n")
layla.serang(zilong)
print("\n")
layla.serang(zilong)
print("\n")
