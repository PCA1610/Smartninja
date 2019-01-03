
class Person(object):
    #first_name = ""

    def __init__(self, first_name, last_name,  phone_number, birth_year, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_year = birth_year
        self.email = email

    def set_first_name(self, first_name):
        self.first_name = first_name

    def print_human(self):
        print self.first_name
        print self.last_name
        print self.phone_number
        print self.birth_year
        print self.email
        print "-----------------"


def add_contact():
    person1 = Person("Philipp", "Andre", "06803286046", 1987, "philippandre1@gmx.at")
    person2 = Person("Anna", "Andre", "06803286046", 1987, "philippandre1@gmx.at")
    person3 = Person("Bruce", "Wayne", 902432309443, 1939, "bruce@batman.com")

    person_list = [person1, person2, person3]
    return person_list


def print_users(contact_book):
    for item in contact_book:
        item.print_human()


def user_choice():
    print ("1 : Print Contact Book")
    print "2: Add Contact"
    print "3: Delete Contact"
    user_input = int(raw_input("Take your choice:"))

    return user_input


def add_new_contact():
    user_input_first_name = raw_input("first name?: ")
    user_input_last_name = raw_input("last name?: ")
    user_input_phone_number = int(raw_input("Phone Number?: "))
    user_input_birth_year = int(raw_input("Birth Year?: "))
    user_input_email = raw_input("Email?: ")
    new_person = Person(user_input_first_name, user_input_last_name, user_input_phone_number, user_input_birth_year,
                        user_input_email)

    return new_person


def main():
    print "debug"
    contact_list = []

    user_input = user_choice()
    if user_input == 1:
        print_users(contact_list)
    elif user_input == 2:
        contact_list.append(add_new_contact())


if __name__ == "__main__":
    main()
