class Sim_Cache:
    def __new__(cls):
        if not hasattr(cls, 'cache'):
            cls.cache = super().__new__(cls)
        return cls.cache

    def __init__(self):
        self.nama_web = "PBOTRI"
        self.create_cache()

    def create_cache(self):
        self.cache_source = self.nama_web + ".txt"
        self.cache_file_name = "cache_" + self.nama_web + ".txt"

        sf = open(self.cache_source, "r")  # buka source file
        cf = open(self.cache_file_name, "w")  # buat file cache baru

        cf.write(f"Ini adalah file cache dari web {self.nama_web}\n")

        line1 = False
        for line in sf:
            if "Start_cache" in line:  # menentukan baris awal cache
                line1 = True

            if line1 == True:
                cf.write(line)  # menyalin cache dari source

        sf.close()
        cf.close()

    def get_cache(self):
        if not self.cache:
            self.cache = Sim_Cache()
            print(f"Nama file cache adalah {self.cache_file_name}")

        cf = open(self.cache_file_name, "r")
        print(cf.read())
        cf.close()

# Instansiasi pertama:====
cache1 = Sim_Cache()
cache1.get_cache()

# =====Instansiasi kedua:===
cache2 = Sim_Cache()
add_cache = open("cache_PBOTRI.txt", "a")
add_cache.write("\n***Baris tambahan di file cache***")
add_cache.close()
cache2.get_cache()

#no2

from abc import ABC, abstractmethod
class Section(ABC):
    @abstractmethod
    def describe(self):
        pass
class PersonalSection(Section):
    def describe(self):
        print("Personal Section")
class AlbumSection(Section):
    def describe(self):
        print("Album Section")
class PatentSection(Section):
    def describe(self):
        print("Patent Section")
class PublicationSection(Section):
    def describe(self):
        print("Publication Section")
#Factory class
class Profile(ABC):
    def __init__(self):
        self.sections = []
        self.createProfile()
    @abstractmethod
    def createProfile(self):
        pass
    def getSections(self):
        return self.sections
    def addSections(self, section):
        self.sections.append(section)
class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())
class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

profile_type = input("Profil apa yang ingin anda buat? [Linkedin atau Facebook:]")
profile = eval(profile_type.lower())()
print(f"Profil {type(profile).__name__} sedang dibuat..")
print("Profil mempunyai Section:")
for section in profile.getSections():
    print(section)

#no3

from abc import abstractmethod
class Animal:
    @abstractmethod
    def speak(self):
        pass

class Kucing:
    def speak(self):
        return "Miaww!!"
class Jerapah:
    def speak(self):
        return "Bruahh!!"
class Kangguru:
    def speak(self):
        return "Ngikkk..."

class AnimalFactory:
    def create_animal (self, animal_type):
        if animal_type == "kucing":
            return Kucing()
        if animal_type == "Kangguru":
            return Kangguru()
        if animal_type == "jerapah":
            return Jerapah()
        else:
            return None
if __name__ == "__main__":
    factory = AnimalFactory()

kucing = factory.create_animal("kucing")
print (f"suara kucing {kucing.speak()}")

jerapah = factory.create_animal("jerapah")
print (f"suara jerapah: {jerapah.speak()}")