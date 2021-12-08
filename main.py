
class Bird:

        #class attributes
        attr1 = "bird"
        attr2 = "type"

        #instance attributes
        def __init__(self, name, species):
            self.name = name
            self.species = species

        def get_name(self):
            return self.name

        def get_species(self):
            return self.species

        def speak(self):
            print("My name is {}".format(self.name), "and I am a {}".format(self.species))



if __name__ == '__main__':
    name1 = input("Name your first bird: ")
    name2 = input("Name your second bird: ")
    species1 = input("First species of bird: ")
    species2 = input("Second species of bird: ")
    b1 = Bird(name1, species1)
    b2 = Bird(name2, species2)
    b1.speak()
    b2.speak()

