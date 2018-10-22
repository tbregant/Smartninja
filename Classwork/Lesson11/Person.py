
class Person(object):

    def __init__ (self, firstname, surname, age):
        self.firstname = firstname
        self.surname = surname
        self.age = age
        self.name = str(firstname) + " " + str(surname)


    def show_person(self):
        print "Ime: {}\nPriimek: {}\nStarost: {}".format(self.firstname,
                                                         self.surname,
                                                         self.age)


    def age_in_months(self):
        return self.age*12


if __name__ == '__main__':
    oseba = Person("Miha", "Mihovc", 30)
    oseba.show_person()
    print oseba.age_in_months()


person_list = [Person("ime1", "prim2", 12), Person("ime2", "primer2", 44), Person("ime3", "prim2", 66)]

for p in person_list:
    p.show_person()

