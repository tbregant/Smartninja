
class Oseba(object):

    def __init__(self, ime):
        self.ime = ime


class ContactBook(object):

    def __init__(self):
        self.entries = []

    def add_contact(self, ime):
        self.entries.append(Oseba(ime))

    def update_contact(self, old_ime, new_ime):
        for person in self.entries:
            if person.ime == old_ime:
                person.ime = new_ime

    def delete_contact(self, ime):
        for n, person in enumerate(self.entries):
            if person.ime == ime:
                index_to_delete = n
        self.entries.pop(index_to_delete)

    def __str__(self):
        return_string = ""
        for person in self.entries:
            return_string += person.ime+"\n"
        return return_string


if __name__ == '__main__':
    contact_book = ContactBook()
    contact_book.add_contact("Tomaz")
    contact_book.add_contact("Maja")
    print contact_book # klice se __str__ metoda objekta!

    contact_book.update_contact("Tomaz", "new")
    print contact_book

    contact_book.delete_contact("Maj")
    print contact_book